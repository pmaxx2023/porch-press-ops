#!/usr/bin/env python3
"""
The Wrong Widow — Stage 4 Binder packet builder (deterministic).
Reads Canon documents.json + Trail design JSON; renders player / hints / sealed PDFs.
Does NOT invent mystery facts or ads.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

from reportlab.lib.colors import Color, black, white, HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, KeepTogether, HRFlowable, ListFlowable, ListItem,
    Flowable,
)

ROOT = Path(__file__).resolve().parents[1]
CANON = ROOT / "canon"
TRAIL = ROOT / "trail"
OUT = Path(__file__).resolve().parent

PAGE = letter
MARGIN = 0.7 * inch

# Grayscale-friendly palette
AGED = HexColor("#f4ecd8")
AGED_BORDER = HexColor("#8a7a5a")
INK = HexColor("#1a1a1a")
MUTED = HexColor("#444444")
SEALED_RED = HexColor("#7a1010")
LIGHT_RULE = HexColor("#b0a890")
HEADER_BG = HexColor("#e8dfc8")
CATALOG_BG = HexColor("#f7f3e8")


def load_json(path: Path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


DOCS = {d["document_id"]: d for d in load_json(CANON / "documents.json")["documents"]}
PLAYER_START = load_json(TRAIL / "player_start.json")
HINTS = load_json(TRAIL / "hint_ladder.json")
RUBRIC = load_json(TRAIL / "solution_rubric.json")
EVIDENCE = load_json(TRAIL / "evidence_map.json")


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(
        name="CoverTitle", fontName="Times-Bold", fontSize=28,
        leading=34, alignment=TA_CENTER, textColor=INK, spaceAfter=12,
    ))
    s.add(ParagraphStyle(
        name="CoverSub", fontName="Times-Italic", fontSize=12,
        leading=16, alignment=TA_CENTER, textColor=MUTED, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="H1", fontName="Times-Bold", fontSize=16,
        leading=20, textColor=INK, spaceBefore=6, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="H2", fontName="Times-Bold", fontSize=13,
        leading=16, textColor=INK, spaceBefore=10, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="Body", fontName="Times-Roman", fontSize=10.5,
        leading=14, textColor=INK, alignment=TA_JUSTIFY, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="BodyCenter", fontName="Times-Roman", fontSize=10.5,
        leading=14, textColor=INK, alignment=TA_CENTER, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="Small", fontName="Times-Roman", fontSize=9,
        leading=12, textColor=MUTED, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="FooterFacsimile", fontName="Times-Italic", fontSize=8,
        leading=10, textColor=MUTED, alignment=TA_CENTER,
    ))
    s.add(ParagraphStyle(
        name="ExhibitCode", fontName="Helvetica-Bold", fontSize=14,
        leading=16, textColor=INK, alignment=TA_LEFT,
    ))
    s.add(ParagraphStyle(
        name="ExhibitTitle", fontName="Times-Bold", fontSize=11,
        leading=14, textColor=INK, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="DocBody", fontName="Times-Roman", fontSize=11,
        leading=15, textColor=INK, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="DocBig", fontName="Times-Bold", fontSize=16,
        leading=20, textColor=INK, alignment=TA_CENTER, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="DocHuge", fontName="Times-Bold", fontSize=18,
        leading=22, textColor=INK, alignment=TA_CENTER, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="WorksheetQ", fontName="Times-Roman", fontSize=10.5,
        leading=14, textColor=INK, spaceBefore=8, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="HintRung", fontName="Helvetica-Bold", fontSize=12,
        leading=15, textColor=INK, spaceBefore=10, spaceAfter=4,
    ))
    s.add(ParagraphStyle(
        name="SealedBanner", fontName="Helvetica-Bold", fontSize=18,
        leading=22, textColor=SEALED_RED, alignment=TA_CENTER, spaceAfter=8,
    ))
    s.add(ParagraphStyle(
        name="CatalogCue", fontName="Times-Roman", fontSize=9.5,
        leading=12.5, textColor=INK, spaceAfter=3,
    ))
    s.add(ParagraphStyle(
        name="Warn", fontName="Times-Bold", fontSize=10,
        leading=13, textColor=SEALED_RED, alignment=TA_CENTER, spaceAfter=6,
    ))
    s.add(ParagraphStyle(
        name="BulletBody", fontName="Times-Roman", fontSize=10.5,
        leading=14, textColor=INK, leftIndent=12, spaceAfter=3,
    ))
    return s


STY = styles()


class AgedBox(Flowable):
    """A bordered aged-paper panel containing flowables."""

    def __init__(self, flowables, width, pad=10, min_height=0):
        Flowable.__init__(self)
        self.flowables = flowables
        self.box_width = width
        self.pad = pad
        self.min_height = min_height
        self._inner_height = 0

    def wrap(self, availWidth, availHeight):
        w = self.box_width
        inner_w = w - 2 * self.pad
        y = 0
        for f in self.flowables:
            fw, fh = f.wrap(inner_w, availHeight)
            y += fh + 4
        self._inner_height = max(y + self.pad, self.min_height)
        self.width = w
        self.height = self._inner_height + self.pad
        return self.width, self.height

    def draw(self):
        c = self.canv
        c.setFillColor(AGED)
        c.setStrokeColor(AGED_BORDER)
        c.setLineWidth(1.5)
        c.roundRect(0, 0, self.width, self.height, 4, fill=1, stroke=1)
        # inner thin rule
        c.setLineWidth(0.5)
        c.setStrokeColor(LIGHT_RULE)
        c.rect(4, 4, self.width - 8, self.height - 8, fill=0, stroke=1)
        inner_w = self.width - 2 * self.pad
        y = self.height - self.pad
        for f in self.flowables:
            fw, fh = f.wrap(inner_w, self.height)
            y -= fh
            f.drawOn(c, self.pad, y)
            y -= 4


def write_lines_space(story, n=3, gap=16):
    for _ in range(n):
        story.append(Spacer(1, gap))
        story.append(HRFlowable(width="100%", thickness=0.4, color=LIGHT_RULE, spaceBefore=0, spaceAfter=0))


# Player-facing exhibit titles: keep Canon fields, strip trap-softening labels
# (Canon titles may say Decoy / False divorce / red-herring — never print those to players.)
PLAYER_TITLE_OVERRIDES = {
    "D015": "Hospital register line — Silas M. Corbit, Co. B 83rd Indiana",
    "D016": "Ripley County divorce decree — Eli Corbin & Martha Ann Ashley",
    "D017": "Pension note — Harriet Whitcomb Keller (remarriage)",
}


def footer_facsimile():

    return Paragraph("Fictional facsimile for game use — not an authentic historical document.", STY["FooterFacsimile"])


def exhibit_header(doc_id: str, doc: dict):
    flows = []
    flows.append(Paragraph(doc_id, STY["ExhibitCode"]))
    title = PLAYER_TITLE_OVERRIDES.get(doc_id, doc.get("title", ""))
    flows.append(Paragraph(title, STY["ExhibitTitle"]))
    meta = f"<b>Date:</b> {doc.get('date', '')}&nbsp;&nbsp;&nbsp;<b>Place:</b> {doc.get('place', '')}"
    flows.append(Paragraph(meta, STY["Small"]))
    flows.append(Spacer(1, 4))
    flows.append(HRFlowable(width="100%", thickness=0.8, color=AGED_BORDER, spaceBefore=0, spaceAfter=6))
    return flows


def field_row(label, value, big=False):
    style = STY["DocHuge"] if big else STY["DocBody"]
    return Paragraph(f"<b>{label}:</b> {value}", style if not big else STY["DocBody"])


def render_fields_generic(doc: dict, big_keys=None):
    """Render recorded_fields as visible document content from data."""
    big_keys = big_keys or set()
    fields = doc.get("recorded_fields", {})
    flows = []
    for key, val in fields.items():
        if key == "noise":
            continue  # never surface internal noise notes to players
        label = key.replace("_", " ").title()
        if isinstance(val, list):
            if val and isinstance(val[0], dict):
                # household table handled elsewhere
                continue
            joined = ", ".join(str(x) for x in val)
            if key in big_keys:
                flows.append(Paragraph(f"<b>{label}:</b>", STY["DocBody"]))
                flows.append(Paragraph(joined, STY["DocHuge"]))
            else:
                flows.append(Paragraph(f"<b>{label}:</b> {joined}", STY["DocBody"]))
        elif isinstance(val, dict):
            continue
        else:
            text = str(val)
            if key in big_keys:
                flows.append(Paragraph(f"<b>{label}:</b>", STY["DocBody"]))
                flows.append(Paragraph(text, STY["DocHuge"]))
            else:
                flows.append(Paragraph(f"<b>{label}:</b> {text}", STY["DocBody"]))
    return flows


def household_table(rows, caption=None):
    flows = []
    if caption:
        flows.append(Paragraph(caption, STY["Small"]))
    data = [[
        Paragraph("<b>Name</b>", STY["Small"]),
        Paragraph("<b>Age</b>", STY["Small"]),
        Paragraph("<b>Relationship</b>", STY["Small"]),
    ]]
    for r in rows:
        data.append([
            Paragraph(str(r.get("name", "")), STY["DocBody"]),
            Paragraph(str(r.get("age", "")), STY["DocBody"]),
            Paragraph(str(r.get("relationship", "")), STY["DocBody"]),
        ])
        # marital_status_implied shown as ordinary text if present — no callout
        if r.get("marital_status_implied"):
            data[-1][2] = Paragraph(
                f"{r.get('relationship', '')} ({r['marital_status_implied']})",
                STY["DocBody"],
            )
    t = Table(data, colWidths=[2.6 * inch, 0.9 * inch, 2.4 * inch])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("GRID", (0, 0), (-1, -1), 0.5, AGED_BORDER),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    flows.append(t)
    return flows


def build_exhibit_content(doc_id: str) -> list:
    """Build facsimile body from documents.json recorded_fields. Special cases for HARD risks."""
    doc = DOCS[doc_id]
    fields = doc["recorded_fields"]
    flows = exhibit_header(doc_id, doc)
    body = []

    if doc_id == "D001":
        body.append(Paragraph("UNITED STATES PENSION BUREAU", STY["DocBig"]))
        body.append(Paragraph("Internal Routing Note — Contested Widow Claims", STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Soldier:</b> {fields['soldier']}", STY["DocBody"]))
        body.append(Spacer(1, 4))
        body.append(Paragraph(f"<b>Claimant A:</b> {fields['claimant_a']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Claimant B:</b> {fields['claimant_b']}", STY["DocBody"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph(f"<b>Status:</b> {fields['status']}", STY["DocHuge"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(
            "Both files are pending. No adjudication entered. Forward county and military paper as assembled.",
            STY["DocBody"],
        ))

    elif doc_id == "D002":
        body.append(Paragraph("WIDOW'S PENSION CLAIM — EXCERPT", STY["DocBig"]))
        body.append(Paragraph(f"Claimant: <b>{fields['claimant']}</b>", STY["DocBody"]))
        body.append(Paragraph(f"Maiden name: {fields['maiden_name']}", STY["DocBody"]))
        body.append(Paragraph(
            f"Marriage claimed: <b>{fields['marriage_date']}</b>, {fields['marriage_place']}",
            STY["DocBody"],
        ))
        body.append(Paragraph(
            f"Asserted soldier death: {fields['asserted_soldier_death']}",
            STY["DocBody"],
        ))
        kids = ", ".join(fields["children_named"])
        body.append(Paragraph(f"Children named: {kids}", STY["DocBody"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(
            "Claimant states she married the soldier before his enlistment and received word that he died of disease in hospital during the war. She asks for widow's pension on that marriage and that death.",
            STY["DocBody"],
        ))

    elif doc_id == "D003":
        body.append(Paragraph("WIDOW'S PENSION CLAIM — EXCERPT", STY["DocBig"]))
        body.append(Paragraph(f"Claimant: <b>{fields['claimant']}</b>", STY["DocBody"]))
        body.append(Paragraph(f"Maiden name: {fields['maiden_name']}", STY["DocBody"]))
        body.append(Paragraph(
            f"Marriage claimed: <b>{fields['marriage_date']}</b>, {fields['marriage_place']}",
            STY["DocBody"],
        ))
        body.append(Paragraph(
            f"Asserted soldier death: {fields['asserted_soldier_death']}",
            STY["DocBody"],
        ))
        kids = ", ".join(fields["children_named"])
        body.append(Paragraph(f"Children named: {kids}", STY["DocBody"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph(
            f"Claimant's stated belief: {fields['belief']}",
            STY["DocBody"],
        ))
        body.append(Spacer(1, 6))
        body.append(Paragraph(
            "Claimant asks for widow's pension on the 1866 marriage and the 1887 death, naming herself as his widow.",
            STY["DocBody"],
        ))

    elif doc_id == "D004":
        body.append(Paragraph("JEFFERSON COUNTY — DEATH REGISTER", STY["DocBig"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph(f"<b>Decedent:</b> {fields['decedent']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date of death:</b> {fields['death_date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Cause:</b> {fields['cause']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Place:</b> {fields['place']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Physician:</b> {fields['physician']}", STY["DocBody"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph("<b>Widow / informant wife:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["widow_or_informant_wife"], STY["DocHuge"]))

    elif doc_id == "D005":
        body.append(Paragraph("RIPLEY COUNTY MARRIAGE REGISTER", STY["DocBig"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Groom:</b> {fields['groom']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Bride:</b> {fields['bride']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date:</b> {fields['date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>County:</b> {fields['county']}", STY["DocBody"]))

    elif doc_id == "D006":
        body.append(Paragraph("JEFFERSON COUNTY MARRIAGE REGISTER", STY["DocBig"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Groom:</b> {fields['groom']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Groom status (as recorded):</b> {fields['groom_status']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Bride:</b> {fields['bride']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date:</b> {fields['date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Officiant:</b> {fields['officiant']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>County:</b> {fields['county']}", STY["DocBody"]))

    elif doc_id == "D007":
        body.append(Paragraph("U.S. GENERAL HOSPITAL — REGISTER LINE", STY["DocBig"]))
        body.append(Paragraph(doc["place"], STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Name:</b> {fields['name']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Unit:</b> {fields['unit']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Admitted:</b> {fields['admitted']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date:</b> {fields['date']}", STY["DocBody"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph("<b>Status:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["status"], STY["DocHuge"]))

    elif doc_id == "D008":
        body.append(Paragraph("COMPANY MUSTER / DESCRIPTIVE ROLL", STY["DocBig"]))
        body.append(Paragraph(fields["unit"], STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Name:</b> {fields['name']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Unit:</b> {fields['unit']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Approx. date:</b> {fields['approx_date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Context:</b> {fields['context']}", STY["DocBody"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph("<b>Status:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["status"], STY["DocHuge"]))

    elif doc_id == "D009":
        body.append(Paragraph("1860 FEDERAL CENSUS — SCHEDULE EXTRACT", STY["DocBig"]))
        body.append(Paragraph(f"{doc['place']} — {doc['date']}", STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.extend(household_table(fields["household"]))

    elif doc_id == "D010":
        # HARD risk #3: NO tip/bold/callout of Corbit, Wife, etc.
        body.append(Paragraph("1870 FEDERAL CENSUS — SCHEDULE EXTRACT", STY["DocBig"]))
        body.append(Paragraph(f"{doc['place']} — {doc['date']}", STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.extend(household_table(fields["household"]))

    elif doc_id == "D011":
        # HARD risk #3: NO tip on Eli / age-off / Wife
        body.append(Paragraph("1880 FEDERAL CENSUS — SCHEDULE EXTRACT", STY["DocBig"]))
        body.append(Paragraph(f"{doc['place']} — {doc['date']}", STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.extend(household_table(fields["household"]))

    elif doc_id == "D012":
        body.append(Paragraph("FEDERAL CENSUS — MARTHA CORBETT HOUSEHOLD", STY["DocBig"]))
        body.append(Paragraph("Ripley County, Indiana", STY["BodyCenter"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph("<b>1870 schedule</b>", STY["H2"]))
        body.extend(household_table(fields["1870"]))
        body.append(Spacer(1, 10))
        body.append(Paragraph("<b>1880 schedule</b>", STY["H2"]))
        body.extend(household_table(fields["1880"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(
            f"Remarriage noted on these schedules: {fields['remarriage']}",
            STY["DocBody"],
        ))

    elif doc_id == "D013":
        body.append(Paragraph("BURIAL / DEATH CERTIFICATE EXTRACT", STY["DocBig"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Decedent:</b> {fields['decedent']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Burial date:</b> {fields['burial_date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Cause:</b> {fields['cause']}", STY["DocBody"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph("<b>Widow:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["widow"], STY["DocHuge"]))

    elif doc_id == "D014":
        body.append(Paragraph("COURT / COUNTY SEARCH RESULT", STY["DocBig"]))
        body.append(Paragraph("Divorce / Dissolution Search", STY["BodyCenter"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Parties searched:</b> {fields['parties_searched']}", STY["DocBody"]))
        body.append(Paragraph(
            f"<b>Counties:</b> {', '.join(fields['counties'])}",
            STY["DocBody"],
        ))
        body.append(Paragraph(f"<b>Years searched:</b> {fields['years_searched']}", STY["DocBody"]))
        body.append(Spacer(1, 10))
        body.append(Paragraph("<b>RESULT:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["result"], STY["DocHuge"]))

    elif doc_id == "D015":
        # HARD risk #2: eliminators ON-FACE — Co. B, 83rd Indiana, Dearborn, age ~23
        body.append(Paragraph("HOSPITAL REGISTER LINE — NASHVILLE", STY["DocBig"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Name:</b> {fields['name']}", STY["DocBody"]))
        body.append(Spacer(1, 4))
        body.append(Paragraph("<b>Unit:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["unit"], STY["DocHuge"]))  # Co. B, 83rd Indiana
        body.append(Paragraph("<b>Residence:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["residence"], STY["DocHuge"]))  # Dearborn County
        body.append(Paragraph("<b>Age (approx.):</b>", STY["DocBody"]))
        body.append(Paragraph(str(fields["age_approx"]), STY["DocHuge"]))
        body.append(Spacer(1, 4))
        body.append(Paragraph(f"<b>Status:</b> {fields['status']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date:</b> {fields['date']}", STY["DocBody"]))

    elif doc_id == "D016":
        # HARD risk #1: Corbin/Ashley vs Corbett/Ashby LARGE and CLEAR
        body.append(Paragraph("RIPLEY COUNTY — DIVORCE DECREE EXTRACT", STY["DocBig"]))
        body.append(Spacer(1, 10))
        body.append(Paragraph("<b>Husband:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["husband"], STY["DocHuge"]))  # Eli Corbin
        body.append(Paragraph("<b>Wife:</b>", STY["DocBody"]))
        body.append(Paragraph(fields["wife"], STY["DocHuge"]))  # Martha Ann Ashley
        body.append(Spacer(1, 6))
        body.append(Paragraph(f"<b>Decree date:</b> {fields['decree_date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>County:</b> {fields['county']}", STY["DocBody"]))
        body.append(Spacer(1, 10))
        body.append(Paragraph(
            "Names as recorded on the decree. Compare letter-by-letter to any other couple under study.",
            STY["Small"],
        ))

    elif doc_id == "D017":
        # HARD risk #7: clearly neighboring / example — NOT Claimant C
        body.append(Paragraph(
            "NEIGHBORING / EXAMPLE FILE — NOT A CLAIMANT ON ELIAS M. CORBETT'S PENSION",
            STY["Warn"],
        ))
        body.append(Paragraph("PENSION NOTE — REMARRIAGE RULE", STY["DocBig"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph(
            "This paper is from a neighboring Jefferson County widow's file. "
            "It is supplied only to illustrate how remarriage can affect widow-pension eligibility. "
            "It is <b>not</b> Claimant C on Elias M. Corbett's contested file.",
            STY["DocBody"],
        ))
        body.append(Spacer(1, 8))
        body.append(Paragraph(f"<b>Widow:</b> {fields['widow']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>First husband:</b> {fields['first_husband']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Remarriage:</b> {fields['remarriage']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Effect noted:</b> {fields['effect']}", STY["DocBody"]))

    elif doc_id == "D018":
        body.append(Paragraph("AFFIDAVIT", STY["DocBig"]))
        body.append(Spacer(1, 6))
        body.append(Paragraph(f"<b>Affiant:</b> {fields['affiant']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Date:</b> {doc['date']}", STY["DocBody"]))
        body.append(Paragraph(f"<b>Place:</b> {doc['place']}", STY["DocBody"]))
        body.append(Spacer(1, 8))
        body.append(Paragraph("Affiant states under oath:", STY["DocBody"]))
        for item in fields["confirms"]:
            body.append(Paragraph(f"• {item}", STY["BulletBody"]))

    else:
        body.extend(render_fields_generic(doc))

    flows.extend(body)
    flows.append(Spacer(1, 12))
    flows.append(footer_facsimile())
    return flows


def exhibit_page(doc_id: str, width=6.8 * inch):
    content = build_exhibit_content(doc_id)
    return AgedBox(content, width=width, pad=14, min_height=2.5 * inch)


# ---------------------------------------------------------------------------
# Research catalog (CRITICAL risk #6 — unlocks from opening cues)
# ---------------------------------------------------------------------------
CATALOG_ROWS = [
    ("D005", "1858 Ripley County marriage register",
     "From D002: marriage date 1858-03-12 + Ripley County → pull Corbett/Ashby register for that date/county."),
    ("D006", "1866 Jefferson County marriage register",
     "From D003: marriage date 1866-06-04 + Jefferson County → pull Corbett/Briggs register (groom status as recorded)."),
    ("D007", "Hospital register line — Nashville",
     "From D001: soldier Co. C, 36th Indiana Infantry → pull hospital/convalescent lines for that unit."),
    ("D008", "Company muster / descriptive roll",
     "From D001: same unit Co. C, 36th Indiana → pull company muster fate line for the named soldier."),
    ("D009", "1860 Federal Census — Ripley household",
     "From D002: Ripley + Elias/Martha + child Sarah → pre-war household schedule."),
    ("D010", "1870 Federal Census — Jefferson household",
     "From D003/D004: Jefferson County + Lydia household after the 1866 marriage date."),
    ("D011", "1880 Federal Census — Jefferson household",
     "From D003: Jefferson + Lydia + children named on her claim → later schedule."),
    ("D012", "1870/1880 Census — Martha household, Ripley",
     "From D002: Ripley + Martha Corbett + children Sarah & James → postwar widow-head schedules."),
    ("D013", "1887 burial / death certificate extract",
     "From D004: death 1887-02-14 Jefferson → burial/death naming follow-up."),
    ("D014", "Divorce-search negative — named parties",
     "From D005 parties (Elias M. Corbett & Martha Jane Ashby) + counties already on D002/D003 (Ripley, Jefferson), years 1858–1887."),
    ("D015", "Hospital register line — Nashville (additional)",
     "From D007 hospital context: scan nearby Corbett/Corbit hospital deaths in Nashville registers; compare unit/age/residence."),
    ("D016", "Divorce decree extract — Ripley County",
     "Side result when searching divorces near D005 parties in Ripley — compare every letter of both surnames."),
    ("D017", "Neighboring remarriage pension note (example)",
     "Optional teaching file from Jefferson County widow-pension practice — labeled neighboring/example; NOT a third claimant on this soldier."),
]


def add_page_number(canv, doc):
    canv.saveState()
    canv.setFont("Times-Roman", 8)
    canv.setFillColor(MUTED)
    canv.drawCentredString(PAGE[0] / 2, 0.4 * inch, f"— {doc.page} —")
    canv.restoreState()


def add_sealed_page_number(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica-Bold", 8)
    canv.setFillColor(SEALED_RED)
    canv.drawCentredString(PAGE[0] / 2, 0.55 * inch, "SEALED — DO NOT OPEN UNTIL SUBMITTED")
    canv.setFont("Times-Roman", 8)
    canv.setFillColor(MUTED)
    canv.drawCentredString(PAGE[0] / 2, 0.35 * inch, f"— {doc.page} —")
    canv.restoreState()


# ---------------------------------------------------------------------------
# PLAYER PDF
# ---------------------------------------------------------------------------
def build_player_pdf(path: Path):
    doc = SimpleDocTemplate(
        str(path), pagesize=PAGE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=0.65 * inch,
        title="The Wrong Widow — Player Case",
        author="Genealogy Mystery Series",
    )
    story = []
    W = 6.8 * inch

    # Cover
    story.append(Spacer(1, 1.2 * inch))
    story.append(Paragraph("THE WRONG WIDOW", STY["CoverTitle"]))
    story.append(Paragraph("A printable historical family mystery", STY["CoverSub"]))
    story.append(Spacer(1, 0.3 * inch))
    story.append(HRFlowable(width="60%", thickness=1, color=AGED_BORDER, spaceBefore=4, spaceAfter=12))
    frame = PLAYER_START["player_frame"]
    story.append(Paragraph(f"<b>Player frame:</b> {frame['years']}", STY["BodyCenter"]))
    story.append(Paragraph(frame["role"], STY["BodyCenter"]))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph(frame["objective_player_facing"], STY["Body"]))
    story.append(Spacer(1, 0.4 * inch))
    story.append(Paragraph(
        "This is the <b>player case</b>. Keep <b>hints.pdf</b> and <b>sealed-solution.pdf</b> closed until you need them.",
        STY["Warn"],
    ))
    story.append(Spacer(1, 0.5 * inch))
    story.append(Paragraph("Solo or small group · One evening · US Letter", STY["Small"]))
    story.append(PageBreak())

    # How to investigate (short — after stakes will appear in cold open; keep brief)
    story.append(Paragraph("How to investigate", STY["H1"]))
    story.append(Paragraph(
        "Work in short loops: <b>observe</b> what a document asserts → form a <b>hypothesis</b> → "
        "<b>pull</b> the next record from the research catalog → <b>compare</b> witnesses → <b>revise</b>. "
        "Records disagree the way witnesses disagree. No single page is gospel.",
        STY["Body"],
    ))
    story.append(Paragraph(
        "Use the worksheets. Cite exhibit codes (D001, D002, …) when you answer. "
        "When you are ready, answer the final adjudication questions — then open the sealed solution only after you commit.",
        STY["Body"],
    ))
    story.append(Paragraph(
        "<b>Spoiler warning:</b> Do not open sealed-solution.pdf until you have submitted (or firmly written) your answers. "
        "hints.pdf is progressive; open one rung at a time if stuck.",
        STY["Small"],
    ))
    story.append(PageBreak())

    # Cold open
    story.append(Paragraph("Cold open — the dispute", STY["H1"]))
    story.append(Paragraph(
        "Two women have filed Civil War widow's pension claims for the same enlisted man. "
        "The bureau papers are already in conflict. You are walking into an open dispute.",
        STY["Body"],
    ))
    story.append(Paragraph(
        "Read exhibits <b>D001 → D002 → D003 → D004</b> in that order. Then verify both marriages.",
        STY["Body"],
    ))
    story.append(Spacer(1, 8))

    for oid in ["D001", "D002", "D003", "D004"]:
        story.append(exhibit_page(oid, W))
        story.append(Spacer(1, 14))
        story.append(PageBreak())

    # First research ask
    story.append(Paragraph("First research ask", STY["H1"]))
    story.append(Paragraph(PLAYER_START["first_research_ask"], STY["Body"]))
    story.append(Paragraph(
        "Use the research catalog below. Each cue unlocks from dates, places, and names already on D001–D004 "
        "(and from records you unlock next). You do not need hidden knowledge to find the next pull.",
        STY["Body"],
    ))
    story.append(PageBreak())

    # Research catalog
    story.append(Paragraph("Research catalog", STY["H1"]))
    story.append(Paragraph(
        "Index of research exhibits D005–D017. Unlock cues are written from opening paper — not from author-only knowledge.",
        STY["Body"],
    ))
    story.append(Spacer(1, 6))

    cat_data = [[
        Paragraph("<b>Code</b>", STY["Small"]),
        Paragraph("<b>Record</b>", STY["Small"]),
        Paragraph("<b>How you find it (cue from paper you already have)</b>", STY["Small"]),
    ]]
    for code, title, cue in CATALOG_ROWS:
        cat_data.append([
            Paragraph(f"<b>{code}</b>", STY["CatalogCue"]),
            Paragraph(title, STY["CatalogCue"]),
            Paragraph(cue, STY["CatalogCue"]),
        ])
    cat = Table(cat_data, colWidths=[0.6 * inch, 2.0 * inch, 4.2 * inch])
    cat.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), HEADER_BG),
        ("BACKGROUND", (0, 1), (-1, -1), CATALOG_BG),
        ("GRID", (0, 0), (-1, -1), 0.4, AGED_BORDER),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(cat)
    story.append(Spacer(1, 10))
    story.append(Paragraph(
        "<b>Note on D017:</b> Neighboring/example remarriage file only — not a claimant on Elias M. Corbett's contested pension.",
        STY["Small"],
    ))
    story.append(PageBreak())

    # Research exhibits D005–D017
    story.append(Paragraph("Research exhibits", STY["H1"]))
    story.append(Paragraph(
        "Pull these as your investigation requires. Exhibit codes match the catalog.",
        STY["Body"],
    ))
    story.append(PageBreak())

    for oid in [f"D{str(i).zfill(3)}" for i in range(5, 18)]:
        story.append(exhibit_page(oid, W))
        story.append(Spacer(1, 10))
        story.append(PageBreak())

    # Worksheets
    story.append(Paragraph("Worksheets", STY["H1"]))
    story.append(Paragraph(
        "Write freely. Cite exhibit codes. Do not treat these sheets as answer keys.",
        STY["Body"],
    ))

    story.append(Paragraph("1. Claim comparison", STY["H2"]))
    story.append(Paragraph(
        "What does each claimant assert? (marriage date/place, death claim, children, what would make her file look strong)",
        STY["WorksheetQ"],
    ))
    story.append(Paragraph("<b>Martha Jane Corbett (from her file):</b>", STY["DocBody"]))
    write_lines_space(story, 4, 18)
    story.append(Paragraph("<b>Lydia Ann Corbett (from her file):</b>", STY["DocBody"]))
    write_lines_space(story, 4, 18)
    story.append(PageBreak())

    story.append(Paragraph("2. War paper conflict", STY["H2"]))
    story.append(Paragraph(
        "Hospital line vs company muster — how does each describe the soldier's fate? If they disagree, note the disagreement.",
        STY["WorksheetQ"],
    ))
    story.append(Paragraph("<b>Hospital / convalescent line:</b>", STY["DocBody"]))
    write_lines_space(story, 3, 18)
    story.append(Paragraph("<b>Company muster:</b>", STY["DocBody"]))
    write_lines_space(story, 3, 18)
    story.append(Paragraph("<b>Conflict / working theory:</b>", STY["DocBody"]))
    write_lines_space(story, 3, 18)
    story.append(PageBreak())

    story.append(Paragraph("3. Household reconstruction", STY["H2"]))
    story.append(Paragraph(
        "Sketch who lives where, and when. First household vs second household. Note remarriage (or none) as the schedules show it.",
        STY["WorksheetQ"],
    ))
    story.append(Paragraph("<b>Ripley / first household:</b>", STY["DocBody"]))
    write_lines_space(story, 5, 18)
    story.append(Paragraph("<b>Jefferson / second household:</b>", STY["DocBody"]))
    write_lines_space(story, 5, 18)
    story.append(PageBreak())

    # Final questions A–D (blank)
    story.append(Paragraph("Final adjudication", STY["H1"]))
    story.append(Paragraph(
        "Answer from the open record set (D001–D017). Cite exhibits. Keep the sealed packet closed until you commit.",
        STY["Body"],
    ))

    questions = [
        ("A. Supportable widow",
         "Which claimant's marriage is the undissolved prior union that controls widow status? Name her and cite the paper that supports your choice."),
        ("B. Claimant beliefs",
         "What did each woman believe or assert in her file? (Sincere vs knowingly false is a separate layer — stay with what the open paper shows.)"),
        ("C. What happened",
         "Reconstruct the soldier's wartime fate from the conflicting military paper and his postwar life. When did he die?"),
        ("D. Why both claims look real",
         "Which documents legitimately support each file? Keep “record says X” separate from “X happened.”"),
    ]
    for title, prompt in questions:
        story.append(Paragraph(title, STY["H2"]))
        story.append(Paragraph(prompt, STY["WorksheetQ"]))
        story.append(Paragraph("<b>Your answer:</b>", STY["DocBody"]))
        write_lines_space(story, 5, 18)
        story.append(Paragraph("<b>Exhibit citations:</b>", STY["DocBody"]))
        write_lines_space(story, 2, 18)

    story.append(Spacer(1, 16))
    story.append(HRFlowable(width="100%", thickness=1, color=AGED_BORDER))
    story.append(Paragraph(
        "When finished: seal your answers, then open sealed-solution.pdf. Use hints.pdf only if stuck (one rung at a time).",
        STY["BodyCenter"],
    ))

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return path


# ---------------------------------------------------------------------------
# HINTS PDF
# ---------------------------------------------------------------------------
def build_hints_pdf(path: Path):
    doc = SimpleDocTemplate(
        str(path), pagesize=PAGE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=0.65 * inch,
        title="The Wrong Widow — Hints",
        author="Genealogy Mystery Series",
    )
    story = []
    story.append(Paragraph("THE WRONG WIDOW", STY["CoverTitle"]))
    story.append(Paragraph("Progressive hints (separate packet)", STY["CoverSub"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "Open one rung at a time when stuck. Hints teach method — they do not name the supportable widow.",
        STY["Body"],
    ))
    story.append(Paragraph(
        "Keep sealed-solution.pdf closed. These hints never include the sealed exhibit.",
        STY["Warn"],
    ))
    story.append(HRFlowable(width="100%", thickness=1, color=AGED_BORDER, spaceBefore=8, spaceAfter=12))

    for rung in HINTS["rungs"]:
        story.append(Paragraph(f"{rung['rung']} — when stuck: {rung['when_stuck']}", STY["HintRung"]))
        story.append(Paragraph(rung["hint"], STY["Body"]))
        story.append(Paragraph(f"<i>Teaches:</i> {rung['teaches']}", STY["Small"]))
        story.append(Spacer(1, 4))
        story.append(HRFlowable(width="100%", thickness=0.3, color=LIGHT_RULE, spaceBefore=2, spaceAfter=2))

    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "Still stuck after H8? Commit your best adjudication from the three-question frame, then open the sealed solution.",
        STY["Body"],
    ))

    doc.build(story, onFirstPage=add_page_number, onLaterPages=add_page_number)
    return path


# ---------------------------------------------------------------------------
# SEALED SOLUTION PDF
# ---------------------------------------------------------------------------
def build_sealed_pdf(path: Path):
    doc = SimpleDocTemplate(
        str(path), pagesize=PAGE,
        leftMargin=MARGIN, rightMargin=MARGIN,
        topMargin=MARGIN, bottomMargin=0.75 * inch,
        title="The Wrong Widow — SEALED Solution",
        author="Genealogy Mystery Series",
    )
    story = []
    W = 6.8 * inch

    story.append(Paragraph("★★★ SEALED ★★★", STY["SealedBanner"]))
    story.append(Paragraph("DO NOT OPEN UNTIL YOU HAVE SUBMITTED YOUR ANSWERS", STY["SealedBanner"]))
    story.append(Paragraph("THE WRONG WIDOW — Solution packet", STY["CoverTitle"]))
    story.append(Spacer(1, 8))
    story.append(Paragraph(
        "This packet contains the answer key and sealed exhibit D018. "
        "Keep it physically separate from the player case (own envelope / own print job / duplex break).",
        STY["Body"],
    ))
    story.append(PageBreak())

    story.append(Paragraph("★★★ SEALED — ANSWER KEY ★★★", STY["SealedBanner"]))
    story.append(Paragraph(
        "Solved when A–D are supported from the <b>open</b> record set (D001–D017). "
        "D018 confirms motive/knowledge color only — it is not required to solve and is not the sole legal hinge.",
        STY["Body"],
    ))
    story.append(Spacer(1, 6))

    # Distinguish layers
    story.append(Paragraph("Two layers (do not collapse them)", STY["H2"]))
    story.append(Paragraph(
        "<b>Recorded observation:</b> what a document asserts (hospital “dead,” death register naming Lydia, 1866 “widower”).",
        STY["Body"],
    ))
    story.append(Paragraph(
        "<b>Canonical truth:</b> what happened (desertion; Martha’s marriage never dissolved; Lydia was lied to).",
        STY["Body"],
    ))
    story.append(PageBreak())

    for el in RUBRIC["elements"]:
        story.append(Paragraph(f"Element {el['element']}: {el['name']}", STY["H2"]))
        story.append(Paragraph(f"<i>Player must establish:</i> {el['player_must_establish']}", STY["Small"]))
        correct = el["correct"]
        if el["element"] == "A":
            story.append(Paragraph(
                f"<b>Answer:</b> {correct['name']} (person {correct['person_id']})",
                STY["DocBody"],
            ))
            story.append(Paragraph(f"<b>Basis:</b> {correct['basis']}", STY["DocBody"]))
        elif el["element"] == "B":
            story.append(Paragraph(f"<b>Martha:</b> {correct['Martha']}", STY["DocBody"]))
            story.append(Paragraph(f"<b>Lydia:</b> {correct['Lydia']}", STY["DocBody"]))
        elif el["element"] == "C":
            story.append(Paragraph(f"<b>Wartime:</b> {correct['wartime']}", STY["DocBody"]))
            story.append(Paragraph(f"<b>Postwar:</b> {correct['postwar']}", STY["DocBody"]))
            story.append(Paragraph(f"<b>Canonical death:</b> {correct['canonical_death_only']} only", STY["DocBody"]))
        elif el["element"] == "D":
            story.append(Paragraph(
                "<b>Martha file supports:</b> " + "; ".join(correct["Martha_file_supports"]),
                STY["DocBody"],
            ))
            story.append(Paragraph(
                "<b>Lydia file supports:</b> " + "; ".join(correct["Lydia_file_supports"]),
                STY["DocBody"],
            ))
            story.append(Paragraph(f"<b>Teaching:</b> {correct['teaching']}", STY["DocBody"]))

        cites = el.get("required_citations_min", [])
        story.append(Paragraph(
            "<b>Minimum exhibit citations:</b> " + ", ".join(cites),
            STY["DocBody"],
        ))
        if el.get("helpful"):
            story.append(Paragraph(
                "<b>Also helpful:</b> " + ", ".join(el["helpful"]),
                STY["Small"],
            ))
        story.append(Spacer(1, 8))

    story.append(PageBreak())
    story.append(Paragraph("Fail / incomplete if", STY["H2"]))
    for fail in RUBRIC["fail_incomplete_if"]:
        story.append(Paragraph(f"• {fail}", STY["BulletBody"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Explicitly not required", STY["H2"]))
    for item in RUBRIC["explicitly_not_required"]:
        story.append(Paragraph(f"• {item}", STY["BulletBody"]))

    story.append(Spacer(1, 10))
    story.append(Paragraph("Proveable from open set (summary)", STY["H2"]))
    for prv in EVIDENCE["proveable_from_open_set"]:
        docs = ", ".join(prv.get("documents", prv.get("depends_on", [])))
        story.append(Paragraph(
            f"<b>{prv['id']}:</b> {prv['claim']} <i>({docs})</i>",
            STY["Small"],
        ))

    story.append(PageBreak())
    story.append(Paragraph("★★★ SEALED EXHIBIT D018 ★★★", STY["SealedBanner"]))
    story.append(Paragraph(
        "Confirmation only. Players who already adjudicated correctly should feel confirmation — not a new legal theory. "
        "Open-set proof already covers desertion trail (D008), postwar overlap (D010/D011), and no divorce (D014).",
        STY["Body"],
    ))
    story.append(Spacer(1, 10))
    story.append(exhibit_page("D018", W))
    story.append(Spacer(1, 16))
    story.append(Paragraph(
        "End of sealed packet. This case resolves fully. Series appetite comes from craft and tone — not from withholding the answer.",
        STY["BodyCenter"],
    ))

    doc.build(story, onFirstPage=add_sealed_page_number, onLaterPages=add_sealed_page_number)
    return path


def page_count(path: Path) -> int:
    from pypdf import PdfReader
    return len(PdfReader(str(path)).pages)


def extract_text(path: Path) -> str:
    from pypdf import PdfReader
    r = PdfReader(str(path))
    return "\n".join((p.extract_text() or "") for p in r.pages)


def verify(player_path, hints_path, sealed_path):
    issues = []
    player_text = extract_text(player_path)
    hints_text = extract_text(hints_path)
    sealed_text = extract_text(sealed_path)

    # No D018 leak in player/hints
    for label, text in [("player", player_text), ("hints", hints_text)]:
        if re.search(r"\bD018\b", text):
            issues.append(f"{label}: contains D018")
        if "Benjamin F. Corbett" in text and "affidavit" in text.lower():
            issues.append(f"{label}: Benjamin F. Corbett affidavit content leak")
        if re.search(r"supportable widow is Martha", text, re.I):
            issues.append(f"{label}: spoiler prose 'supportable widow is Martha'")
        if re.search(r"Martha is the supportable", text, re.I):
            issues.append(f"{label}: spoiler prose Martha supportable")

    # D015 eliminators present in player
    for s in ["Co. B", "83rd Indiana", "Dearborn", "Silas M. Corbit"]:
        if s not in player_text:
            issues.append(f"player: missing D015 eliminator string '{s}'")

    # D016 surnames large/present
    for s in ["Eli Corbin", "Martha Ann Ashley", "Corbin", "Ashley"]:
        if s not in player_text:
            issues.append(f"player: missing D016 string '{s}'")

    # Sealed must have D018 and answer
    if "D018" not in sealed_text:
        issues.append("sealed: missing D018")
    if "Martha Jane (Ashby) Corbett" not in sealed_text:
        issues.append("sealed: missing Martha answer")
    if "Benjamin F. Corbett" not in sealed_text:
        issues.append("sealed: missing Benjamin affiant")

    # Player must have D001–D017
    for i in range(1, 18):
        code = f"D{str(i).zfill(3)}"
        if code not in player_text:
            issues.append(f"player: missing {code}")

    # Hints H1–H8
    for i in range(1, 9):
        if f"H{i}" not in hints_text:
            issues.append(f"hints: missing H{i}")

    # D017 neighboring label
    if "NOT A CLAIMANT ON ELIAS" not in player_text.upper() and "not a claimant" not in player_text.lower():
        # check softer
        if "Neighboring" not in player_text and "neighboring" not in player_text:
            issues.append("player: D017 neighboring label weak/missing")

    # Director polish: no trap-softening tell labels in player-facing text
    for pat, name in [
        (r"(?i)\bdecoy\b", "Decoy"),
        (r"(?i)false divorce", "False divorce"),
        (r"(?i)red[\s-]?herring", "red-herring"),
        (r"(?i)near[\s-]?name", "Near-name"),
    ]:
        if re.search(pat, player_text):
            issues.append(f"player: tell label present: {name}")

    return issues, player_text, hints_text, sealed_text


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    player = OUT / "player.pdf"
    hints = OUT / "hints.pdf"
    sealed = OUT / "sealed-solution.pdf"

    print("Building player.pdf …")
    build_player_pdf(player)
    print("Building hints.pdf …")
    build_hints_pdf(hints)
    print("Building sealed-solution.pdf …")
    build_sealed_pdf(sealed)

    pc = page_count(player)
    hc = page_count(hints)
    sc = page_count(sealed)
    print(f"Pages: player={pc}, hints={hc}, sealed={sc}")

    issues, _, _, _ = verify(player, hints, sealed)
    if issues:
        print("VERIFY ISSUES:")
        for i in issues:
            print(" -", i)
        raise SystemExit(1)
    print("VERIFY OK")

    # Write page counts sidecar for report
    meta = {
        "player_pages": pc,
        "hints_pages": hc,
        "sealed_pages": sc,
        "player_exhibits": [f"D{str(i).zfill(3)}" for i in range(1, 18)],
        "sealed_exhibits": ["D018"],
    }
    with open(OUT / "_build_meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)
    print("Wrote", OUT / "_build_meta.json")


if __name__ == "__main__":
    main()
