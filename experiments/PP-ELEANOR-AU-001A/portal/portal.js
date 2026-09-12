/**
 * PP-ELEANOR-AU-001A FIXTURE portal — browser-local state only.
 * No eval, no network AI, no auth.
 */
(function () {
  "use strict";

  var STORAGE_KEY = "pp-eleanor-au-001a-fixture";
  var CASE_ID = "PP-ELEANOR-AU-001A-FIXTURE";
  var SCHEMA_VERSION = 1;
  var MAX_IMPORT_BYTES = 64 * 1024;
  var MAX_NOTES_CHARS = 8 * 1024;

  var VALID_TOKENS = Object.freeze([
    "FIXTURE-NMC-0001",
    "FIXTURE-NMC-0002",
    "FIXTURE-CFD-0001",
    "FIXTURE-CFD-0002",
    "FIXTURE-LIL-0001",
    "FIXTURE-LIL-0002"
  ]);

  var KNOWN_EPISODES = Object.freeze(["FX1"]);
  var KNOWN_HINTS = Object.freeze(["FX-HINT-001", "FX-HINT-002"]);
  var KNOWN_CLAIM_VALUES = Object.freeze(["supported", "contested", "disproved"]);

  var REVEAL_A = "FIXTURE-NMC-0001";
  var REVEAL_B = "FIXTURE-CFD-0001";
  var CLAIM_ID = "FX-CLAIM-001";

  var TOKEN_META = Object.freeze({
    "FIXTURE-NMC-0001": {
      title: "Sample Notice: Fixture Subject A Seeks Forwarding Address",
      institution: "Northbridge Sample Tribune Clipping Desk (FIXTURE)",
      href: "../archives/northbridge-municipal-clippings/artifacts/fixture-nmc-0001.html"
    },
    "FIXTURE-CFD-0001": {
      title: "Docket Slip: Fixture Subject A — Counter Visit",
      institution: "Cedar Fork Sample Registry Deed Room (FIXTURE)",
      href: "../archives/cedar-fork-deed-room/artifacts/fixture-cfd-0001.html"
    }
  });

  function defaultState() {
    return {
      case_id: CASE_ID,
      schema_version: SCHEMA_VERSION,
      evidence_tokens: [],
      claim_states: {},
      episodes_open: ["FX1"],
      hints_used: [],
      notes: "",
      updated_at: new Date().toISOString()
    };
  }

  function isValidImport(obj) {
    return (
      obj &&
      typeof obj === "object" &&
      obj.case_id === CASE_ID &&
      obj.schema_version === SCHEMA_VERSION
    );
  }

  function dedupeValidTokens(list) {
    var out = [];
    if (!Array.isArray(list)) return out;
    list.forEach(function (t) {
      if (typeof t !== "string") return;
      var tok = t.trim().toUpperCase();
      if (VALID_TOKENS.indexOf(tok) === -1) return;
      if (out.indexOf(tok) === -1) out.push(tok);
    });
    return out;
  }

  function normalizeState(s) {
    var out = defaultState();
    out.evidence_tokens = dedupeValidTokens(s.evidence_tokens);

    out.claim_states = {};
    if (s.claim_states && typeof s.claim_states === "object") {
      var cv = s.claim_states[CLAIM_ID];
      if (typeof cv === "string" && KNOWN_CLAIM_VALUES.indexOf(cv) !== -1) {
        out.claim_states[CLAIM_ID] = cv;
      }
    }

    out.episodes_open = [];
    if (Array.isArray(s.episodes_open)) {
      s.episodes_open.forEach(function (id) {
        if (typeof id === "string" && KNOWN_EPISODES.indexOf(id) !== -1 && out.episodes_open.indexOf(id) === -1) {
          out.episodes_open.push(id);
        }
      });
    }
    if (!out.episodes_open.length) out.episodes_open = ["FX1"];

    out.hints_used = [];
    if (Array.isArray(s.hints_used)) {
      s.hints_used.forEach(function (id) {
        if (typeof id === "string" && KNOWN_HINTS.indexOf(id) !== -1 && out.hints_used.indexOf(id) === -1) {
          out.hints_used.push(id);
        }
      });
    }

    if (typeof s.notes === "string") {
      out.notes = s.notes.length > MAX_NOTES_CHARS ? s.notes.slice(0, MAX_NOTES_CHARS) : s.notes;
    } else {
      out.notes = "";
    }

    out.updated_at = typeof s.updated_at === "string" ? s.updated_at : out.updated_at;
    return out;
  }

  function loadState() {
    try {
      var raw = localStorage.getItem(STORAGE_KEY);
      if (!raw) return defaultState();
      var parsed = JSON.parse(raw);
      if (!isValidImport(parsed)) return defaultState();
      return normalizeState(parsed);
    } catch (e) {
      return defaultState();
    }
  }

  function saveState(state) {
    state.updated_at = new Date().toISOString();
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  }

  var state = loadState();
  var revealWasOpen = false;

  var els = {
    accession: document.getElementById("accession-input"),
    notes: document.getElementById("notes-input"),
    validateBtn: document.getElementById("validate-btn"),
    status: document.getElementById("validate-status"),
    tokenList: document.getElementById("token-list"),
    reveal: document.getElementById("cast-reveal"),
    revealAnnounce: document.getElementById("reveal-announce"),
    receiptList: document.getElementById("receipt-list"),
    claimRadios: document.querySelectorAll('input[name="claim-class"]'),
    claimStatus: document.getElementById("claim-status"),
    nextQ: document.getElementById("next-research-q"),
    exportBtn: document.getElementById("export-btn"),
    importInput: document.getElementById("import-input"),
    resetBtn: document.getElementById("reset-btn"),
    copyPrompt: document.getElementById("copy-prompt-btn"),
    researchPrompt: document.getElementById("research-prompt"),
    importStatus: document.getElementById("import-status")
  };

  function setStatus(el, kind, message) {
    if (!el) return;
    el.className = "status " + kind;
    el.textContent = message;
    el.hidden = !message;
  }

  function renderTokens() {
    if (!els.tokenList) return;
    els.tokenList.innerHTML = "";
    if (!state.evidence_tokens.length) {
      var empty = document.createElement("li");
      empty.textContent = "(none yet)";
      empty.style.background = "transparent";
      empty.style.fontFamily = "inherit";
      els.tokenList.appendChild(empty);
      return;
    }
    state.evidence_tokens.forEach(function (tok) {
      var li = document.createElement("li");
      li.textContent = tok;
      els.tokenList.appendChild(li);
    });
  }

  function hasRevealPair() {
    return (
      state.evidence_tokens.indexOf(REVEAL_A) !== -1 &&
      state.evidence_tokens.indexOf(REVEAL_B) !== -1
    );
  }

  function renderReceipts() {
    if (!els.receiptList) return;
    els.receiptList.innerHTML = "";
    [REVEAL_A, REVEAL_B].forEach(function (tok) {
      var meta = TOKEN_META[tok];
      if (!meta) return;
      var li = document.createElement("li");
      li.className = "receipt-card";
      li.innerHTML =
        '<p class="receipt-label">Evidence receipt</p>' +
        '<p class="accession">' + tok + "</p>" +
        "<p><strong>" + meta.title + "</strong></p>" +
        "<p class=\"muted\">Institution: " + meta.institution + "</p>" +
        '<p><a href="' + meta.href + '">Open source artifact</a></p>';
      els.receiptList.appendChild(li);
    });
  }

  function renderReveal(announceUnlock) {
    if (!els.reveal) return;
    var open = hasRevealPair();
    els.reveal.hidden = !open;
    if (open) {
      renderReceipts();
      var current = state.claim_states[CLAIM_ID];
      els.claimRadios.forEach(function (r) {
        r.checked = current === r.value;
      });
      if (current) {
        setStatus(els.claimStatus, "ok", "Classification saved: " + current);
      } else {
        setStatus(els.claimStatus, "info", "Classify the CAST CLAIM to continue.");
      }
      if (announceUnlock && !revealWasOpen && els.revealAnnounce) {
        els.revealAnnounce.hidden = false;
        els.revealAnnounce.textContent =
          "Cast reveal unlocked. Evidence receipts for " +
          REVEAL_A +
          " and " +
          REVEAL_B +
          " are shown before cast dialogue.";
      }
    } else if (els.revealAnnounce) {
      els.revealAnnounce.textContent = "";
      els.revealAnnounce.hidden = true;
    }
    revealWasOpen = open;
  }

  function renderNotes() {
    if (els.notes) els.notes.value = state.notes || "";
  }

  function renderAll(announceUnlock) {
    renderTokens();
    renderReveal(!!announceUnlock);
    renderNotes();
  }

  function addToken(raw) {
    var token = String(raw || "").trim().toUpperCase();
    if (!token) {
      setStatus(els.status, "bad", "Enter an accession code.");
      return;
    }
    if (VALID_TOKENS.indexOf(token) === -1) {
      setStatus(
        els.status,
        "bad",
        "Invalid token. Use an exact FIXTURE-* code from the six sample artifacts."
      );
      return;
    }
    if (state.evidence_tokens.indexOf(token) !== -1) {
      setStatus(els.status, "info", "Duplicate token — already in evidence locker: " + token);
      if (els.accession) els.accession.value = "";
      renderAll(false);
      return;
    }
    var beforeReveal = hasRevealPair();
    state.evidence_tokens.push(token);
    saveState(state);
    setStatus(els.status, "ok", "New valid evidence token recorded: " + token);
    if (els.accession) els.accession.value = "";
    renderAll(!beforeReveal && hasRevealPair());
  }

  if (els.validateBtn) {
    els.validateBtn.addEventListener("click", function () {
      addToken(els.accession && els.accession.value);
    });
  }

  if (els.accession) {
    els.accession.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        addToken(els.accession.value);
      }
    });
  }

  function persistNotes() {
    if (!els.notes) return;
    var text = els.notes.value || "";
    if (text.length > MAX_NOTES_CHARS) {
      text = text.slice(0, MAX_NOTES_CHARS);
      els.notes.value = text;
      setStatus(els.status, "info", "Notes truncated to 8KB.");
    }
    state.notes = text;
    saveState(state);
  }

  if (els.notes) {
    els.notes.addEventListener("change", persistNotes);
    els.notes.addEventListener("blur", persistNotes);
  }

  els.claimRadios.forEach(function (radio) {
    radio.addEventListener("change", function () {
      if (!hasRevealPair()) return;
      state.claim_states[CLAIM_ID] = radio.value;
      saveState(state);
      setStatus(els.claimStatus, "ok", "Classification saved: " + radio.value);
    });
  });

  if (els.copyPrompt && els.researchPrompt) {
    els.copyPrompt.addEventListener("click", function () {
      var text = els.researchPrompt.textContent || "";
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(
          function () {
            setStatus(els.status, "info", "Research prompt copied to clipboard.");
          },
          function () {
            fallbackCopy(text);
          }
        );
      } else {
        fallbackCopy(text);
      }
    });
  }

  function fallbackCopy(text) {
    var ta = document.createElement("textarea");
    ta.value = text;
    document.body.appendChild(ta);
    ta.select();
    try {
      document.execCommand("copy");
      setStatus(els.status, "info", "Research prompt copied to clipboard.");
    } catch (e) {
      setStatus(els.status, "bad", "Could not copy automatically — select the prompt text manually.");
    }
    document.body.removeChild(ta);
  }

  if (els.exportBtn) {
    els.exportBtn.addEventListener("click", function () {
      persistNotes();
      var blob = new Blob([JSON.stringify(state, null, 2)], { type: "application/json" });
      var url = URL.createObjectURL(blob);
      var a = document.createElement("a");
      a.href = url;
      a.download = "pp-eleanor-au-001a-fixture-state.json";
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
      URL.revokeObjectURL(url);
      setStatus(els.importStatus, "ok", "Exported current case state as JSON.");
    });
  }

  function clearImportInput() {
    if (els.importInput) els.importInput.value = "";
  }

  if (els.importInput) {
    els.importInput.addEventListener("change", function () {
      var file = els.importInput.files && els.importInput.files[0];
      if (!file) return;
      if (file.size > MAX_IMPORT_BYTES) {
        setStatus(
          els.importStatus,
          "bad",
          "Import rejected: file exceeds 64KB size limit."
        );
        clearImportInput();
        return;
      }
      var reader = new FileReader();
      reader.onload = function () {
        try {
          var rawText = String(reader.result || "");
          if (rawText.length > MAX_IMPORT_BYTES) {
            setStatus(els.importStatus, "bad", "Import rejected: payload exceeds 64KB.");
            clearImportInput();
            return;
          }
          var parsed = JSON.parse(rawText);
          if (!isValidImport(parsed)) {
            setStatus(
              els.importStatus,
              "bad",
              "Import rejected: case_id must be " +
                CASE_ID +
                " and schema_version must be " +
                SCHEMA_VERSION +
                "."
            );
            clearImportInput();
            return;
          }
          state = normalizeState(parsed);
          saveState(state);
          revealWasOpen = false;
          renderAll(hasRevealPair());
          setStatus(els.importStatus, "ok", "Import accepted. State restored.");
        } catch (err) {
          setStatus(els.importStatus, "bad", "Import failed: file is not valid JSON.");
        }
        clearImportInput();
      };
      reader.onerror = function () {
        setStatus(els.importStatus, "bad", "Import failed: could not read file.");
        clearImportInput();
      };
      reader.readAsText(file);
    });
  }

  if (els.resetBtn) {
    els.resetBtn.addEventListener("click", function () {
      var ok = window.confirm(
        "Reset fixture case state? Export your JSON first if you want to keep it. This clears evidence tokens, claims, and notes in localStorage."
      );
      if (!ok) return;
      state = defaultState();
      saveState(state);
      revealWasOpen = false;
      setStatus(els.status, "info", "Case state reset.");
      setStatus(els.importStatus, "info", "");
      setStatus(els.claimStatus, "info", "");
      if (els.revealAnnounce) els.revealAnnounce.textContent = "";
      renderAll(false);
    });
  }

  revealWasOpen = hasRevealPair();
  renderAll(false);
})();
