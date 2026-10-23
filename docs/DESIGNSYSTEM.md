# NagelNEU Designsystem (Website)

Alle Werte stehen als Variablen am Anfang von `assets/css/site.css`.

## Haltung

Ruhig, warm, menschlich. Papierfarbener Grund wie im PDF-Tagebuch, dunkle „Nacht“-Flächen wie in der App und ein Rosé als einzige Signalfarbe. Die Knibbler-Figuren aus der App sind die einzige Illustration. Es gibt keine Stockfotos und keine erfundenen Menschen.

## Farben

| Name | Wert | Einsatz | Kontrast |
|---|---|---|---|
| `--paper` | `#fbf7f2` | Seitenhintergrund | |
| `--paper-2` | `#f4ece3` | Abwechselnde Abschnitte | |
| `--card` | `#fffdfb` | Karten | |
| `--ink` | `#1f1722` | Text, Überschriften | 16,4 : 1 auf Papier |
| `--ink-2` | `#463c4c` | Einleitungstexte | 9,8 : 1 |
| `--mute` | `#6b6072` | Nebentexte | 5,6 : 1 |
| `--rose` | `#c21f5b` | Buttons, Hervorhebung | 5,8 : 1 mit Weiß |
| `--rose-ink` | `#9f1347` | Links, Eyebrows | 7,4 : 1 |
| `--rose-soft` | `#f9e3eb` | Hinweisflächen | |
| `--green` / `--green-soft` | `#1d7556` / `#e2f1e9` | „realistisch“, Haken | 4,8 : 1 |
| `--amber` / `--amber-soft` | `#8a4f06` / `#fbefd9` | Hinweise, Grenzen | über 4,5 : 1 |
| `--night` / `--night-2` | `#150f18` / `#211827` | Übung, Fußzeile, Abschluss | |
| `--rose-light` | `#ff7ab0` | Akzent auf Nacht | 7,8 : 1 |

Alle Textkombinationen erreichen mindestens WCAG AA (4,5 : 1).

## Schrift

- **Archivo** (variabel, Breite 62 bis 125 %), lokal als `assets/fonts/archivo-var.woff`, SIL Open Font License
  - Überschriften: Gewicht 800, Breite 118 %, Zeilenhöhe 1,08
  - Fließtext: Gewicht 400, Breite 100 %, Zeilenhöhe 1,65
- **Caveat** für kleine handschriftliche Notizen (Leitfragen der Methode, Notiz im Hero), sparsam eingesetzt

| Stufe | Größe |
|---|---|
| `--step--1` | 0,875 rem |
| `--step-0` | 1,0625 rem (Fließtext) |
| `--step-1` | 1,25 rem (h3) |
| `--step-2` | 1,45 bis 1,75 rem |
| `--step-3` | 1,8 bis 2,5 rem (h2) |
| `--step-4` | 2,3 bis 4 rem (h1) |

## Abstände und Breiten

- 4er-Raster: `--s1` 4 px bis `--s10` 128 px
- Abschnitte: 56 bis 112 px oben und unten, je nach Bildschirm
- Textbreite höchstens 66 Zeichen, Seitenbreite höchstens 1160 px, Seitenrand 16 bis 32 px

## Komponenten

- **Buttons:** `btn-primary` (Rosé, weiß), `btn-secondary` (Umriss), `btn-sm`. Mindesthöhe 52 px (klein 42 px), Pillenform.
- **Links:** `arrow-link` mit Pfeil für „Weiter“-Wege
- **Karten:** `card`, `fact`, `step`, `phase`; Radius 18 px, feiner Rand, weicher Schatten
- **Hinweise:** `note` (Bernstein) und `note soft` (Papier)
- **Tags:** `tag`, `tag green`, `tag amber`
- **Formulare:** `input` mit 52 px Höhe; Radio-Karten `.opt` in der Übung
- **FAQ:** natives `<details>`, also ohne JavaScript bedienbar

## Zustände

- **Fokus:** Doppelter Ring (Papier und Rosé) an allen bedienbaren Elementen, nur bei Tastaturbedienung (`:focus-visible`)
- **Hover:** Buttons dunkeln ab, Karten heben sich 2 px an, Pfeile wandern 3 px
- **Bewegung:** Nur sanftes Einblenden beim Scrollen und der Atemkreis in der Übung. Bei „Bewegung reduzieren“ ist alles abgeschaltet.

## Breakpoints

- unter 640 px: alles einspaltig
- ab 640 px: Raster 2-spaltig
- ab 760 px: Methode, Phasen und Fußzeile mehrspaltig
- ab 960 px: Desktop-Navigation, Hero zweispaltig
- ab 1100 px: Methode und Phasen 4-spaltig

## Druck

Kopf, Fuß und Handlungsaufrufe werden beim Drucken ausgeblendet. Das Arbeitsblatt ist für A4 ausgelegt.

## Schreibweise und Typografie

- **Marke und Methode:** NagelNEU, HÄNDE-STOPP (englisch HANDS STOP), immer in dieser Schreibweise.
- **Anführungszeichen:** Deutsch „…“, Englisch “…”, Apostroph ’
- **Striche:** Bis-Strich ohne Leerzeichen bei Bereichen (Tag 1–5, 4–6), kein Geviertstrich
- **Zahlen:** Deutsch mit Komma (0,4 mm), Englisch mit Punkt (0.4 mm)
- **Geschützte Leerzeichen** automatisch zwischen Zahl und Einheit (5 Minuten, 60 Sekunden, 3 mm), bei „Tag 1“, „Nr. 1“, „z. B.“, „§ 5“, „© 2026“ und der Telefonnummer. Auf der Website erledigt das `tools/site_base.py`, in der App eine Typografie-Funktion im Skript.
- **Umbruch:** Überschriften ausgeglichen (`text-wrap: balance`), Absätze ohne einzelne Wörter in der letzten Zeile (`text-wrap: pretty`), Silbentrennung auf schmalen Bildschirmen
- **Satzzeichen:** Listenpunkte als ganze Sätze enden mit Punkt, Stichworte ohne
