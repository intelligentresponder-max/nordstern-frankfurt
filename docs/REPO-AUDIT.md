# Repo-Audit intelligentresponder-max (15.11.2026)

32 Repos geprüft (25 öffentlich geklont, 2 private gelesen, 5 private bewusst nicht geöffnet: crown7, crown-v10, crown-v10.git-, energieberater-app, sneakers4seekers, inspiredbyipat).

## Sofort handeln
| Befund | Repos | Warum | Vorschlag |
| --- | --- | --- | --- |
| Kein Impressum, aber öffentlich per GitHub Pages | copy-code-agency-website, STAFF, Sneaks4seek, rm-apply, texter-portfolio, bewerbung-copywriter, turmhotel, telavendelele, flinkr-agent, hypnosis, EXTRA7, fughtcyberdevils, model-hub, energie-app, frankfurt-energie-oekostrom, nachbarschaftshilfe-demo | Geschäftsmäßige Seiten brauchen ein Impressum (§ 5 DDG); Abmahnrisiko. | Für Agentur- und Verkaufsseiten Impressum ergänzen; reine Experimente auf privat stellen oder Pages abschalten. |
| `copy-code-agency-website` hat nur 3 Dateien und noch Tomasz als Partner | copy-code-agency-website | Wird das Aushängeschild für Sam + André. | Team/Partner aktualisieren, Impressum, auf Nordstern-Agenturseite verlinken. |
| Doppelte/verwaiste Repos | `crown-v10.git-` (Tippfehler-Kopie), `sneakers4seekers` vs `Sneaks4seek`, `energie-app` / `energieberater-app` / `frankfurt-energie-oekostrom` | Verwirrt Käufer beim Repo-Verkauf und Samuel beim Review. | Archivieren (GitHub → Settings → Archive), nicht löschen. |
| `Frankfurt_FW` Wurzel ist ein Create-React-App-Rest mit fremder `index.html` | Frankfurt_FW | Steht schon im eigenen FEHLER-LOG. | Bürgerplattform in eigenes Repo ziehen (`fw-frankfurt-buergerplattform` existiert, ist aber leer). |
| `fw-frankfurt-buergerplattform` enthält nur eine README | fw-frankfurt-buergerplattform | Leeres privates Repo. | Entweder mit `Frankfurt_FW/buergerplattform` befüllen oder archivieren. |

## Unkritisch geprüft
- Secret-Scan (GitHub-Token, Stripe-Keys, AWS, Telegram-Bot-Token): nur `mindful7777/stripe-api/.env.example` – eine Beispieldatei, kein echter Schlüssel (nur Trefferzahl geprüft, Inhalt nicht ausgegeben).
- Gut gepflegt (CLAUDE.md, CHANGELOG/FEHLER-LOG, Impressum): nh-preungesheim-web, nachbarschaftshilfe-preungesheim, wege-nach-frankfurt, Frankfurt_FW/buergerplattform, bangla-hilfe, topwash.

## Was Nordstern wiederverwendet
| Baustein | Herkunft |
| --- | --- |
| Build-Prinzip „ein Python-Skript erzeugt alle Seiten“ | nh-preungesheim-web/tools/build.py |
| Lokale Schriften Fraunces + Atkinson Hyperlegible (SIL OFL) | nachbarschaftshilfe-preungesheim/app/fonts |
| Positionen FREIE WÄHLER (inkl. Freigabe-Schalter) | Frankfurt_FW/buergerplattform/data/themen.json |
| Bestätigte ffm.de-Links (Mängelmelder, Ideenplattform) | Frankfurt_FW/buergerplattform/data/links.json |
| Lehren aus Pages-Einrichtung, noindex, ungeprüfte Links | Frankfurt_FW/buergerplattform/FEHLER-LOG.md |
