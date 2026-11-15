# FEHLER-LOG – Nordstern Frankfurt

Format: Symptom · Ursache · Fix · Lehre · Datum. Einmal gemachte Fehler hier festhalten.

## Übernommene Lehren aus anderen Repos (gelten hier von Anfang an)
- **Pages vom Hauptzweig = jeder Merge ist eine Veröffentlichung** (Frankfurt_FW) → `noindex`, `robots.txt Disallow` und Vorschau-Banner schon im ersten Commit; Launch nur über `data/site.json`.
- **Keine ungeprüfte URL ins Repo** (Frankfurt_FW) → `data/links.json` mit Datum `bestaetigt`; unbestätigte Links werden nur als Text gezeigt.
- **ffm.de blockt automatische Abrufe (HTTP 403)** → Links im Browser prüfen, nicht per Skript.
- **Tailwind-/Google-CDN überträgt Besucher-IP** (Frankfurt_FW, nachbarschaftshilfe-preungesheim M1) → nur lokale Schriften, kein CDN.
- **Branch-Schutz auf main lehnt Direkt-Push ab (GH013)** (copy-code-agency-website) → Arbeit auf `dev`, Merge per PR.
- **„IPAT-Studie Uni Augsburg“ war falsch** → richtig: IPot-Studie, Hochschule Kempten.
- **Ungenutztes Hosting-Paket lief weiter** (frankfurt-energie.online) → nur Domain buchen, Fristen notieren.

## 15.11.2026 – Aufbau
- **check.py meldete Platzhalter im Impressum** · Regex mit `re.I` traf die CSS-Klasse `class="todo"` · nur Großschreibung `\bTODO\b` prüfen · Lehre: Prüfmuster an echten Seiten testen, nicht nur ausdenken.
- **Hellmodus: dunkle Schrift auf Gold #8A6A10 ≈ 3,6:1** (WCAG verlangt 4,5:1) · Vorschau-Banner und aktiver Menüpunkt im Hellmodus auf Navy/Weiß · Lehre: beide Farbschemata per Screenshot prüfen.
- **Python-f-String mit Backslash im Ausdruck** (`\"page\"`) bricht vor Python 3.12 (Termux kann älter sein) · Wert vorher in Variable · Lehre: Skripte so schreiben, dass sie auch auf älterem Python laufen.
