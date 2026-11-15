# UX-Konzept Nordstern Frankfurt – multifunktionale Infoseite

Ziel: Jede Seite erklärt sich in 5 Sekunden über Bilder, Zahlen und Symbole – Text vertieft nur.
Zielgruppen (Reihenfolge = Priorität): 1. Ältere Menschen und Angehörige im Frankfurter Norden · 2. Helfende/Fachkraft · 3. Bürger mit Anliegen · 4. Betriebe/Vereine (Kunden der Agentur) · 5. Menschen mit Bangla-, Tigrinya-, Thai-, Lao-Hintergrund.

## 1 · Prinzipien
1. **Ein Hauptziel je Seite** (eine Primär-Schaltfläche, Gold). Alles andere ist sekundär.
2. **Bild vor Text:** Jeder Abschnitt beginnt mit einem visuellen Anker (Icon, Zahl, Karte, Diagramm, Illustration).
3. **Barrierefrei zuerst:** WCAG 2.1 AA, 18 px Grundschrift, Touch-Ziele ≥ 44 px, jedes Bild mit Alt-Text, Diagramme zusätzlich als Tabelle.
4. **Schnell auf alten Android-Geräten:** keine Bibliotheken, keine Fremdabrufe, Bilder WebP/AVIF ≤ 150 KB, `loading="lazy"`.
5. **Ehrlich:** Geplantes ist als geplant markiert, jede Zahl hat Quelle + Stand.

## 2 · Visuelle Bausteine (nicht nur Fotos)
| Baustein | Wofür | Technik | Herkunft / Lizenz |
| --- | --- | --- | --- |
| **Icon-System** | Navigation, Dienste, Kategorien | Inline-SVG, eine Datei `assets/icons.svg` mit `<symbol>` | Lucide (ISC) oder Tabler Icons (MIT), lokal kopiert, Lizenzdatei ins Repo |
| **Kennzahl-Kacheln** | „15.770 Einwohner“, „131 € Entlastungsbetrag“ | HTML + CSS, Zahl groß, Quelle klein darunter | Zahlen nur aus Primärquelle (Stadt Frankfurt, Gesetz), in `data/zahlen.json` mit Quelle und Datum |
| **Schema-Karte Ortsbezirk 10** | „Wo sind wir?“, Stadtteile im Norden | Selbst gezeichnetes SVG (vereinfachte Umrisse), keine Kachel-Karte | Grundlage OpenStreetMap-Daten (ODbL) → Pflichthinweis „© OpenStreetMap-Mitwirkende“ mit Link |
| **Ablauf-Diagramme** | „So funktioniert Nachbarschaftshilfe“, „Vom Mangel zur Petition“ | Nummerierte Schritte mit Icons, CSS-Grid | eigen |
| **Fortschrittsbalken** | Petitionen (x von 220) | vorhanden (`.meter`) + Text-Alternative | eigen |
| **Zeitleiste** | Vereinsgründung, Wahl, Projekte | `<ol>` mit Linie und Punkten | eigen |
| **Balken-/Ringdiagramme** | Altersstruktur, Bedarf | Inline-SVG, aus JSON erzeugt im Build | Daten mit Quelle; Diagramm zusätzlich als `<table>` |
| **Illustrationen** | Hero je Seite, Leerzustände | SVG-Illustrationen im Nordstern-Stil (Navy/Gold) | eigene Zeichnung oder unDraw (eigene Lizenz – vor Nutzung lesen) |
| **Fotos** | Frankfurt-Stimmung, Orte | WebP, Bildunterschrift + Nachweis | Wikimedia Commons (CC BY / CC BY-SA / CC0), eigene Fotos; **keine Personen ohne schriftliche Einwilligung** |
| **Sprach-Chips** | DE / বাংলা / ትግርኛ / ไทย / ລາວ | Buttons mit `lang`-Attribut | eigen, Schriften lokal (Noto, SIL OFL) |
| **Stern-Motiv** | Wiedererkennung, Trenner, Ladezustand | vorhandenes SVG, dezent animiert (abschaltbar über `prefers-reduced-motion`) | eigen |

## 3 · Seiten-Gerüste (mobil zuerst, Desktop = 2–3 Spalten)
```
START                                   NACHBARSCHAFT
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ ★ Hero: Illustration Skyline  │       │ Hero-Illustration: Einkauf    │
│   Claim + [Hilfe & Mitmachen] │       │ 4 Icon-Kacheln: Einkauf,      │
│ 3 Kennzahl-Kacheln            │       │ Begleitung, Gesellschaft, Hand│
│ 4 Säulen-Karten mit Icon      │       │ Ablauf 1-2-3 (Anruf→Helfer→da)│
│ Schema-Karte Ortsbezirk 10    │       │ Gesucht: Fachkraft (Steckbrief)│
│ Nordstern-Familie (3 Karten)  │       │ Zeitleiste Vereinsgründung    │
│ Zeitleiste „Was als Nächstes“ │       │ [Zur Initiative]              │
└───────────────────────────────┘       └───────────────────────────────┘
FRANKFURT-INFO                          MELDEN & PETITIONEN
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ Schaubild „Wer entscheidet?“  │       │ Ablauf: Sehen→Melden→Bündeln  │
│ (Stadtverordnete → Magistrat  │       │ Großer Button Mängelmelder    │
│  → 16 Ortsbeiräte)            │       │ Petitions-Karten + Balken /220│
│ Themen-Raster mit Icons       │       │ „Eigenes Anliegen“ 3 Schritte │
│ Ratgeber-Karten (Blog)        │       └───────────────────────────────┘
│ Sprach-Chips → bangla/ wege/  │
└───────────────────────────────┘
VERMITTLUNG                             FÜR VEREINE & FIRMEN
┌───────────────────────────────┐       ┌───────────────────────────────┐
│ Dienst-Raster: Icon+Titel+3   │       │ Vorher/Nachher-Vergleich      │
│ Punkte, Filter-Chips (Alltag, │       │ Paket-Karten mit Preis/Zahlung│
│ Arbeit, Wellness, Energie)    │       │ Referenzen als Screenshots    │
│ „So läuft’s“ 3 Schritte       │       │ Ablauf Auftrag in 4 Schritten │
└───────────────────────────────┘       └───────────────────────────────┘
```
Filter-Chips ohne JavaScript: Anker-Sprungmarken oder `:target`; JS nur, wenn Entscheidung in `docs/ENTSCHEIDUNGEN.md` dokumentiert.

## 4 · Bildrechte – Null-Fehler-Regel
Jede Bild-/Grafikdatei braucht einen Eintrag in `data/bilder.json`:
```json
{"datei":"img/roemer.webp","titel":"Römerberg","autor":"Name laut Quelle","quelle_url":"https://commons.wikimedia.org/wiki/File:…","lizenz":"CC BY-SA 4.0","lizenz_url":"https://creativecommons.org/licenses/by-sa/4.0/deed.de","geaendert":"zugeschnitten, WebP","geprueft":"2026-11-15","alt":"Römerberg mit Fachwerkhäusern am Abend"}
```
- **CC BY / BY-SA:** Titel, Autor, Quelle (Link), Lizenz (Link), Änderungen nennen – direkt unter dem Bild **und** auf `bildnachweise.html`.
- **CC0 / Public Domain:** trotzdem Quelle angeben (Transparenz).
- **Verboten:** Bilder aus Google-Suche, Pinterest, Nachrichtenseiten, Social Media; Parteilogos ohne schriftliche Freigabe; Fotos erkennbarer Personen ohne Einwilligung; KI-Bilder echter Orte als „Foto“ ausgeben.
- Lizenz immer **am Original** prüfen, nicht auf Aggregator-Seiten.
- `tools/check.py` bricht ab, wenn ein `<img>`/SVG-Bild keinen vollständigen Eintrag hat.

## 5 · Qualitätskriterien (Abnahme)
- Lighthouse mobil: Performance ≥ 95, Accessibility = 100, Best Practices = 100, SEO ≥ 95 (nach Launch).
- Screenshots je Seite: mobil 390 px und Desktop 1280 px, hell und dunkel.
- Kein Fremdabruf (Netzwerk-Tab leer außer eigener Domain).
- Jede Zahl mit Quelle + Stand, jede Grafik mit Text-Alternative.
