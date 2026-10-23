# Offene Punkte für Frank

Diese Punkte kann nur der Betreiber erledigen. Sie sind nach Dringlichkeit sortiert.

## Sofort (rechtlich)

1. **Impressum ausfüllen:** `impressum/index.html` sowie in der App `LEGAL.impressum` (Deutsch) und `EN_DATA.LEGAL.impressum` (Englisch). Nötig sind Anschrift, E-Mail und gegebenenfalls eine Umsatzsteuer-ID. Alle Platzhalter stehen in eckigen Klammern `[ ]`.
2. **Datenschutzerklärung ausfüllen und prüfen lassen:** `datenschutz/index.html` und die Texte in der App. Verantwortlicher, Anschrift, E-Mail, später der Newsletter-Dienst.
3. **Nutzungsbedingungen in der App:** Platzhalter `[Name und Anschrift des Anbieters]`, `[E-Mail]`, `[Datum]`
4. **E-Mail-Pflicht klären:** Solange `LEAD_URL` leer ist, bleibt die E-Mail-Adresse freiwillig. Wird ein Versanddienst angebunden, ist sie wieder Pflicht. Lass prüfen, ob die Kopplung „kostenlos nur gegen E-Mail und YouTube-Abo“ zulässig ist (Kopplungsverbot, Art. 7 Abs. 4 DSGVO). Empfehlung: freiwillig lassen und Double-Opt-in nutzen.

## Bald (Inhalt)

5. **Persönliche Geschichte bestätigen und ergänzen:** Auf der Startseite steht nur, was im Auftrag stand. Frank kennt Nägelkauen aus eigener Erfahrung und kennt den Weg, es zu verändern. Gut wären zum Beispiel: seit wann, was der Wendepunkt war, was geholfen hat, gern ein echtes Foto. Die Stelle ist im Code mit `OFFENER PUNKT` markiert, in `tools/pages_home.py` und in `index.html`.
6. **Bewertungen:** In `app/index.html` bei `REVIEWS` echte Texte von Petra, Stephan und Simone eintragen, nur mit deren Einverständnis. Ohne Text erscheinen sie nicht. Auf der Website gibt es bewusst keine Bewertungen.
7. **PayPal-Link testen:** `PAYPAL_URL` in `app/index.html` einmal selbst aufrufen
8. **Adresse prüfen:** Alle Seiten nutzen `https://nagelneu.github.io/nagelNEU/`. Heißt das Repository anders geschrieben, ändere `SITE` und `BASE_PATH` in `tools/site_base.py` und baue neu, sonst passen Canonical-URLs und Sitemap nicht.

## Später (Wachstum)

9. Google Search Console einrichten (siehe `docs/SEO-STRATEGIE.md`)
10. YouTube-Kanal mit der Website verknüpfen (siehe `docs/YOUTUBE-STRATEGIE.md`)
11. Optional: KI-Chat über `server/chat-proxy.php` auf einem PHP-Webspace. Den Schlüssel nur dort eintragen, nie auf GitHub.
12. Optional: Besucherzähler (`COUNTER_URL`). Vorher die Datenschutzerklärung ergänzen.

## Als neuer Programminhalt gekennzeichnet

- Die Website beschreibt die Methode jetzt als **HÄNDE-STOPP in vier Schritten** (Wahrnehmen, Innehalten, Alternative wählen, Reflektieren). Die App wurde daran angeglichen. Vorher hieß es dort „Die 4 B“.
- Die vier Phasen-Beschreibungen in der 21-Tage-Übersicht sind neu formuliert. Die Tagestitel stammen unverändert aus der App.
