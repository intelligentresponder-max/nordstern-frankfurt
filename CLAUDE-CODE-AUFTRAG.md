# Auftrag an Claude Code – Nordstern Frankfurt, Phase 2 (visuelles Redesign)

Lies zuerst: `CLAUDE.md`, `docs/UX-KONZEPT.md`, `docs/ENTSCHEIDUNGEN.md`, `FEHLER-LOG.md`.
Repo: `nordstern-ffm/nordstern-frankfurt` · Umgebung: Windows, Git Bash (Pfade mit Leerzeichen: `"$HOME/..."`, nie `~` in Anleitungen für den Nutzer – Einfügen verliert `~` und `@`).

## Arbeitsregeln
1. Arbeite auf Branch `ux-phase2`, nie direkt auf `main`. Jede Aufgabe = ein Commit mit klarer Nachricht.
2. Nach jeder Aufgabe: `python tools/build.py && python tools/check.py` → 0 Fehler, sonst nicht committen.
3. Inhalte nur in `data/*.json`; HTML wird erzeugt. Keine Frameworks, kein npm, kein CDN, kein externes JS.
4. **Keine Fakten erfinden.** Jede Zahl, jede Rechtsaussage, jeder Link mit Primärquelle und Datum; was nicht belegt ist, kommt nicht auf die Seite, sondern in `docs/OFFEN.md`.
5. **Keine Bilder ohne vollständigen Eintrag in `data/bilder.json`** (siehe UX-KONZEPT Abschnitt 4). Im Zweifel eigenes SVG statt fremdes Foto.
6. Jeder Fehler → `FEHLER-LOG.md` (Symptom · Ursache · Fix · Lehre). Jede Richtungsentscheidung mit Alternativen → `docs/ENTSCHEIDUNGEN.md`.
7. Sparsam: Routine (Texte, JSON, CSS) mit dem günstigsten Modell; Planung, Recht/Datenschutz und Abschluss-Review mit dem stärksten.
8. Vor dem Push dem Nutzer die Befehle einzeln zum Kopieren geben und auf seine Ausgabe warten.

## Aufgaben (in dieser Reihenfolge)
| # | Aufgabe | Fertig, wenn |
| --- | --- | --- |
| 1 | `data/bilder.json` anlegen + `check.py` erweitern: jedes `<img src>` und jede Bilddatei unter `img/` braucht Eintrag mit allen Pflichtfeldern; `build.py` erzeugt `bildnachweise.html` und Bildunterschriften mit Nachweis | check schlägt bei fehlendem Eintrag fehl (mit Testfall belegt) |
| 2 | Icon-System: Lucide oder Tabler lokal als `assets/icons.svg` (nur benötigte Symbole), Lizenzdatei `assets/LICENSE-icons.txt`, Hilfsfunktion `icon(name)` in build.py | alle Karten/Navi mit Icon, `aria-hidden` bei Deko-Icons |
| 3 | `data/zahlen.json` + Kennzahl-Kacheln (Start, Nachbarschaft). Nur belegte Zahlen (z. B. Einwohner Preungesheim lt. Stadt Frankfurt Statistik, Entlastungsbetrag lt. SGB XI) | jede Kachel zeigt Quelle + Stand |
| 4 | Ablauf-Diagramme (Nachbarschaft, Melden) und Zeitleiste (Start) als wiederverwendbare Bausteine `steps()` / `timeline()` | auf 390 px lesbar, Screenreader-Reihenfolge stimmt |
| 5 | Schaubild „Wer entscheidet in Frankfurt?“ als Inline-SVG + Text-Alternative | Fakten mit Quelle (Hessische Gemeindeordnung, frankfurt.de) |
| 6 | Schema-Karte Ortsbezirk 10 (eigenes vereinfachtes SVG, OSM-Hinweis) | Stadtteilnamen nur laut Stadt Frankfurt; ODbL-Hinweis sichtbar |
| 7 | Hero-Illustrationen je Seite (eigene SVG im Nordstern-Stil) | kein fremdes Material oder vollständig nachgewiesen |
| 8 | 3–6 Fotos von Wikimedia Commons (Frankfurter Norden/Frankfurt), WebP ≤ 150 KB, Lizenz am Original geprüft | Nachweis unter Bild + auf `bildnachweise.html` |
| 9 | Vermittlung: Filter-Chips ohne JS (Sprungmarken), Dienst-Karten mit Icon | nur `aktiv: true`-Dienste sichtbar |
| 10 | Abnahme: Screenshots aller Seiten (390/1280, hell/dunkel), Kontrast-Check, Lighthouse-Werte laut UX-KONZEPT Abschnitt 5, Ergebnis in `docs/ABNAHME-PHASE2.md` | alle Kriterien erfüllt oder Abweichung begründet |

## Nicht in Phase 2
BanglaHilfe- und wege-nach-frankfurt-Neubau (Phase 3, eigener Auftrag), Zahlungslinks live schalten, Domain, Impressum-Daten (kommen vom Nutzer).

## Übergabe an den Nutzer (Git Bash), am Ende
```bash
cd "$HOME/nordstern-frankfurt"
git push -u origin ux-phase2
```
Dann Pull Request auf GitHub `ux-phase2 → main`, Nutzer prüft die Vorschau und mergt.
