#!/usr/bin/env python3
"""Prüft das Repo. Exit-Code 1 = Fehler (nicht pushen).

python3 tools/check.py          Vorschau-Prüfung
python3 tools/check.py --launch zusätzlich Launch-Bedingungen (Impressum, Domain)
"""
import json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fehler, warn = [], []
site = json.load(open(os.path.join(ROOT, "data/site.json"), encoding="utf-8"))
links = json.load(open(os.path.join(ROOT, "data/links.json"), encoding="utf-8"))["links"]
pages = sorted(f for f in os.listdir(ROOT) if f.endswith(".html"))

for p in pages:
    t = open(os.path.join(ROOT, p), encoding="utf-8").read()
    # 1. Keine Fremd-Ressourcen (Datenschutz-Zusage)
    for m in re.findall(r'(?:src|href)="(https?://[^"]+)"', t):
        if 'rel="stylesheet"' in t and m in t.split('rel="stylesheet"')[0][-200:]:
            fehler.append(f"{p}: externes Stylesheet {m}")
    if re.search(r"<script[^>]+src=", t) or "fonts.googleapis" in t:
        fehler.append(f"{p}: externes Skript/Google Fonts")
    # 2. Interne Links existieren
    for m in re.findall(r'href="([a-z0-9\-]+\.html)', t):
        if m not in pages:
            fehler.append(f"{p}: toter Link {m}")
    # 3. Externe Links nur, wenn in links.json bestätigt oder ausdrücklich erlaubt
    ok = {l["url"] for l in links.values() if l.get("bestaetigt")} | {site["verein"]["website"]}
    for m in re.findall(r'href="(https?://[^"]+)"', t):
        if m not in ok and "openpetition" not in m:
            warn.append(f"{p}: ungeprüfter externer Link {m}")
    # 4. Keine Lorem/Platzhalter
    # Fehler 2026-11-15: re.I + "TODO" traf die CSS-Klasse class="todo" → nur Großschreibung prüfen
    if re.search(r"lorem ipsum|\[NAME\]|\[ADRESSE\]|\bTODO\b", t):
        fehler.append(f"{p}: Platzhaltertext")
    if 'name="robots" content="noindex' not in t and not (site["launch"] and site["domain_bestaetigt"]):
        fehler.append(f"{p}: Vorschau ohne noindex")

if "--launch" in sys.argv:
    b = site["betreiber"]
    for k in ("anschrift", "email", "telefon"):
        if not b[k]:
            fehler.append(f"Launch: betreiber.{k} in data/site.json fehlt (Impressumspflicht)")
    if not site["domain_bestaetigt"]:
        fehler.append("Launch: Domain noch nicht gekauft/bestätigt (domain_bestaetigt=false)")
    if not links["fw_programm"]["bestaetigt"]:
        warn.append("Launch: Link zum FW-Programm noch nicht im Browser bestätigt")

for w in warn:
    print("WARNUNG", w)
for f in fehler:
    print("FEHLER ", f)
print(f"{len(pages)} Seiten geprüft · {len(fehler)} Fehler · {len(warn)} Warnungen")
sys.exit(1 if fehler else 0)
