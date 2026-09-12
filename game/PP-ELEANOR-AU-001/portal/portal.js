(function () {
  "use strict";
  var CASE_ID = "PP-ELEANOR-AU-001";
  var STORAGE_KEY = "pp-eleanor-au-001-v1";
  var SCHEMA = 1;
  var MAX_NOTES = 8192;
  var MAX_IMPORT = 64 * 1024;
  var VALID = Object.freeze([
    "CIM-HART-1912-01",
    "OIM-HW-1946-07",
    "BHR-PH-1951-17",
    "RRG-1948-10-18-A",
    "CIM-EH-1912-NB"
  ]);
  var MSG = {
    empty: "Your locker is empty. Start with the photograph, but do not save its label as a fact until you know who wrote it.",
    invalid: "That accession code does not match an available record. Check spaces, punctuation, and the visible archive page. A guessed code cannot unlock evidence.",
    duplicate: "Already in your locker. Add a new observation or return to the source instead of collecting the same code twice."
  };

  var scripts = null;
  var content = null;
  var state = defaultState();
  var activeSceneId = null;

  function defaultState() {
    return {
      case_id: CASE_ID,
      schema_version: SCHEMA,
      evidence_tokens: [],
      claim_states: {},
      episodes_open: ["E0", "E1"],
      active_episode: null,
      episode_opened: {},
      scenes_played: [],
      hints_used: [],
      notes: "",
      updated_at: new Date().toISOString()
    };
  }

  function $(id) { return document.getElementById(id); }

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaultState();
      var p = JSON.parse(raw);
      if (!p || p.case_id !== CASE_ID || p.schema_version !== SCHEMA) return defaultState();
      return normalize(p);
    } catch (e) {
      return defaultState();
    }
  }

  function normalize(s) {
    var out = defaultState();
    out.evidence_tokens = [];
    (s.evidence_tokens || []).forEach(function (t) {
      if (typeof t === "string" && VALID.indexOf(t) !== -1 && out.evidence_tokens.indexOf(t) === -1) out.evidence_tokens.push(t);
    });
    out.claim_states = {};
    if (s.claim_states && typeof s.claim_states === "object") {
      Object.keys(s.claim_states).forEach(function (cid) {
        var v = s.claim_states[cid];
        if (typeof v === "string" && ["supported", "contested", "disproved"].indexOf(v) !== -1) {
          out.claim_states[cid] = { status: v, history: [] };
        } else if (v && typeof v === "object" && ["supported", "contested", "disproved"].indexOf(v.status) !== -1) {
          out.claim_states[cid] = {
            status: v.status,
            history: Array.isArray(v.history) ? v.history.filter(function (h) {
              return h && ["supported", "contested", "disproved", "unset"].indexOf(String(h.from).toLowerCase()) !== -1;
            }) : []
          };
        }
      });
    }
    out.episodes_open = ["E0", "E1"];
    out.active_episode = s.active_episode === "E0" || s.active_episode === "E1" ? s.active_episode : null;
    out.episode_opened = {};
    if (s.episode_opened && typeof s.episode_opened === "object") {
      ["E0", "E1"].forEach(function (e) { if (s.episode_opened[e]) out.episode_opened[e] = true; });
    }
    out.scenes_played = Array.isArray(s.scenes_played) ? s.scenes_played.filter(function (x) { return typeof x === "string"; }) : [];
    out.hints_used = Array.isArray(s.hints_used) ? s.hints_used : [];
    out.notes = typeof s.notes === "string" ? s.notes.slice(0, MAX_NOTES) : "";
    out.updated_at = typeof s.updated_at === "string" ? s.updated_at : out.updated_at;
    return out;
  }

  function save() {
    state.updated_at = new Date().toISOString();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  function setStatus(el, kind, msg) {
    if (!el) return;
    el.hidden = !msg;
    el.className = "status " + (kind || "info");
    el.textContent = msg || "";
  }

  function artifactById(id) {
    if (!content) return null;
    for (var i = 0; i < content.artifacts.length; i++) {
      if (content.artifacts[i].id === id) return content.artifacts[i];
    }
    return null;
  }

  function artifactByAccession(code) {
    if (!content) return null;
    for (var i = 0; i < content.artifacts.length; i++) {
      if (content.artifacts[i].accession_code === code) return content.artifacts[i];
    }
    return null;
  }

  function archiveBase(surface) {
    var map = {
      "Cincinnati Industrial Memory Archive": "../archives/cincinnati-industrial-memory",
      "Ohio River Industrial Memory Project": "../archives/ohio-river-industrial-memory",
      "Bellwether Historical Register": "../archives/bellwether-historical-register",
      "River & Rail Gazette Archive": "../archives/river-and-rail-gazette"
    };
    return map[surface] || "../archives";
  }

  function episodeById(id) {
    if (!scripts) return null;
    for (var i = 0; i < scripts.episodes.length; i++) {
      if (scripts.episodes[i].id === id) return scripts.episodes[i];
    }
    return null;
  }

  function triggerOk(tr) {
    if (!tr) return false;
    if (tr.episode_opened) {
      if (!state.active_episode || !state.episode_opened[state.active_episode]) return false;
    }
    if (tr.all_tokens) {
      for (var i = 0; i < tr.all_tokens.length; i++) {
        if (state.evidence_tokens.indexOf(tr.all_tokens[i]) === -1) return false;
      }
    }
    if (tr.any_tokens) {
      var any = false;
      for (var j = 0; j < tr.any_tokens.length; j++) {
        if (state.evidence_tokens.indexOf(tr.any_tokens[j]) !== -1) any = true;
      }
      if (!any) return false;
    }
    if (tr.none_tokens) {
      for (var k = 0; k < tr.none_tokens.length; k++) {
        if (state.evidence_tokens.indexOf(tr.none_tokens[k]) !== -1) return false;
      }
    }
    return true;
  }

  function eligibleScenes() {
    if (!state.active_episode) return [];
    var ep = episodeById(state.active_episode);
    if (!ep) return [];
    return ep.scenes.filter(function (sc) {
      if (state.scenes_played.indexOf(sc.id) !== -1) return false;
      return triggerOk(sc.trigger || {});
    }).sort(function (a, b) { return (a.priority || 0) - (b.priority || 0); });
  }

  function renderTokens() {
    var ul = $("token-list");
    ul.innerHTML = "";
    if (!state.evidence_tokens.length) {
      var li = document.createElement("li");
      li.textContent = MSG.empty;
      li.style.fontFamily = "inherit";
      li.style.background = "transparent";
      ul.appendChild(li);
      return;
    }
    state.evidence_tokens.forEach(function (t) {
      var li = document.createElement("li");
      li.textContent = t;
      ul.appendChild(li);
    });
  }

  function claimObj(id) {
    return state.claim_states[id] || null;
  }

  function renderClaimUI(sc) {
    var block = $("claim-block");
    if (!sc.claim_id || !sc.claim_text) {
      block.hidden = true;
      return;
    }
    block.hidden = false;
    $("claim-banner").textContent = "CAST CLAIM";
    $("claim-text").textContent = sc.claim_text;
    var pr = sc.player_ruling;
      $("claim-prompt").textContent = (pr && typeof pr === "object") ? (pr.prompt || "") : (pr || "");
    var cur = claimObj(sc.claim_id);
    var status = cur ? cur.status : "unset";
    var st = $("claim-current-status");
    st.textContent = status === "unset" ? "Unset" : status.charAt(0).toUpperCase() + status.slice(1);
    st.setAttribute("data-status", status);
    Array.prototype.forEach.call(document.querySelectorAll('input[name="claim-class"]'), function (r) {
      r.checked = cur && r.value === cur.status;
    });
    var trail = $("claim-edit-trail");
    var list = $("claim-trail-list");
    list.innerHTML = "";
    if (cur && cur.history && cur.history.length) {
      trail.hidden = false;
      var desc = [];
      cur.history.forEach(function (h) {
        var li = document.createElement("li");
        var line = String(h.from).toUpperCase() + " → " + String(h.to).toUpperCase();
        li.textContent = line;
        list.appendChild(li);
        desc.push(line);
      });
      $("claim-trail-desc").textContent = "Ruling history: " + desc.join("; ");
    } else {
      trail.hidden = true;
    }
  }

  function renderScene(sc) {
    activeSceneId = sc ? sc.id : null;
    $("scene-empty").hidden = !!sc;
    $("scene-stage").hidden = !sc;
    if (!sc) return;
    $("scene-id-label").textContent = sc.id + " · priority " + sc.priority;
    var receipt = $("receipt-block");
    var list = $("receipt-list");
    list.innerHTML = "";
    var arts = [];
    if (sc.display_artifact_id) {
      var one = artifactById(sc.display_artifact_id);
      if (one) arts.push(one);
    }
    if (sc.trigger && sc.trigger.all_tokens) {
      sc.trigger.all_tokens.forEach(function (code) {
        var a = artifactByAccession(code);
        if (a && arts.indexOf(a) === -1) arts.push(a);
      });
    }
    if (arts.length) {
      receipt.hidden = false;
      arts.forEach(function (a) {
        var li = document.createElement("li");
        li.className = "receipt-card";
        var href = archiveBase(a.surface) + a.slug + "/";
        li.innerHTML = "<p class=\"receipt-label\">Evidence receipt</p>" +
          "<p><strong>" + a.record_title.replace(/</g, "&lt;") + "</strong></p>" +
          "<p>" + a.surface.replace(/</g, "&lt;") + "</p>" +
          "<p class=\"acc\">" + a.accession_code + "</p>" +
          "<p><a href=\"" + href + "\">Open source record</a></p>";
        list.appendChild(li);
      });
    } else {
      receipt.hidden = true;
    }
    var dlg = $("dialogue-block");
    dlg.innerHTML = "";
    (sc.dialogue || []).forEach(function (d) {
      var art = document.createElement("article");
      art.className = "claim-block";
      var label = document.createElement("p");
      label.className = "claim-banner";
      var mode = String(d.mode || d.role || "").toLowerCase();
      label.textContent = (mode === "crossfire" || mode.indexOf("cross") !== -1) ? "CROSS-EXAMINATION" : "CAST CLAIM";
      var who = document.createElement("h3");
      who.textContent = (d.speaker || d.cast_id || "Investigator") + (d.lens ? " / " + d.lens : "");
      var body = document.createElement("p");
      body.textContent = d.text || d.line || "";
      art.appendChild(label);
      art.appendChild(who);
      art.appendChild(body);
      dlg.appendChild(art);
    });
    renderClaimUI(sc);
    $("next-action").textContent = sc.next_action || "";
    if (state.scenes_played.indexOf(sc.id) === -1) {
      state.scenes_played.push(sc.id);
      if (sc.state_effects) {
        sc.state_effects.forEach(function (ef) {
          if (ef.claim_id && ef.set_expected) {
            /* expected ruling hint only — do not auto-set player claim */
          }
        });
      }
      save();
    }
  }

  function pickScene() {
    var elig = eligibleScenes();
    $("scene-queue").hidden = !elig.length;
    $("scene-queue").textContent = elig.length ? ("Eligible: " + elig.map(function (s) { return s.id; }).join(", ")) : "";
    if (!elig.length) {
      renderScene(null);
      return;
    }
    renderScene(elig[0]);
  }

  function updateQuestion() {
    var el = $("cq-text");
    if (!state.active_episode) {
      el.textContent = "Complete onboarding to open a case movement.";
      return;
    }
    var ep = episodeById(state.active_episode);
    if (!ep) return;
    el.textContent = ep.mission || ep.title || state.active_episode;
    if (ep.player_agent_prompt) {
      $("episode-prompt-wrap").hidden = false;
      $("episode-prompt").textContent = ep.player_agent_prompt;
    }
  }

  function openEpisode(id) {
    state.active_episode = id;
    state.episode_opened[id] = true;
    if (state.episodes_open.indexOf(id) === -1) state.episodes_open.push(id);
    save();
    updateQuestion();
    pickScene();
    renderHints();
  }

  function renderHints() {
    var ep = state.active_episode ? episodeById(state.active_episode) : null;
    var list = $("hints-list");
    list.innerHTML = "";
    if (!ep || !ep.recovery_hints || !ep.recovery_hints.length) {
      $("hints-empty").hidden = false;
      $("btn-hint").hidden = true;
      return;
    }
    $("hints-empty").hidden = true;
    $("btn-hint").hidden = false;
    var used = state.hints_used.filter(function (h) { return String(h).indexOf(ep.id) === 0 || true; });
    var count = 0;
    state.hints_used.forEach(function (h) {
      if (typeof h === "string" && h.indexOf(ep.id + ":") === 0) count++;
    });
    for (var i = 0; i < Math.min(count, ep.recovery_hints.length); i++) {
      var li = document.createElement("li");
      var h = ep.recovery_hints[i];
      li.textContent = typeof h === "string" ? h : (h.text || h.hint || JSON.stringify(h));
      list.appendChild(li);
    }
  }

  function onValidate() {
    var raw = ($("accession-input").value || "").trim();
    var code = raw.toUpperCase();
    // preserve exact case from VALID list
    var match = null;
    for (var i = 0; i < VALID.length; i++) {
      if (VALID[i].toUpperCase() === code) match = VALID[i];
    }
    if (!match) {
      setStatus($("validate-status"), "err", MSG.invalid);
      return;
    }
    if (state.evidence_tokens.indexOf(match) !== -1) {
      setStatus($("validate-status"), "info", MSG.duplicate);
      return;
    }
    state.evidence_tokens.push(match);
    save();
    renderTokens();
    setStatus($("validate-status"), "ok", "Recorded " + match + ".");
    $("accession-input").value = "";
    pickScene();
  }

  function onClaimChange(val) {
    var sc = null;
    var elig = eligibleScenes().concat(
      (episodeById(state.active_episode) || { scenes: [] }).scenes.filter(function (s) {
        return state.scenes_played.indexOf(s.id) !== -1;
      })
    );
    for (var i = 0; i < elig.length; i++) {
      if (elig[i].id === activeSceneId) sc = elig[i];
    }
    if (!sc && state.active_episode) {
      var ep = episodeById(state.active_episode);
      for (var j = 0; j < ep.scenes.length; j++) if (ep.scenes[j].id === activeSceneId) sc = ep.scenes[j];
    }
    if (!sc || !sc.claim_id) return;
    var prev = claimObj(sc.claim_id);
    var from = prev ? prev.status : "unset";
    if (from === val) return;
    var history = prev && prev.history ? prev.history.slice() : [];
    history.push({ from: from, to: val, at: new Date().toISOString() });
    state.claim_states[sc.claim_id] = { status: val, history: history };
    save();
    renderClaimUI(sc);
    setStatus($("claim-status"), "ok", "Ruling saved: " + val + ".");
  }


  function applyEvidenceShot() {
    try {
      var params = new URLSearchParams(location.search || "");
      var shot = params.get("evidenceShot");
      if (!shot) return;
      if (shot === "invalid") {
        $("accession-input").value = "BAD-CODE-99";
        onValidate();
        $("locker").scrollIntoView();
      } else if (shot === "duplicate") {
        state.evidence_tokens = ["CIM-HART-1912-01"];
        save();
        renderTokens();
        $("accession-input").value = "CIM-HART-1912-01";
        onValidate();
        $("locker").scrollIntoView();
      } else if (shot === "focus") {
        $("validate-btn").focus();
        $("locker").scrollIntoView();
      } else if (shot === "comparison" || shot === "trail") {
        state.active_episode = "E1";
        state.episode_opened.E1 = true;
        state.evidence_tokens = ["OIM-HW-1946-07", "BHR-PH-1951-17"];
        state.scenes_played = ["E1-S01-INTAKE", "E1-S02-ARTICLE_FIRST"];
        if (shot === "trail") {
          state.claim_states["E1-C02"] = {
            status: "supported",
            history: [
              { from: "unset", to: "contested", at: "2026-09-12T18:00:00.000Z" },
              { from: "contested", to: "supported", at: "2026-09-12T18:01:00.000Z" }
            ]
          };
        }
        save();
        updateQuestion();
        pickScene();
        renderTokens();
        $("scene").scrollIntoView();
      } else if (shot === "sticky") {
        state.active_episode = "E1";
        state.episode_opened.E1 = true;
        save();
        updateQuestion();
        window.scrollTo(0, 0);
      }
    } catch (e) {
      console.error(e);
    }
  }

  function bind() {
    $("btn-open-1948").addEventListener("click", function () { openEpisode("E1"); });
    $("btn-need-1912").addEventListener("click", function () { openEpisode("E0"); });
    $("btn-know-e0").addEventListener("click", function () { openEpisode("E1"); });
    $("btn-how-web").addEventListener("click", function () { $("how-web-panel").hidden = false; });
    $("btn-dismiss-how").addEventListener("click", function () { $("how-web-panel").hidden = true; });
    $("validate-btn").addEventListener("click", onValidate);
    $("accession-input").addEventListener("keydown", function (e) {
      if (e.key === "Enter") onValidate();
    });
    $("copy-prompt-btn").addEventListener("click", function () {
      var t = $("research-prompt").textContent;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(t).then(function () {
          setStatus($("prompt-status"), "ok", "Copied standing brief.");
        });
      }
    });
    Array.prototype.forEach.call(document.querySelectorAll('input[name="claim-class"]'), function (r) {
      r.addEventListener("change", function () { if (r.checked) onClaimChange(r.value); });
    });
    $("btn-continue-scene").addEventListener("click", function () {
      pickScene();
      $("locker").scrollIntoView({ block: "start" });
    });
    $("btn-hint").addEventListener("click", function () {
      var ep = episodeById(state.active_episode);
      if (!ep || !ep.recovery_hints) return;
      var count = 0;
      state.hints_used.forEach(function (h) {
        if (typeof h === "string" && h.indexOf(ep.id + ":") === 0) count++;
      });
      if (count >= ep.recovery_hints.length) return;
      state.hints_used.push(ep.id + ":" + count);
      save();
      renderHints();
    });
    $("notes-input").addEventListener("input", function () {
      state.notes = ($("notes-input").value || "").slice(0, MAX_NOTES);
      save();
    });
    $("export-btn").addEventListener("click", function () {
      var blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
      var a = document.createElement("a");
      a.href = URL.createObjectURL(blob);
      a.download = "pp-eleanor-au-001-case-state.json";
      a.click();
      URL.revokeObjectURL(a.href);
    });
    $("import-input").addEventListener("change", function () {
      var f = $("import-input").files && $("import-input").files[0];
      if (!f) return;
      if (f.size > MAX_IMPORT) {
        setStatus($("import-status"), "err", "Import rejected: file exceeds 64KB.");
        $("import-input").value = "";
        return;
      }
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var obj = JSON.parse(String(reader.result || ""));
          if (!obj || obj.case_id !== CASE_ID || obj.schema_version !== SCHEMA) {
            setStatus($("import-status"), "err", "Import rejected: case_id/schema mismatch (fixture exports are not accepted).");
            $("import-input").value = "";
            return;
          }
          state = normalize(obj);
          save();
          $("notes-input").value = state.notes || "";
          renderTokens();
          updateQuestion();
          pickScene();
          renderHints();
          setStatus($("import-status"), "ok", "Import restored.");
        } catch (e) {
          setStatus($("import-status"), "err", "Import rejected: invalid JSON.");
        }
        $("import-input").value = "";
      };
      reader.readAsText(f);
    });
    $("reset-btn").addEventListener("click", function () {
      if (!window.confirm("Reset this case? Export first if you need a backup.")) return;
      state = defaultState();
      save();
      $("notes-input").value = "";
      renderTokens();
      updateQuestion();
      renderScene(null);
      renderHints();
      setStatus($("import-status"), "info", "Case reset.");
    });
  }

  function boot() {
    state = loadState();
    Promise.all([
      fetch("../content/episode-scripts.json").then(function (r) { return r.json(); }),
      fetch("../content/public-content.json").then(function (r) { return r.json(); })
    ]).then(function (pair) {
      scripts = pair[0];
      content = pair[1];
      bind();
      $("notes-input").value = state.notes || "";
      renderTokens();
      updateQuestion();
      pickScene();
      renderHints();
      applyEvidenceShot();
    }).catch(function (err) {
      setStatus($("validate-status"), "err", "Failed to load locked content JSON.");
      console.error(err);
    });
  }

  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
