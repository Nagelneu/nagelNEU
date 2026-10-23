# NagelNEU

**Erst bemerken. Dann neu entscheiden.**
Ein kostenloser Begleiter für Erwachsene, die das Nägelkauen verändern möchten: die HÄNDE-STOPP-Methode und ein 21-Tage-Programm im Browser, auf Deutsch und Englisch.

Live: https://nagelneu.github.io/nagelNEU/

## Aufbau

```
/                         Startseite (Deutsch)
/en/                      Startseite (Englisch)
/app/                     Die NagelNEU-App (21-Tage-Programm, Tagebuch, PDF, Chat)
/haende-stopp/            Die Methode mit Übung
/21-tage-programm/        Das Programm im Detail
/naegelkauen-abgewoehnen/ Ratgeber
/warum-kaue-ich-naegel/   Ratgeber
/naegelkauen-bei-stress/  Ratgeber
/arbeitsblatt/            Arbeitsblatt zum Ausdrucken (EN: /en/worksheet/)
/impressum/ /datenschutz/ Rechtliches
assets/                   CSS, Skript, Schriften, Bilder
tools/                    Python-Skripte, die alle Seiten erzeugen
server/chat-proxy.php     Optionale KI-Anbindung (braucht PHP, läuft nicht auf GitHub)
docs/                     Bestandsaufnahme, Designsystem, SEO, YouTube, offene Punkte
```

Auf jeder Seite sitzt unten links der Chat-Assistent („Fragen?“). Er öffnet den Chat der App als Fenster und lädt erst beim ersten Klick.

Alte Links wie `…/nagelNEU/#tagebuch` oder `…/nagelNEU/?lang=en` führen automatisch in die App. Gespeicherte Einträge bleiben erhalten, weil die Adresse dieselbe Domain hat.

## Hochladen

Den kompletten Ordnerinhalt ins Repository laden (bei GitHub: **Add file → Upload files**, alles hineinziehen) und **Commit changes** klicken. GitHub Pages ist bereits aktiv.

## Seiten ändern

Die Seiten entstehen aus `tools/*.py`. Nach Änderungen dort:

```
python3 tools/build.py
```

Kleine Textkorrekturen gehen auch direkt in den HTML-Dateien. Sie werden aber beim nächsten Bauen überschrieben.

## Erst lesen

`docs/OFFENE-PUNKTE.md`: Impressum und Datenschutz müssen noch mit echten Angaben gefüllt werden.

## Lizenzen

Design, Texte, Figuren und Software: Design by Frank Zimmermann © 2026, alle Rechte vorbehalten. Ein öffentliches Repository ist sichtbar, gibt aber keine Nutzungsrechte frei.
Schriften: Archivo und Caveat unter SIL Open Font License (`assets/fonts/OFL-*.txt`). pdf-lib unter MIT-Lizenz (`app/vendor/LICENSE-pdf-lib.md`).
