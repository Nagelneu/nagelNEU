# SEO-Strategie NagelNEU

## Markenarchitektur

| Ebene | Rolle | Wo |
|---|---|---|
| **NagelNEU** | Marke | überall |
| **HÄNDE-STOPP** | Methode in vier Schritten: Wahrnehmen, Innehalten, Alternative wählen, Reflektieren | `/haende-stopp/`, App, PDF, Arbeitsblatt |
| **Das 21-Tage-Programm** | Produkt (kostenlos, App im Browser) | `/21-tage-programm/`, `/app/` |
| **YouTube @fingernägelkauen** | Reichweite und Übungen | Verlinkt auf allen Seiten |

**Markensatz:** „Erst bemerken. Dann neu entscheiden.“

**Leitidee:** „Du kaust an deinen Nägeln. Vielleicht seit Jahren. Dafür musst du dich nicht schämen.“

**Nutzen in einem Satz:** NagelNEU hilft Erwachsenen, den automatischen Moment früher zu bemerken und den Händen etwas anderes anzubieten.

## Technik (umgesetzt)

- Eigener `<title>` und eigene Beschreibung je Seite (Titel höchstens 60 Zeichen, Beschreibung höchstens 160)
- Genau eine `<h1>` pro Seite, keine übersprungenen Überschriftenebenen (geprüft)
- Canonical-URL je Seite; `hreflang` zwischen `/` und `/en/` sowie zwischen den beiden Arbeitsblättern
- Open Graph und Twitter-Karte mit eigenem Vorschaubild (DE und EN, 1200 × 630)
- Strukturierte Daten: `Organization`, `WebSite`, `WebPage`, `Article` (Ratgeber), `BreadcrumbList`
- **Bewusst weggelassen:** `FAQPage`, `Product`, `Review` und `AggregateRating`. Es gibt keine echten Bewertungen. FAQ-Rich-Results zeigt Google seit 2023 nur noch für ausgewählte Behörden- und Gesundheitsseiten.
- `robots.txt` mit Verweis auf die Sitemap; `/docs/`, `/tools/`, `/server/` sind ausgeschlossen
- `sitemap.xml` mit `lastmod` und hreflang-Angaben
- Impressum und Datenschutz auf `noindex, follow`
- Lokale Schriften (WOFF, Latin-Teilmenge), Bilder als WebP oder SVG mit festen Maßen, Skript mit `defer`. Die Startseite lädt insgesamt rund 320 KB (gemessen ohne Komprimierung durch den Server).
- 404-Seite mit Weg zur Startseite und zur App

## Themenarchitektur

| Suchabsicht | Seite | Kern-Suchbegriffe |
|---|---|---|
| Überblick, Einstieg | `/` | Nägelkauen abgewöhnen, Nägelkauen Erwachsene |
| Anleitung | `/naegelkauen-abgewoehnen/` | Nägelkauen abgewöhnen, wie höre ich auf Nägel zu kauen, Tipps gegen Nägelkauen |
| Ursachen | `/warum-kaue-ich-naegel/` | warum kaue ich Nägel, Nägelkauen Ursache, Nägelkauen psychisch |
| Situation | `/naegelkauen-bei-stress/` | Nägelkauen Stress, Nägelkauen bei Nervosität |
| Methode, Übungen | `/haende-stopp/` | Übungen gegen Nägelkauen, Alternativen zum Nägelkauen, was tun statt Nägel kauen |
| Produkt | `/21-tage-programm/` | 21 Tage Nägelkauen, Programm gegen Nägelkauen, App gegen Nägelkauen |
| Werkzeug | `/arbeitsblatt/` | Nägelkauen Arbeitsblatt, Tagebuch Nägelkauen |

Jede Ratgeberseite verlinkt auf die Methode, das Programm und die anderen Ratgeber.

## Nächste Inhalte (Vorschläge, noch nicht umgesetzt)

1. `/nagelhaut-knibbeln/`: Nagelhaut knibbeln und abkauen (eigene Suchabsicht, im Programm schon angelegt)
2. `/naegelkauen-unbewusst/`: Wenn du es erst hinterher merkst
3. `/rueckfall-naegelkauen/`: Ausrutscher-Protokoll als eigene Seite
4. `/bitterlack-und-hilfsmittel/`: ehrlicher Vergleich ohne Kaufempfehlung oder Affiliate-Links
5. Englische Ratgeber erst, wenn der englische YouTube-Kanal oder englische Nutzer das rechtfertigen

Pro Monat lieber eine gründliche Seite als vier dünne.

## Google Search Console

1. Auf [search.google.com/search-console](https://search.google.com/search-console) eine Property vom Typ **URL-Präfix** anlegen: `https://nagelneu.github.io/nagelNEU/`
2. Bestätigungsmethode **HTML-Tag** wählen und nur den Code aus `content="…"` kopieren
3. Den Code in `tools/site_base.py` bei `GSC_VERIFICATION` eintragen und `python3 tools/build.py` ausführen. Wer kein Python nutzt, fügt `<meta name="google-site-verification" content="CODE">` direkt im `<head>` von `index.html` ein.
4. Hochladen, bestätigen, dann unter **Sitemaps** `sitemap.xml` einreichen

## Messung (datenschutzgerecht)

Es ist bewusst **kein** Tracking eingebaut. Für erste Erkenntnisse reichen Search Console (Suchbegriffe, Klicks) und YouTube Studio (Verweise auf die Website). Falls später nötig: ein cookieloses, EU-gehostetes Werkzeug ohne Einwilligungspflicht prüfen (z. B. selbst gehostetes Matomo im cookielosen Modus) und die Datenschutzerklärung vorher anpassen. Keine Rankings, keine Erfolgsquoten versprechen.
