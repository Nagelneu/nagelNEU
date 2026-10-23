"""Arbeitsblatt (DE/EN), Impressum, Datenschutz, 404."""
import os
from site_base import E, ROOT, SITE, BASE_PATH, YT_URL, page, breadcrumb_ld, header, footer, LOGO_SVG

PH = lambda t: f'<span class="ph">[{t}]</span>'


def worksheet(lang):
    if lang == "de":
        path, title = "arbeitsblatt/", "HÄNDE-STOPP-Arbeitsblatt zum Ausdrucken | NagelNEU"
        desc = "Kostenloses Arbeitsblatt gegen Nägelkauen: 7-Tage-Beobachtungsbogen nach der HÄNDE-STOPP-Methode, Wenn-dann-Sätze und eine Notfallkarte zum Ausschneiden."
        t = dict(crumb="Arbeitsblatt", eyebrow="Zum Ausdrucken", h1="HÄNDE-STOPP-Arbeitsblatt",
                 lead="Ein Bogen für sieben Tage: Notiere, wann du kaust, was du bemerkt hast und was geholfen hat. Nach einer Woche erkennst du dein Muster.",
                 print="Arbeitsblatt drucken", how="So nutzt du den Bogen",
                 howl=["Trage jeden Moment ein, in dem deine Hand zum Mund wollte, auch wenn du es erst hinterher bemerkt hast.",
                       "Kreuze an, ob du innehalten konntest. Es geht nicht um Perfektion, sondern ums Bemerken.",
                       "Schau am Ende der Woche auf deine Einträge: Welche zwei Situationen kommen am häufigsten vor?"],
                 cols=["Tag", "Situation und Ort", "Auslöser", "Bemerkt (vorher / währenddessen / danach)", "Innegehalten?", "Alternative", "Was habe ich bemerkt?"],
                 days=["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"], ifthen="Meine Wenn-dann-Sätze",
                 ifl=["Wenn ______________________, dann ______________________.", "Wenn ______________________, dann ______________________."],
                 card="Notfallkarte zum Ausschneiden", steps=[("Wahrnehmen", "„Meine Hand will zum Mund.“"), ("Innehalten", "Fäuste 3 Sek., lösen, Hände flach. 4 ein, 6 aus."),
                                                             ("Alternative wählen", "Knetball, Stift, Creme, Feile."), ("Reflektieren", "Was hat es ausgelöst?")],
                 week="Mein Wochenrückblick", wq=["Meine häufigsten Situationen:", "Was hat am besten geholfen:", "Was ich nächste Woche anders mache:"],
                 foot="NagelNEU · HÄNDE-STOPP-Arbeitsblatt · " + SITE, back="Zurück zur Methode", back_href="../haende-stopp/", app="../app/", app_l="Im 21-Tage-Programm weiterüben")
    else:
        path, title = "en/worksheet/", "HANDS STOP worksheet to print | NagelNEU"
        desc = "Free nail-biting worksheet: a 7-day observation sheet based on the HANDS STOP method, if-then plans and an emergency card to cut out."
        t = dict(crumb="Worksheet", eyebrow="Printable", h1="HANDS STOP worksheet",
                 lead="One sheet for seven days: note when you bite your nails, what you noticed and what helped. After a week you will see your pattern.",
                 print="Print the worksheet", how="How to use the sheet",
                 howl=["Write down every moment your hand wanted to go to your mouth, even if you only noticed afterwards.",
                       "Tick whether you were able to pause. It is not about perfection, it is about noticing.",
                       "At the end of the week, look at your entries: which two situations come up most often?"],
                 cols=["Day", "Situation and place", "Trigger", "Noticed (before / during / after)", "Paused?", "Alternative", "What did I notice?"],
                 days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], ifthen="My if-then plans",
                 ifl=["When ______________________, then ______________________.", "When ______________________, then ______________________."],
                 card="Emergency card to cut out", steps=[("Notice", "“My hand wants to go to my mouth.”"), ("Pause", "Fists 3 sec., release, hands flat. 4 in, 6 out."),
                                                         ("Choose an alternative", "Stress ball, pen, cream, nail file."), ("Reflect", "What set it off?")],
                 week="My weekly review", wq=["My most common situations:", "What helped most:", "What I will do differently next week:"],
                 foot="NagelNEU · HANDS STOP worksheet · " + SITE + "en/", back="Back to the method", back_href="../#method", app="../../app/?lang=en", app_l="Keep practising in the 21-day programme")
    head = "".join(f"<th scope=\"col\">{E(c)}</th>" for c in t["cols"])
    rows = "".join(f'<tr><th scope="row" class="row-label">{d}</th>' + "<td></td>" * (len(t["cols"]) - 1) + "</tr>" for d in t["days"])
    steps = "".join(f"<li><strong>{E(a)}</strong> {E(b)}</li>" for a, b in t["steps"])
    wq = "".join(f'<p style="margin:14px 0 4px"><strong>{E(q)}</strong></p><div class="lines"></div><div class="lines"></div>' for q in t["wq"])
    ifl = "".join(f'<p style="margin:16px 0">{E(x)}</p>' for x in t["ifl"])
    howl = "".join(f"<li>{E(x)}</li>" for x in t["howl"])
    home = "../" if lang == "de" else "../"
    body = f"""
<section class="hero no-print" style="padding-bottom:24px">
  <div class="wrap">
    <nav class="breadcrumb" aria-label="Breadcrumb"><a href="{home}">{'Start' if lang == 'de' else 'Home'}</a><span aria-hidden="true">›</span>{t['crumb']}</nav>
    <span class="eyebrow">{t['eyebrow']}</span>
    <h1>{t['h1']}</h1>
    <p class="lead">{t['lead']}</p>
    <div class="btn-row"><button class="btn btn-primary" type="button" data-print>{t['print']}</button><a class="btn btn-secondary" href="{t['back_href']}">{t['back']}</a></div>
    <h2 style="font-size:var(--step-1);margin-top:32px">{t['how']}</h2>
    <ol>{howl}</ol>
  </div>
</section>
<section style="padding-top:0">
  <div class="wrap">
    <div class="sheet">
      <p style="display:flex;align-items:center;gap:10px;margin:0 0 6px">{LOGO_SVG}<strong class="brand-mark">Nagel<b>NEU</b></strong></p>
      <h2 style="margin-bottom:6px">{t['h1']}</h2>
      <p class="small mute">{'Name' if lang == 'en' else 'Name'}: ____________________ &nbsp; {'Week from' if lang == 'en' else 'Woche ab'}: ____________</p>
      <div style="overflow-x:auto"><table><thead><tr>{head}</tr></thead><tbody>{rows}</tbody></table></div>
      <div class="grid-2" style="margin-top:24px;align-items:start">
        <div><h3>{t['ifthen']}</h3>{ifl}<h3 style="margin-top:20px">{t['week']}</h3>{wq}</div>
        <div style="border:2px dashed var(--line-2);border-radius:16px;padding:18px">
          <h3>✂ {t['card']}</h3><p class="method-word" style="color:var(--rose);margin:0 0 8px">{'HÄNDE-STOPP' if lang == 'de' else 'HANDS STOP'}</p>
          <ol style="margin:0;padding-left:1.2em">{steps}</ol>
        </div>
      </div>
      <p class="small mute" style="margin-top:24px">{E(t['foot'])}</p>
    </div>
    <p class="no-print" style="margin-top:24px"><a class="arrow-link" href="{t['app']}">{t['app_l']}</a></p>
  </div>
</section>"""
    alts = {"de": "arbeitsblatt/", "en": "en/worksheet/"}
    ld = [breadcrumb_ld([("Start" if lang == "de" else "Home", "" if lang == "de" else "en/"), (t["crumb"], path)])]
    page(path, lang, title, desc, body, alternates=alts, ld=ld, alt_path=("en/worksheet/" if lang == "de" else "arbeitsblatt/"))


def impressum():
    body = f"""
<section class="hero"><div class="narrow legal">
  <span class="eyebrow">Rechtliches</span>
  <h1>Impressum</h1>
  <p class="note"><strong>Hinweis an den Betreiber:</strong> Die markierten Felder müssen mit deinen echten Angaben ausgefüllt werden, bevor die Seite öffentlich beworben wird. Siehe docs/OFFENE-PUNKTE.md.</p>
  <h2>Angaben gemäß § 5 DDG</h2>
  <p>Frank Zimmermann<br>{PH('Straße und Hausnummer')}<br>{PH('PLZ und Ort')}<br>Deutschland</p>
  <h2>Kontakt</h2>
  <p>E-Mail: {PH('E-Mail-Adresse')}<br>Telefon: {PH('Telefonnummer, optional')}</p>
  <h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
  <p>Frank Zimmermann, Anschrift wie oben</p>
  <h2>Umsatzsteuer</h2>
  <p>{PH('Umsatzsteuer-ID, falls vorhanden. Sonst diesen Abschnitt löschen.')}</p>
  <h2>Hinweis zu den Inhalten</h2>
  <p>NagelNEU ist ein Selbsthilfe-Angebot. Die Inhalte dienen der allgemeinen Information und ersetzen keine ärztliche oder psychotherapeutische Beratung, Diagnose oder Behandlung.</p>
  <h2>Haftung für Links</h2>
  <p>Diese Website enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter verantwortlich. Bei Bekanntwerden von Rechtsverletzungen entfernen wir derartige Links umgehend.</p>
  <h2>Urheberrecht</h2>
  <p>Design, Texte, Figuren und Software: Design by Frank Zimmermann © 2026. Alle Rechte vorbehalten. Die verwendeten Schriften Archivo und Caveat stehen unter der SIL Open Font License.</p>
  <h2>Verbraucherstreitbeilegung</h2>
  <p>Wir sind nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren vor einer Verbraucherschlichtungsstelle teilzunehmen.</p>
</div></section>"""
    page("impressum/", "de", "Impressum | NagelNEU", "Impressum von NagelNEU.", body, robots="noindex, follow")


def datenschutz():
    body = f"""
<section class="hero"><div class="narrow legal prose">
  <span class="eyebrow">Rechtliches</span>
  <h1>Datenschutzerklärung</h1>
  <p class="note"><strong>Hinweis an den Betreiber:</strong> Bitte die markierten Felder ausfüllen und die Erklärung vor der Bewerbung der Seite rechtlich prüfen lassen. Sie beschreibt den technischen Stand vom 22.10.2026.</p>

  <h2>1. Verantwortlicher</h2>
  <p>Frank Zimmermann, {PH('Anschrift')}, E-Mail: {PH('E-Mail-Adresse')}</p>

  <h2>2. Kurz zusammengefasst</h2>
  <ul>
    <li>Diese Website setzt <strong>keine Cookies</strong> und nutzt <strong>keine Analyse- oder Werbedienste</strong>.</li>
    <li>Schriften und Programmbibliotheken liegen auf unserem eigenen Webspace. Es werden keine Dateien von Google Fonts oder anderen Schrift-Servern geladen.</li>
    <li>Alles, was du in der App einträgst, bleibt <strong>in deinem Browser auf deinem Gerät</strong>.</li>
    <li>Die Übung auf der Startseite speichert und überträgt nichts.</li>
  </ul>

  <h2>3. Hosting über GitHub Pages</h2>
  <p>Diese Website wird über GitHub Pages bereitgestellt, einen Dienst der GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, USA. Beim Aufruf der Seiten verarbeitet GitHub technisch notwendige Daten, insbesondere deine IP-Adresse, Datum und Uhrzeit des Abrufs, die aufgerufene Seite und Angaben zu deinem Browser. Das dient der sicheren und stabilen Auslieferung der Website (Art. 6 Abs. 1 lit. f DSGVO). Dabei kann eine Übermittlung in die USA stattfinden. Näheres findest du in der <a href="https://docs.github.com/de/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener" target="_blank">Datenschutzerklärung von GitHub</a>.</p>

  <h2>4. Die NagelNEU-App</h2>
  <p>Die App läuft vollständig in deinem Browser. Profil, Fortschritt, Tagebuch, Briefe, Fotos und Sprachaufnahmen werden ausschließlich lokal auf deinem Gerät gespeichert (Browser-Speicher „localStorage“ und „IndexedDB“). Wir erhalten diese Daten nicht. Du kannst sie in der App unter „Ich“ mit „Alles zurücksetzen“ oder über die Einstellungen deines Browsers jederzeit löschen.</p>
  <p>Diese lokale Speicherung ist für die Funktion der App erforderlich (§ 25 Abs. 2 Nr. 2 TDDDG). Bitte beachte: Wer Zugriff auf dein Gerät und deinen Browser hat, kann diese Einträge unter Umständen sehen. Nutze bei geteilten Geräten am besten ein eigenes Browser-Profil.</p>
  <p>Die Startseite liest, falls vorhanden, Vorname und Startdatum aus diesem lokalen Speicher, um dich mit „Willkommen zurück“ zu begrüßen. Auch dabei wird nichts übertragen.</p>

  <h2>5. Spracheingabe</h2>
  <p>Wenn du im Tagebuch oder im Chat die Spracheingabe nutzt, verwendet dein Browser die Spracherkennung seines Herstellers. Je nach Browser wird die Aufnahme dafür an dessen Server übermittelt, zum Beispiel an Google bei Chrome oder an Apple bei Safari. Darauf haben wir keinen Einfluss. Die Spracheingabe startet nur, wenn du sie aktiv antippst und den Mikrofonzugriff erlaubst.</p>

  <h2>6. E-Mail-Adresse beim Programmstart</h2>
  <p>Beim Start des Programms bitten wir um deine E-Mail-Adresse. Solange kein Versanddienst angebunden ist, bleibt sie nur lokal in deinem Browser gespeichert und wird nicht an uns übertragen. {PH('Sobald ein Newsletter- oder Formulardienst angebunden ist: Name und Sitz des Dienstes, Zweck, Rechtsgrundlage Art. 6 Abs. 1 lit. a DSGVO, Double-Opt-in, Widerruf über den Abmeldelink, Speicherdauer.')}</p>

  <h2>7. Chat-Assistent</h2>
  <p>Der eingebaute Chat-Assistent beantwortet Fragen direkt in deinem Browser. Deine Fragen werden dabei nicht übertragen. {PH('Nur falls eine KI-Anbindung aktiviert wird: Fragen, die der Assistent nicht selbst beantworten kann, werden über unseren Server an [Anbieter, z. B. Anthropic PBC, USA] übermittelt. Zweck, Rechtsgrundlage und Speicherdauer ergänzen.')}</p>

  <h2>8. YouTube, PayPal und weitere Links</h2>
  <p>Auf unseren Seiten sind keine YouTube-Videos eingebettet. Erst wenn du auf einen Link zu YouTube tippst, öffnet sich die Seite der Google Ireland Limited, und es gilt deren Datenschutzerklärung.</p>
  <p>Wenn du uns freiwillig unterstützt, wirst du zu PayPal (Europe) S.à r.l. et Cie, S.C.A., Luxemburg weitergeleitet. PayPal verarbeitet deine Zahlungsdaten. Wir erhalten Name, E-Mail-Adresse und Betrag zur Abwicklung (Art. 6 Abs. 1 lit. b und c DSGVO).</p>
  <p>Für die Erstellung des PDF-Tagebuchs werden alle nötigen Programmteile von unserem eigenen Webspace geladen. Nur wenn du eigene, lizenzierte Schriftdateien im Ordner „fonts“ hinterlegst, wird zusätzlich eine Programmbibliothek von jsDelivr geladen.</p>

  <h2>9. Deine Rechte</h2>
  <p>Du hast das Recht auf Auskunft, Berichtigung, Löschung, Einschränkung der Verarbeitung, Datenübertragbarkeit und Widerspruch sowie das Recht, erteilte Einwilligungen jederzeit zu widerrufen. Außerdem kannst du dich bei einer Datenschutz-Aufsichtsbehörde beschweren, zum Beispiel bei der Behörde deines Wohnorts.</p>

  <h2>10. Stand</h2>
  <p>22.10.2026</p>
</div></section>"""
    page("datenschutz/", "de", "Datenschutzerklärung | NagelNEU", "Datenschutzerklärung von NagelNEU: keine Cookies, kein Tracking, App-Daten bleiben auf deinem Gerät.", body, robots="noindex, follow")


def not_found():
    """404-Seite: GitHub Pages liefert sie für alle unbekannten Pfade aus, darum mit festem Basispfad."""
    b = BASE_PATH
    doc = f"""<!DOCTYPE html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Seite nicht gefunden | NagelNEU</title>
<meta name="robots" content="noindex">
<script>/* Basispfad aus der Adresse: /nagelNEU/ oder /nagelneu/ auf GitHub Pages, sonst / (eigene Domain) */
(function(){{var seg=location.pathname.split('/')[1]||'';var b=seg.toLowerCase()==='nagelneu'?'/'+seg+'/':'/';document.write('<base href="'+b+'">')}})();</script>
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="assets/css/site.css">
<script>/* Alte Links mit #tagebuch führen in die App */
if(/^#tagebuch/i.test(location.hash))location.replace('app/'+location.search+location.hash);</script>
</head>
<body>
<main id="main">
<section class="hero"><div class="narrow center">
  <p><a class="logo" href="./" style="justify-content:center">{LOGO_SVG}<span class="brand-mark">Nagel<b>NEU</b></span></a></p>
  <img src="assets/img/knibbler-1.svg" alt="" width="96" height="128" style="margin:24px auto">
  <h1>Diese Seite gibt es nicht.</h1>
  <p class="lead">Vielleicht hat sich die Adresse geändert. Hier geht es weiter:</p>
  <div class="btn-row" style="justify-content:center">
    <a class="btn btn-primary" href="./">Zur Startseite</a>
    <a class="btn btn-secondary" href="app/">App öffnen</a>
  </div>
  <p class="small mute" style="margin-top:24px" lang="en">Page not found. <a href="en/">English home page</a></p>
</div></section>
</main>
</body>
</html>
"""
    with open(os.path.join(ROOT, "404.html"), "w", encoding="utf-8") as f:
        f.write(doc)


def build_misc():
    worksheet("de")
    worksheet("en")
    impressum()
    datenschutz()
    not_found()
