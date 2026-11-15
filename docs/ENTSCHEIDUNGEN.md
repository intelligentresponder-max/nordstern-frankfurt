# Entscheidungen – Alternativen doppelt geprüft (Nutzen / Sicherheit / neuer Weg)

## E1 · Eine Marke, getrennte Verantwortung
**Gewählt:** Nordstern als Dach, betrieben von André / Copy & Code Agency. Verein, Partei und Vermittlung je in eigenem, gekennzeichnetem Bereich.
| Alternative | Nutzen | Sicherheit | Ergebnis |
| --- | --- | --- | --- |
| Alles als Vereinsseite | ein Absender | **Gemeinnützigkeit in Gefahr**: Ein gemeinnütziger Verein darf keine Partei fördern (§ 55 Abs. 1 Nr. 1 AO) und keine gewerbliche Vermittlung im Vordergrund haben | verworfen |
| Alles gemischt ohne Kennzeichnung | einfach | Glaubwürdigkeit leidet; Senioren, die Hilfe suchen, landen bei Parteiwerbung | verworfen |
| **Dach + Bereiche** | Reichweite wird geteilt, Risiken getrennt | Verein verlinkt nicht zurück auf Partei/Geschäft | **gewählt** – vor Gründung mit Steuerberatung bestätigen |

## E2 · Mängelmelder
**Gewählt:** Verlinken auf den städtischen Mängelmelder (ffm.de). Eigener Melder hätte Fotos mit Standort/Personen (DSGVO), Moderation und keine Weiterleitung an die Verwaltung bedeutet. **Neuer Weg später:** Monatlicher Blogbeitrag „Was im Norden gemeldet wurde“ – Mehrwert ohne Datenhaltung.

## E3 · Petitionen „220 Bürger“
**Gewählt:** Anliegen hier vorstellen und Fortschritt zeigen; Unterschriften extern (ffm.de-Ideenplattform oder openPetition). Eigene Unterschriftenliste = politische Meinung = besondere Kategorie (Art. 9 DSGVO) → zu riskant für eine statische Seite. Zahl 220 steht nur in `data/petitionen.json`.
**Zu prüfen:** Gilt für ffm.de-Ideen wirklich eine 200er-Schwelle? (laut Bürgerplattform-FEHLER-LOG unbestätigt). Für ein Bürgerbegehren gelten andere, viel höhere Quoren (HGO § 8b).

## E4 · Technik
**Gewählt:** Statisches HTML aus Python-Skript, kein JS, kein npm. Läuft in Termux.
| Alternative | Warum nicht |
| --- | --- |
| React (wie Frankfurt_FW-Wurzel) | Build-Kette, auf Termux fehleranfällig, für Infoseite unnötig |
| Tailwind-CDN | Besucher-IP an Dritte; laut eigenem FEHLER-LOG bereits einmal ersetzt |
| WordPress | Hosting-Kosten, Updates, Angriffsfläche |
| **Neuer Weg geprüft:** Eleventy/Hugo | sinnvoll ab ~30 Seiten/Blog; bis dahin reicht build.py |

## E5 · Hosting & Domain
**Gewählt (Start):** GitHub Pages + eigene Domain (kostenlos, HTTPS automatisch).
**Später:** EU-Hoster (z. B. ein deutscher Anbieter mit statischem Hosting), weil Pages in den USA liegt – steht ehrlich in der Datenschutzerklärung.

## E6 · Kontakt
**Gewählt:** `mailto:`-Link. Formspree (früher in copy-code-agency genutzt) = US-Dienst, Formulardaten außerhalb der EU → verworfen. Später EU-Formulardienst prüfen.

## E7 · Vermittlung – Risiken je Dienst (nicht öffentlich, steht in `data/dienste.json` → `pruefen`)
- Personal: private Arbeitsvermittlung ist erlaubnisfrei, Gewerbeanmeldung genügt; Zeitarbeit braucht AÜG-Erlaubnis, Vermittlungsgutscheine eine AZAV-Zulassung.
- Hotel: Interessenkonflikt mit eigenem Arbeitgeber vorab klären.
- Taxi: nur vermitteln, nicht befördern (Personenbeförderungsgesetz).
- Massage: nur Fachpersonal, keine Heilversprechen, strikt getrennt vom Projekt STAFF.
- Nähen: Status der Näherinnen klären (Scheinselbstständigkeit).
