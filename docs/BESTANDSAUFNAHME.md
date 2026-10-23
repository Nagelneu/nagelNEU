# Bestandsaufnahme NagelNEU (Stand 22.10.2026)

Ausgangszustand gesichert als Git-Tag `ausgangszustand-2026-10-22` (Commit `56866f3`).

## A. Vorhandene Dateien und Projektstruktur

| Datei | Inhalt |
|---|---|
| `index.html` (377 KB) | Die komplette NagelNEU-App in einer Datei: HTML, CSS und JavaScript. Deutsch und Englisch, Chat-Assistent, Tagebuch mit Spracheingabe, Fotos, PDF-Export, Knibbler-Figuren als SVG im Code. |

Sonst gab es keine Dateien: keine weiteren Seiten, keine Bilder, keine `robots.txt`, keine Sitemap, keine Favicons und keinen Ordner `fonts/`.

## B. Tatsächlich gefundene Probleme

**Nachgewiesen (im Code geprüft oder im Browser getestet):**

1. **Keine Website, nur App.** Wer die Adresse aufruft, landet direkt in der App. Es gibt keine Seite, die in Ruhe erklärt, für wen NagelNEU gedacht ist, was die Methode ist und welche Grenzen das Angebot hat.
2. **SEO-Grundlagen fehlen.** Es gab keine Canonical-URL, kein Open Graph, keine strukturierten Daten, keine Sitemap und keine `robots.txt`. Die Inhalte entstehen erst durch JavaScript, deshalb steht für Suchmaschinen kaum lesbarer Text im HTML. Mehrere `<h1>` werden dynamisch erzeugt.
3. **Datenübertragung an Dritte.** Schriften kamen von Google Fonts, die PDF-Bibliothek von jsDelivr. Beim Laden ging die IP-Adresse an Google. Das ist in Deutschland rechtlich heikel (LG München I, 20.01.2022, 3 O 17493/20).
4. **E-Mail ohne Ziel.** `LEAD_URL` ist leer. Die Pflicht-E-Mail-Adresse wurde also abgefragt, aber nirgends hingeschickt. Das ist unnötige Datenerhebung mit einem Einwilligungstext, der nicht zutrifft.
5. **Rechtstexte unvollständig.** Impressum, Datenschutz und Nutzungsbedingungen enthalten Platzhalter in eckigen Klammern. Ein eigenständig erreichbares Impressum fehlte.
6. **Zu starke Aussage.** „Aufgebaut nach einer Methode, die sich in der Verhaltenstherapie bewährt hat“ klingt wie ein Wirksamkeitsnachweis für das Programm selbst.
7. **Begriffe uneinheitlich.** Die Startseite der App nannte „Bemerken, Unterbrechen, Ersetzen, Belohnen“, Notfallkarte, PDF und Plan dagegen „Die 4 B: Bemerken, Ballen, Beschäftigen, Belohnen“. Eine Marke „HÄNDE-STOPP“ als Methode gab es noch nicht.
8. **Darstellung auf dem Handy.** In der App-Kachel „Das System“ wurden die Wörter bei 390 px Breite abgeschnitten.

**Begründete Vermutungen (nicht abschließend prüfbar):**

- Die genaue Schreibweise der Repository-Adresse (`nagelNEU` oder `nagelneu`) ließ sich von hier aus nicht prüfen. Verwendet wird die Adresse aus dem Auftrag: `https://nagelneu.github.io/nagelNEU/`.
- Ob die Seite schon bei Google angemeldet ist, ist unbekannt. Eine Suche nach der Adresse ergab keinen Treffer.

## C. Verbesserungen nach Priorität

1. **Rechtliches:** Impressum- und Datenschutzseite anlegen. Die Platzhalter muss der Betreiber selbst ausfüllen (siehe OFFENE-PUNKTE.md).
2. **Website:** Eigene Startseite mit klarer Zielgruppe, HÄNDE-STOPP-Methode, Einstiegsübung, Programm, Übersicht, Geschichte, FAQ und Handlungsaufruf. Die App zieht nach `/app/` um.
3. **Datenschutz:** Schriften und PDF-Bibliothek liegen jetzt lokal. Die E-Mail-Adresse ist freiwillig, solange kein Versanddienst angebunden ist.
4. **SEO:** Canonical, hreflang, Open Graph, strukturierte Daten, Sitemap, `robots.txt`, eigene Ratgeberseiten.
5. **Marke:** HÄNDE-STOPP als einheitliche Methode in Website und App.
6. **Druckbares Arbeitsblatt**, englische Startseite, YouTube-Strategie.

## D. Risiken und offene Fragen

- **Impressum und Datenschutz** sind online, aber noch nicht vollständig ausgefüllt. Das ist das größte Risiko, solange die Seite öffentlich ist.
- **Kopplung der kostenlosen Nutzung** an E-Mail-Einwilligung und YouTube-Abo: Wird `LEAD_URL` gesetzt, ist die E-Mail wieder Pflicht. Ob diese Kopplung zulässig ist (Art. 7 Abs. 4 DSGVO, Kopplungsverbot), sollte rechtlich geprüft werden. Empfehlung: E-Mail freiwillig lassen, Newsletter mit Double-Opt-in.
- **Persönliche Geschichte:** Es sind nur die Angaben aus dem Auftrag verwendet. Details muss der Betreiber ergänzen.
- **Bewertungen:** Die drei Bewertungen in der App erscheinen erst, wenn echte Texte eingetragen sind. Es wurden keine Texte erfunden.

## E. Umgesetzte Änderungen an konkreten Dateien

| Datei | Änderung |
|---|---|
| `index.html` | Neue Startseite (Deutsch). Alte Links mit `#tagebuch` oder `?lang=` führen automatisch in die App. |
| `en/index.html` | Neue englische Startseite |
| `app/index.html` | Die App (vorher `index.html`): lokale Schriften, lokale PDF-Bibliothek mit Ersatz-Download, einheitliche HÄNDE-STOPP-Begriffe in Deutsch, Englisch, PDF, Plan und Chat, abgeschwächte Therapie-Aussage, E-Mail freiwillig ohne Versanddienst, Link zur Website, Canonical, Favicon |
| `app/vendor/pdf-lib.min.js` | PDF-Bibliothek lokal (MIT-Lizenz) |
| `haende-stopp/`, `21-tage-programm/` | Methode und Programm im Detail |
| `naegelkauen-abgewoehnen/`, `warum-kaue-ich-naegel/`, `naegelkauen-bei-stress/` | Ratgeberseiten mit Quellen |
| `arbeitsblatt/`, `en/worksheet/` | Druckbares Arbeitsblatt |
| `impressum/`, `datenschutz/`, `404.html` | Rechtliches und Fehlerseite |
| `robots.txt`, `sitemap.xml` | Suchmaschinen-Technik |
| `assets/` | Designsystem (CSS), Skript, Schriften (OFL), Bilder, Favicons, Vorschaubilder |
| `tools/` | Python-Skripte, die alle Seiten erzeugen (`python3 tools/build.py`) |
| `server/chat-proxy.php` | Optionale KI-Anbindung für den Chat (läuft nicht auf GitHub Pages) |
| `tagebuch-einbetten.html` | Baustein, um das Tagebuch auf einer anderen Website einzubetten |
