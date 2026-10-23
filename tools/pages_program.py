"""Unterseiten: 21-Tage-Programm und HÄNDE-STOPP-Methode."""
from site_base import E, SITE, YT_URL, img, page, breadcrumb_ld
from pages_home import overview, exercise


def program_de():
    path, r = "21-tage-programm/", "../"
    body = f"""
<section class="hero" style="padding-bottom:40px">
  <div class="narrow">
    <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="../">Start</a><span aria-hidden="true">›</span>21-Tage-Programm</nav>
    <span class="eyebrow">Das Programm</span>
    <h1>Das 21-Tage-Programm gegen Nägelkauen</h1>
    <p class="lead">Drei Wochen, jeden Tag etwa fünf Minuten: Du lernst deine Auslöser kennen, übst die HÄNDE-STOPP-Methode und dokumentierst, was sich verändert. Kostenlos, im Browser, auf Deutsch und Englisch.</p>
    <div class="btn-row"><a class="btn btn-primary" href="../app/">Meine 21 Tage entdecken</a><a class="btn btn-secondary" href="../haende-stopp/">Erst die Methode ansehen</a></div>
  </div>
</section>

<section class="sec-tight">
  <div class="narrow prose">
    <div class="toc"><strong>Auf dieser Seite</strong><ol>
      <li><a href="#fuer-wen">Für wen das Programm gedacht ist</a></li>
      <li><a href="#tag">So läuft ein Tag ab</a></li>
      <li><a href="#werkzeuge">Die Werkzeuge</a></li>
      <li><a href="#uebersicht">Die 21 Tage im Überblick</a></li>
      <li><a href="#erwartung">Was du realistisch erwarten kannst</a></li>
      <li><a href="#grenzen">Grenzen und Sicherheit</a></li>
      <li><a href="#daten">Deine Daten</a></li>
    </ol></div>

    <h2 id="fuer-wen">Für wen das Programm gedacht ist</h2>
    <ul class="check-list">
      <li>Für Erwachsene, die schon länger Nägel kauen oder an der Nagelhaut knibbeln.</li>
      <li>Für alle, die es verändern möchten, ohne sich dafür schlecht zu fühlen.</li>
      <li>Für Menschen, die oft erst hinterher merken, dass sie gekaut haben.</li>
      <li>Für alle, die einen konkreten Plan wollen statt guter Vorsätze.</li>
    </ul>
    <p><strong>Weniger geeignet</strong> ist NagelNEU als alleinige Hilfe, wenn deine Nagelbetten häufig entzündet sind, du sehr unter dem Kauen leidest oder es mit Ängsten oder Zwängen zusammenhängt. Dann ist ärztliche oder psychotherapeutische Unterstützung der bessere erste Schritt. Für Kinder ist das Programm nicht gedacht.</p>

    <h2 id="tag">So läuft ein Tag ab</h2>
    <p>Jeder Tag hat denselben, kurzen Ablauf. Das macht ihn leicht in den Alltag einzubauen.</p>
    <ol>
      <li><strong>Die Ausrede:</strong> Ein Knibbler, eine kleine Fingerfigur, sagt einen typischen Satz, der zum Kauen verleitet, zum Beispiel „Nur die eine Kante“.</li>
      <li><strong>Die Wahrheit:</strong> Du liest, was in solchen Momenten tatsächlich passiert und was stattdessen hilft.</li>
      <li><strong>Zwei Fragen:</strong> Kurze Fragen, die mitlernen. Was du falsch beantwortest, kommt später noch einmal.</li>
      <li><strong>Die Tagesaufgabe:</strong> Eine konkrete Mission für heute, zum Beispiel ein Hände-Täschchen packen oder einen Wenn-dann-Satz schreiben.</li>
      <li><strong>Das Tagebuch:</strong> Ein paar Zeilen schreiben oder einsprechen. Zahlen wie „heute dreimal ertappt“ trägt die App aus deiner Sprache automatisch ein.</li>
    </ol>
    <p>Dazwischen nutzt du im Alltag zwei Knöpfe: <strong>„Ertappt!“</strong>, wenn du merkst, dass die Hand zum Mund will, und den <strong>60-Sekunden-HÄNDE-STOPP</strong>, wenn der Drang stark ist.</p>

    <h2 id="werkzeuge">Die Werkzeuge</h2>
    <ul>
      <li><strong>Ertappt-Zähler mit Tagesziel:</strong> Du siehst, wie oft du dich rechtzeitig stoppst. Das Tagesziel für „doch gekaut“ sinkt von Tag zu Tag.</li>
      <li><strong>HÄNDE-STOPP:</strong> Eine geführte Minute nach dem HÄNDE-STOPP-Ablauf, vorher und nachher mit Einschätzung des Drangs.</li>
      <li><strong>Tagebuch mit Spracheingabe:</strong> Schreiben, abhaken, einsprechen. Alles bleibt auf deinem Gerät.</li>
      <li><strong>Foto-Tage:</strong> An Tag 1, 7, 14 und 21 fotografierst du deine Hände, für den eigenen Vorher-Nachher-Vergleich.</li>
      <li><strong>Gefahrenradar:</strong> Zeigt aus deinen Einträgen, zu welchen Uhrzeiten es dich am häufigsten erwischt.</li>
      <li><strong>Notfallkarte und Hände-Plan:</strong> Zum Ausdrucken, mit deinen Auslösern und Wenn-dann-Sätzen.</li>
      <li><strong>PDF-Tagebuch:</strong> Am Ende hast du alles in einem Dokument, inklusive deiner Sprachnotizen als Dateien.</li>
      <li><strong>Chat-Assistent:</strong> Beantwortet Fragen rund ums Programm und ums Nägelkauen.</li>
    </ul>
  </div>
</section>

<section id="uebersicht" class="bg-2">
  <div class="wrap">
    <span class="eyebrow">Übersicht</span>
    <h2>Die 21 Tage im Überblick</h2>
    <p class="lead">Die festen Tage sind für alle gleich. An den Auslöser-Tagen trainierst du mit dem Knibbler, der zu deinen drei wichtigsten Auslösern gehört: erst entlarven, dann einen Gegenplan bauen, dann den Ernstfall üben.</p>
    {overview('de')}
  </div>
</section>

<section class="sec-tight">
  <div class="narrow prose">
    <h2 id="erwartung">Was du realistisch erwarten kannst</h2>
    <p>21 Tage sind eine Übungsphase und ein gutes Fundament, aber keine Garantie. In den ersten Tagen geht es vor allem darum, deine Momente früher zu bemerken. Das ist der wichtigste Schritt. Wie schnell das Kauen seltener wird, ist sehr unterschiedlich, und Rückschritte gehören dazu.</p>
    <p>Fingernägel wachsen im Durchschnitt etwa drei Millimeter im Monat. Sichtbare Veränderungen brauchen also Zeit, und es lohnt sich, nach den 21 Tagen dranzubleiben. Dafür gibt es in der App einen Dranbleiben-Pfad bis Tag 90.</p>

    <h2 id="grenzen">Grenzen und Sicherheit</h2>
    <p>NagelNEU ist ein Selbsthilfe-Begleiter und kein Medizinprodukt. Das Programm stellt keine Diagnosen und ersetzt keine Behandlung. Bitte hol dir ärztliche Hilfe, wenn Nagelbett oder Haut gerötet, geschwollen oder eitrig sind. Wenn du sehr unter dem Kauen leidest oder es mit Ängsten oder Zwängen verbunden ist, kann eine Verhaltenstherapie helfen. In einer seelischen Krise erreichst du die TelefonSeelsorge rund um die Uhr unter 0800 111 0 111, im Notfall wähle 112.</p>

    <h2 id="daten">Deine Daten</h2>
    <p>Profil, Tagebuch, Fotos und Sprachnotizen werden nur lokal in deinem Browser gespeichert. Sie werden nicht an NagelNEU übertragen. Wenn du Browserdaten löschst oder das Gerät wechselst, sind sie weg, außer du hast sie vorher unter „Ich“ gesichert. Mehr dazu in der <a href="../datenschutz/">Datenschutzerklärung</a>.</p>
    <div class="btn-row" style="margin-top:32px"><a class="btn btn-primary" href="../app/">Meine 21 Tage entdecken</a><a class="btn btn-secondary" href="../arbeitsblatt/">Arbeitsblatt drucken</a></div>
  </div>
</section>
"""
    ld = [
        {"@type": "WebPage", "url": SITE + path, "name": "Das 21-Tage-Programm gegen Nägelkauen", "inLanguage": "de-DE", "isPartOf": {"@id": SITE + "#website"}, "dateModified": "2026-10-22"},
        breadcrumb_ld([("Start", ""), ("21-Tage-Programm", path)]),
    ]
    page(path, "de", "21-Tage-Programm gegen Nägelkauen | NagelNEU",
         "So funktioniert das kostenlose 21-Tage-Programm von NagelNEU: täglicher Ablauf, Werkzeuge, alle 21 Tage im Überblick, realistische Erwartungen und Grenzen.",
         body, active="21-tage-programm/", ld=ld)


def method_de():
    path, r = "haende-stopp/", "../"
    ifthen = [
        ("Stress", "Wenn Druck aufkommt, balle ich die Fäuste, lege die Hände flach auf die Oberschenkel und atme eine Minute lang 4 Sekunden ein und 6 Sekunden aus."),
        ("Langeweile", "Wenn ich warte oder mich langweile, nehme ich den Knetball oder Drehring in die Hand."),
        ("Bildschirm", "Wenn ich eine Serie oder ein Spiel starte, creme ich zuerst die Hände ein und halte etwas in der Hand."),
        ("Konzentration", "Wenn ich mich an den Schreibtisch setze, liegt ein Stift oder Drehring in meiner Denkhand."),
        ("Kanten", "Wenn ich eine Kante oder abstehende Nagelhaut spüre, nehme ich die Feile, nie die Zähne."),
        ("Unterwegs", "Wenn ich an der Ampel stehe oder unterwegs warte, lege ich beide Hände ans Lenkrad oder nehme meinen Knetball."),
    ]
    rows = "".join(f'<li><strong>{E(k)}:</strong> „{E(v)}“</li>' for k, v in ifthen)
    body = f"""
<section class="hero" style="padding-bottom:40px">
  <div class="narrow">
    <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="../">Start</a><span aria-hidden="true">›</span>HÄNDE-STOPP-Methode</nav>
    <span class="eyebrow">Die Methode</span>
    <h1>HÄNDE-STOPP: Übungen gegen automatisches Nägelkauen</h1>
    <p class="lead">Nägelkauen passiert oft schneller, als du denken kannst. HÄNDE-STOPP gibt dir für genau diesen Moment einen kurzen, festen Ablauf in vier Schritten, ohne Hilfsmittel und in etwa einer Minute.</p>
  </div>
</section>

<section class="sec-tight">
  <div class="narrow prose">
    <div class="toc"><strong>Auf dieser Seite</strong><ol>
      <li><a href="#warum">Warum ein fester Ablauf hilft</a></li>
      <li><a href="#schritte">Die vier Schritte</a></li>
      <li><a href="#ueben">Die 60-Sekunden-Übung zum Mitmachen</a></li>
      <li><a href="#alternativen">Alternativen für deine Hände</a></li>
      <li><a href="#wenn-dann">Wenn-dann-Sätze</a></li>
      <li><a href="#stolpersteine">Typische Stolpersteine</a></li>
    </ol></div>

    <h2 id="warum">Warum ein fester Ablauf hilft</h2>
    <p>Gewohnheiten laufen nach einem Muster: Eine Situation löst eine Bewegung aus, und die Bewegung bringt kurz Erleichterung. Je öfter das passiert, desto automatischer wird es. Ein Vorsatz wie „Ich kaue nicht mehr“ kommt in diesem Moment oft zu spät.</p>
    <p>Ein fester Ablauf funktioniert anders. Du übst ihn so lange, bis er von selbst greift, wenn die Hand zum Mund will. HÄNDE-STOPP greift dafür Elemente auf, die auch in der Verhaltenstherapie bei Gewohnheiten wie dem Nägelkauen genutzt werden: den Moment bewusst wahrnehmen und eine Gegenbewegung einsetzen, die mit Kauen nicht zusammenpasst. Die Methode selbst ist eine praktische Übungsstruktur und kein medizinisch geprüftes Verfahren.</p>

    <h2 id="schritte">Die vier Schritte</h2>
    <h3>1. Wahrnehmen: Was passiert gerade?</h3>
    <p>Bemerke die Bewegung und benenne sie innerlich: „Meine Hand will zum Mund.“ Am Anfang bemerkst du es oft erst hinterher. Das zählt trotzdem, denn jedes Bemerken trainiert deine Aufmerksamkeit. Hilfreich sind spürbare Erinnerungen wie ein Pflaster am Lieblingsfinger, ein Ring oder Bitterlack.</p>
    <h3>2. Innehalten: Kann ich kurz unterbrechen?</h3>
    <p>Balle die Fäuste 3 Sekunden fest, löse sie und lege die Hände flach auf die Oberschenkel oder den Tisch. Atme dabei 4 Sekunden ein und 6 Sekunden aus, etwa eine Minute lang. Fäuste und flache Hände können nicht gleichzeitig kauen. Der Drang wird in dieser Zeit meist schwächer.</p>
    <h3>3. Alternative wählen: Was können meine Hände stattdessen tun?</h3>
    <p>Gib den Händen eine Aufgabe, die zur Situation passt: etwas halten, drücken oder pflegen. Am besten legst du sie vorher fest und hast das Nötige griffbereit.</p>
    <h3>4. Reflektieren: Was habe ich bemerkt?</h3>
    <p>Nimm dir ein paar Sekunden: Wo warst du, was hat es ausgelöst, was hat geholfen? Ein Wort im Tagebuch reicht. Nach einigen Tagen erkennst du dein Muster und kannst dich gezielt vorbereiten.</p>
  </div>
</section>

<section id="ueben" class="night">
  <div class="wrap">
    <span class="eyebrow">Zum Mitmachen</span>
    <h2>Die 60-Sekunden-Übung</h2>
    <p class="lead">Wähle deine Situation und mach die Minute direkt mit. Es wird nichts gespeichert.</p>
    {exercise('de', '../arbeitsblatt/', '../')}
  </div>
</section>

<section class="sec-tight">
  <div class="narrow prose">
    <h2 id="alternativen">Alternativen für deine Hände</h2>
    <p>Nicht jede Alternative passt in jede Situation. Such dir für deine häufigsten Momente je eine aus.</p>
    <ul>
      <li><strong>Halten:</strong> Stift, Drehring, Schlüsselbund, Tasse, Wasserflasche.</li>
      <li><strong>Drücken:</strong> Knetball, Antistressball, die Hände fest gegeneinander drücken.</li>
      <li><strong>Pflegen:</strong> Handcreme einmassieren, Nagelöl, raue Kanten sofort feilen.</li>
      <li><strong>Beschäftigen:</strong> Kritzeln, ein kleines Fingerspielzeug, Hände unter den Oberschenkeln oder in den Jackentaschen.</li>
      <li><strong>Erschweren:</strong> Pflaster am Lieblingsfinger, Bitterlack, kurz geschnittene und glatt gefeilte Nägel.</li>
    </ul>
    <p>Lege an jeden Ort, an dem du oft kaust, eine Feile und etwas für die Hände: Tasche, Schreibtisch, Auto, Sofa, Nachttisch.</p>

    <h2 id="wenn-dann">Wenn-dann-Sätze</h2>
    <p>Ein Wenn-dann-Satz legt vorher fest, was du in deiner typischen Situation tust. So musst du im entscheidenden Moment nicht überlegen. Beispiele:</p>
    <ul>{rows}</ul>
    <p>Schreib dir für deine zwei häufigsten Situationen einen eigenen Satz auf, zum Beispiel auf dem <a href="../arbeitsblatt/">Arbeitsblatt</a>.</p>

    <h2 id="stolpersteine">Typische Stolpersteine</h2>
    <ul>
      <li><strong>„Nur die eine Kante.“</strong> Der gefährlichste Satz. Die Antwort ist immer die Feile.</li>
      <li><strong>„Jetzt ist eh alles egal.“</strong> Nach einem Ausrutscher kommt oft dieser Gedanke. Nagel glatt feilen, eincremen, weitermachen.</li>
      <li><strong>Zu viel auf einmal.</strong> Starte mit Schritt 1. Wer zuverlässig bemerkt, hat schon viel gewonnen.</li>
      <li><strong>Alternative nicht griffbereit.</strong> Was du suchen musst, nutzt du im Ernstfall nicht.</li>
    </ul>
    <div class="btn-row" style="margin-top:32px"><a class="btn btn-primary" href="../app/">Im 21-Tage-Programm üben</a><a class="btn btn-secondary" href="../arbeitsblatt/">Arbeitsblatt drucken</a></div>
    <div class="sources">
      <h2>Quellen und weiterführende Informationen</h2>
      <ul>
        <li><a href="https://www.onmeda.de/krankheiten/fingernaegel-kauen-id202497/" rel="noopener" target="_blank">Onmeda: Fingernägel kauen (Onychophagie)</a>, medizinisch geprüft, Stand 12.12.2022</li>
        <li><a href="https://www.psychologytoday.com/us/conditions/onychophagia-nail-biting" rel="noopener" target="_blank">Psychology Today: Onychophagia (Nail Biting)</a>, englisch</li>
      </ul>
    </div>
  </div>
</section>
"""
    ld = [
        {"@type": "WebPage", "url": SITE + path, "name": "HÄNDE-STOPP: Übungen gegen automatisches Nägelkauen", "inLanguage": "de-DE", "isPartOf": {"@id": SITE + "#website"}, "dateModified": "2026-10-22"},
        breadcrumb_ld([("Start", ""), ("HÄNDE-STOPP-Methode", path)]),
    ]
    page(path, "de", "HÄNDE-STOPP: Übungen gegen Nägelkauen | NagelNEU",
         "HÄNDE-STOPP in vier Schritten: wahrnehmen, innehalten, Alternative wählen, reflektieren. Mit 60-Sekunden-Übung, Alternativen für die Hände und Wenn-dann-Sätzen.",
         body, active="haende-stopp/", ld=ld)
