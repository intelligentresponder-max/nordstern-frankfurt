# Eigene Domain – Schritt für Schritt

Wunschname: **nordstern-frankfurt.de** (Alternativen: `nordstern-ffm.de`, `frankfurter-nordstern.de`, `nordlicht-frankfurt.de`).
Verfügbarkeit wurde NICHT geprüft – zuerst beim Anbieter suchen.

## 1 · Domain kaufen (ca. 5–15 € / Jahr für .de)
Bei einem deutschen Registrar mit DNS-Verwaltung. Kein Hosting-Paket dazubuchen – Pages ist kostenlos.
Fehler aus der Vergangenheit: ungenutztes Hosting-Paket bei frankfurt-energie.online lief weiter → **nur Domain buchen, Kündigungsfrist notieren.**

## 2 · GitHub vorbereiten (zuerst!)
GitHub → Profil → Settings → Pages → **Add a domain** → `nordstern-frankfurt.de` → GitHub zeigt einen TXT-Eintrag (`_github-pages-challenge-nordstern-ffm`). Das verhindert, dass jemand anders die Domain auf sein Repo lenkt (Domain-Übernahme).

## 3 · DNS-Einträge beim Registrar
| Typ | Name | Wert |
| --- | --- | --- |
| TXT | `_github-pages-challenge-nordstern-ffm` | Code aus Schritt 2 |
| A | `@` | 185.199.108.153 |
| A | `@` | 185.199.109.153 |
| A | `@` | 185.199.110.153 |
| A | `@` | 185.199.111.153 |
| CNAME | `www` | `nordstern-ffm.github.io` |
Die IPs vor dem Eintragen mit der GitHub-Doku „Managing a custom domain for your GitHub Pages site“ abgleichen.

## 4 · Repo umschalten
In `data/site.json`: `domain_bestaetigt: true`, Betreiber-Anschrift/E-Mail/Telefon eintragen, dann `launch: true`.
```bash
python3 tools/build.py && python3 tools/check.py --launch
```
Erst bei „0 Fehler“ committen – dann erzeugt build.py die Datei `CNAME`, entfernt `noindex` und öffnet `robots.txt`.

## 5 · HTTPS
Repo → Settings → Pages → Custom domain steht drin → **Enforce HTTPS** anhaken (geht erst, wenn das Zertifikat da ist, meist < 1 Std., bis 24 Std.).

## E-Mail unter der Domain
`kontakt@nordstern-frankfurt.de` braucht einen Mail-Dienst (beim Registrar oft für wenige € dabei). MX-Einträge laut Anbieter setzen.
