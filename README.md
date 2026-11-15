# Nordstern Frankfurt

Sozial. Informiert. Vernetzt. – Dachseite für den Frankfurter Norden.
Briefing: [CLAUDE.md](CLAUDE.md) · Entscheidungen: [docs/ENTSCHEIDUNGEN.md](docs/ENTSCHEIDUNGEN.md) · Domain: [docs/DOMAIN-SETUP.md](docs/DOMAIN-SETUP.md) · Fehler: [FEHLER-LOG.md](FEHLER-LOG.md) · Repo-Audit: [docs/REPO-AUDIT.md](docs/REPO-AUDIT.md)

## Bauen (Termux oder Git Bash)
```bash
python3 tools/build.py      # erzeugt alle .html aus data/*.json
python3 tools/check.py      # 0 Fehler = darf gepusht werden
```
Lokal ansehen: `python3 -m http.server 8000` → http://localhost:8000

## Struktur
| Pfad | Inhalt |
| --- | --- |
| `data/site.json` | Marke, Betreiber, Domain, **Launch-Schalter** |
| `data/dienste.json` | Vermittlungsangebote (+ interne Prüfpunkte) |
| `data/petitionen.json` | Anliegen, Ziel 220 Unterstützer |
| `data/standpunkte.json` | FW-Positionen, nur `freigegeben: true` wird gezeigt |
| `data/zahlung.json` | Agentur-Pakete mit Stripe-/Gumroad-Zahlungslink (erst sichtbar mit Preis + Link) |
| `data/links.json` | Nur im Browser bestätigte externe Links |
| `tools/build.py`, `tools/check.py` | Generator und Prüfung |
| `css/`, `fonts/` | Gestaltung, lokale Schriften (SIL OFL) |

Status: **Vorschau** (`noindex`, kein CNAME), bis Impressumsdaten und Domain eingetragen sind.
