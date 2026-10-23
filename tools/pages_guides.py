"""Ratgeberseiten (Deutsch)."""
from site_base import E, SITE, AUTHOR, UPDATED, img, page, breadcrumb_ld

SOURCES = """<div class="sources">
  <h2>Quellen und weiterführende Informationen</h2>
  <ul>
    <li><a href="https://www.onmeda.de/krankheiten/fingernaegel-kauen-id202497/" rel="noopener" target="_blank">Onmeda: Fingernägel kauen (Onychophagie)</a>, medizinisch geprüft, Stand 12.12.2022</li>
    <li><a href="https://www.psychologytoday.com/us/conditions/onychophagia-nail-biting" rel="noopener" target="_blank">Psychology Today: Onychophagia (Nail Biting)</a>, englisch</li>
  </ul>
  <p>Dieser Ratgeber ersetzt keine ärztliche oder psychotherapeutische Beratung. Stand: 22.10.2026.</p>
</div>"""

RELATED = {
    "naegelkauen-abgewoehnen/": ("Nägelkauen abgewöhnen", "Sechs Schritte, die Erwachsenen wirklich helfen."),
    "warum-kaue-ich-naegel/": ("Warum kaue ich Nägel?", "Häufige Auslöser und was dahintersteckt."),
    "naegelkauen-bei-stress/": ("Nägelkauen bei Stress", "Sofort-Übung und Vorbereitung für den Alltag."),
    "haende-stopp/": ("Die HÄNDE-STOPP-Methode", "Vier Schritte und eine Übung zum Mitmachen."),
    "21-tage-programm/": ("Das 21-Tage-Programm", "Ablauf, Inhalte und Grenzen im Überblick."),
}


def author_box(r):
    return f"""<div class="author-box">{img(r, 'knibbler-2.svg', '', 56, 75)}<div><strong>Von {AUTHOR}</strong><br>
<span class="mute">Gründer von NagelNEU. Er kennt das Nägelkauen aus eigener Erfahrung. Auf YouTube teilt er Übungen unter @fingernägelkauen.</span></div></div>"""


def related(r, current):
    cards = "".join(
        f'<a class="card" href="{r}{p}"><h3>{E(t)}</h3><p>{E(d)}</p><span class="arrow-link">Lesen</span></a>'
        for p, (t, d) in RELATED.items() if p != current
    )[:]
    return f"""<section class="bg-2 sec-tight"><div class="wrap"><h2 style="font-size:var(--step-2)">Weiterlesen</h2><div class="related">{cards}</div></div></section>"""


def cta(r):
    return f"""<div class="card" style="margin-top:40px;background:var(--rose-soft);border-color:transparent">
<h3>Üben statt nur lesen</h3>
<p>Im kostenlosen 21-Tage-Programm übst du die HÄNDE-STOPP-Methode jeden Tag etwa fünf Minuten, mit Tagebuch, Foto-Tagen und Hilfe für akute Momente.</p>
<div class="btn-row"><a class="btn btn-primary" href="{r}app/">Meine 21 Tage entdecken</a><a class="arrow-link" href="{r}haende-stopp/#ueben">60-Sekunden-Übung testen</a></div></div>"""


def guide(path, title, desc, h1, lead, toc, content):
    r = "../"
    toc_html = "".join(f'<li><a href="#{a}">{E(t)}</a></li>' for a, t in toc)
    body = f"""
<section class="hero" style="padding-bottom:24px">
  <div class="narrow">
    <nav class="breadcrumb" aria-label="Brotkrümelnavigation"><a href="../">Start</a><span aria-hidden="true">›</span>Ratgeber<span aria-hidden="true">›</span>{E(RELATED[path][0])}</nav>
    <span class="eyebrow">Ratgeber</span>
    <h1>{E(h1)}</h1>
    <p class="lead">{lead}</p>
    <p class="small mute">Von {AUTHOR} · Aktualisiert am 22.10.2026</p>
  </div>
</section>
<section class="sec-tight" style="padding-top:0">
  <article class="narrow prose">
    <div class="toc"><strong>Inhalt</strong><ol>{toc_html}</ol></div>
    {content}
    {cta(r)}
    {author_box(r)}
    {SOURCES}
  </article>
</section>
{related(r, path)}
"""
    ld = [
        {"@type": "Article", "headline": h1, "description": desc, "inLanguage": "de-DE", "url": SITE + path,
         "mainEntityOfPage": SITE + path, "image": SITE + "assets/img/og-image.png",
         "datePublished": UPDATED, "dateModified": UPDATED,
         "author": {"@type": "Person", "name": AUTHOR, "url": SITE},
         "publisher": {"@id": SITE + "#org"}},
        breadcrumb_ld([("Start", ""), (RELATED[path][0], path)]),
    ]
    page(path, "de", title, desc, body, active="naegelkauen-abgewoehnen/" if path == "naegelkauen-abgewoehnen/" else None,
         ld=ld, og_type="article")


def abgewoehnen():
    content = """
<p>Fast alle, die lange Nägel kauen, haben es schon mit Vorsätzen versucht. Dass es damit oft nicht klappt, hat nichts mit fehlender Disziplin zu tun. Nägelkauen ist meist so eingeübt, dass die Hand schneller ist als der Gedanke. Was hilft, ist deshalb weniger „sich zusammenreißen“ als ein Plan für genau diesen Moment.</p>

<h2 id="willenskraft">Warum Willenskraft allein selten reicht</h2>
<p>Eine Gewohnheit besteht aus drei Teilen: einer Situation, einer Handlung und einer kurzen Belohnung. Beim Nägelkauen ist die Situation zum Beispiel Stress, Langeweile oder eine raue Kante, die Handlung der Griff zum Mund und die Belohnung ein kurzer Moment von Entlastung oder Beschäftigung. Weil das sehr oft wiederholt wurde, läuft es fast ohne Nachdenken ab.</p>
<p>Ein Vorsatz greift erst, wenn du dich bewusst daran erinnerst. Bis dahin ist der Nagel oft schon im Mund. Darum setzen die folgenden Schritte früher an.</p>

<h2 id="muster">Schritt 1: Dein Muster kennenlernen</h2>
<p>Beobachte ein paar Tage, ohne etwas ändern zu müssen. Notiere jedes Mal kurz:</p>
<ul>
  <li>Wo warst du, und was hast du gerade gemacht?</li>
  <li>Wie hast du dich gefühlt: angespannt, gelangweilt, konzentriert, nervös?</li>
  <li>Hast du es vorher, währenddessen oder erst hinterher bemerkt?</li>
</ul>
<p>Nach wenigen Tagen zeigen sich meist zwei oder drei typische Situationen. Genau dort setzt du an. Eine Vorlage dafür findest du auf dem <a href="../arbeitsblatt/">Arbeitsblatt zum Ausdrucken</a>.</p>

<h2 id="bemerken">Schritt 2: Früher bemerken</h2>
<p>Je früher du die Bewegung bemerkst, desto leichter kannst du sie unterbrechen. Spürbare Erinnerungen helfen dabei:</p>
<ul>
  <li>ein Pflaster am Finger, an dem du am häufigsten kaust,</li>
  <li>ein Ring, den du bewusst wahrnimmst,</li>
  <li>Bitterlack aus der Apotheke, der den Geschmack unangenehm macht.</li>
</ul>
<p>Wichtig ist die Haltung: Jedes Bemerken ist ein Erfolg, auch wenn es erst hinterher passiert. Ärger über dich selbst macht es nicht leichter.</p>

<h2 id="gegenbewegung">Schritt 3: Eine Gegenbewegung üben</h2>
<p>Sobald du es merkst, brauchst du etwas, das deine Hände sofort tun können und das mit Kauen nicht zusammenpasst. Bewährt hat sich ein kurzer Ablauf: Fäuste 3 Sekunden fest ballen, lösen, Hände flach auf die Oberschenkel legen und dabei 4 Sekunden ein- und 6 Sekunden ausatmen. Nach etwa einer Minute ist der Drang meist deutlich schwächer.</p>
<p>Diesen Ablauf nennen wir <a href="../haende-stopp/">HÄNDE-STOPP</a>. Er besteht aus vier Schritten: wahrnehmen, innehalten, Alternative wählen und reflektieren. Üb ihn auch in ruhigen Momenten, dann ist er in schwierigen schneller abrufbar.</p>

<h2 id="umgebung">Schritt 4: Deine Umgebung vorbereiten</h2>
<ul>
  <li><strong>Nägel kurz und glatt halten.</strong> Raue Kanten sind eine der häufigsten Einladungen.</li>
  <li><strong>Feilen verteilen:</strong> Tasche, Schreibtisch, Auto, Sofa, Nachttisch.</li>
  <li><strong>Handcreme griffbereit:</strong> Weiche Nagelhaut lädt weniger zum Knibbeln ein.</li>
  <li><strong>Etwas für die Hände:</strong> Knetball, Drehring oder Stift an den Orten, an denen du am häufigsten kaust.</li>
</ul>

<h2 id="unterstuetzung">Schritt 5: Unterstützung ohne Kommentare</h2>
<p>Viele Menschen kauen seit Jahren, und Bemerkungen wie „Lass das!“ lösen eher Scham aus als Veränderung. Besser ist ein vereinbartes, freundliches Zeichen: Eine vertraute Person tippt sich zum Beispiel kurz an die eigene Hand, wenn sie dich kauen sieht. Du antwortest mit einem einfachen „Danke“.</p>

<h2 id="rueckfall">Schritt 6: Mit Ausrutschern umgehen</h2>
<p>Ausrutscher gehören dazu. Gefährlich ist weniger der einzelne Moment als der Gedanke danach: „Jetzt ist eh alles egal.“ Leg dir deshalb vorher fest, was du tust:</p>
<ol>
  <li>Hände runter, kurz durchatmen.</li>
  <li>Den Nagel sofort glatt feilen und eincremen, damit keine Kante lockt.</li>
  <li>Notieren, was der Auslöser war.</li>
  <li>Beim nächsten Moment wieder mit Schritt 1 beginnen.</li>
</ol>

<h2 id="dauer">Wie lange dauert es?</h2>
<p>Darauf gibt es keine allgemeingültige Antwort. Manche kauen schon nach wenigen Wochen deutlich seltener, bei anderen dauert es länger, und Rückschritte sind normal. Fingernägel wachsen im Durchschnitt etwa drei Millimeter im Monat. Bis ein Nagel vollständig nachgewachsen ist, vergehen meist mehrere Monate. Es lohnt sich also, auch nach den ersten Erfolgen dranzubleiben.</p>
<p>Ein strukturierter Zeitraum wie das <a href="../21-tage-programm/">21-Tage-Programm</a> hilft, die neuen Abläufe regelmäßig zu üben. Er ist eine Übungsphase, keine Garantie.</p>

<h2 id="hilfe">Wann du dir Hilfe holen solltest</h2>
<p>Sprich mit deiner Hausärztin oder deinem Hausarzt, wenn Nagelbett oder Haut gerötet, geschwollen oder eitrig sind, wenn es häufig blutet oder wenn du sehr unter dem Kauen leidest. Hängt das Kauen mit Ängsten, Zwängen oder anhaltender Niedergeschlagenheit zusammen, kann eine Verhaltenstherapie helfen. Laut Onmeda wird für ausgeprägte Fälle ein Training empfohlen, bei dem man Auslöser erkennt und Ersatzhandlungen wie festes Faustschließen übt.</p>
"""
    guide("naegelkauen-abgewoehnen/",
          "Nägelkauen abgewöhnen: 6 Schritte für Erwachsene | NagelNEU",
          "Nägelkauen abgewöhnen als Erwachsener: Muster erkennen, früher bemerken, Gegenbewegung üben und mit Ausrutschern umgehen. Praktisch und ohne Scham.",
          "Nägelkauen abgewöhnen: Was Erwachsenen wirklich hilft",
          "Sechs praktische Schritte, die nicht auf Willenskraft setzen, sondern auf einen Plan für den automatischen Moment. Ohne Scham und ohne falsche Versprechen.",
          [("willenskraft", "Warum Willenskraft allein selten reicht"), ("muster", "Schritt 1: Dein Muster kennenlernen"), ("bemerken", "Schritt 2: Früher bemerken"),
           ("gegenbewegung", "Schritt 3: Eine Gegenbewegung üben"), ("umgebung", "Schritt 4: Deine Umgebung vorbereiten"), ("unterstuetzung", "Schritt 5: Unterstützung ohne Kommentare"),
           ("rueckfall", "Schritt 6: Mit Ausrutschern umgehen"), ("dauer", "Wie lange dauert es?"), ("hilfe", "Wann du dir Hilfe holen solltest")],
          content)


def warum():
    content = """
<p>Die meisten, die Nägel kauen, haben sich diese Frage schon oft gestellt. Eine einzige Antwort gibt es selten. Häufig kommen mehrere Gründe zusammen, und sie können sich je nach Situation unterscheiden. Die gute Nachricht: Du musst den einen Grund nicht finden, um etwas zu verändern. Es reicht, deine typischen Momente zu kennen.</p>

<h2 id="haeufig">Wie häufig ist Nägelkauen?</h2>
<p>Nägelkauen ist weit verbreitet. Nach Schätzungen, die Onmeda zitiert, knabbern etwa 30 von 100 Kindern und 45 von 100 Jugendlichen an ihren Fingernägeln. Bei vielen hört es von allein auf, bei manchen bleibt es bis ins Erwachsenenalter. Männer und Frauen sind etwa gleich häufig betroffen. Du bist damit also alles andere als allein.</p>

<h2 id="schleife">Die Gewohnheitsschleife</h2>
<p>Nägelkauen folgt meist einem einfachen Muster:</p>
<ol>
  <li><strong>Auslöser:</strong> eine Situation oder ein Gefühl, zum Beispiel Anspannung, Langeweile oder eine raue Kante.</li>
  <li><strong>Handlung:</strong> Die Hand geht zum Mund, oft ohne dass du es bemerkst.</li>
  <li><strong>Kurze Wirkung:</strong> Für einen Moment fühlt es sich entlastend, beschäftigend oder „glatter“ an.</li>
</ol>
<p>Weil die Wirkung sofort eintritt, verstärkt sich die Schleife mit jeder Wiederholung. Die Nachteile, also Schmerzen, Entzündungen oder Scham, kommen dagegen später und unterbrechen das Muster kaum.</p>

<h2 id="ausloeser">Häufige Auslöser</h2>
<ul>
  <li><strong>Stress und Anspannung:</strong> Druck bei der Arbeit, schwierige Gespräche, Termine. Mehr dazu im Ratgeber <a href="../naegelkauen-bei-stress/">Nägelkauen bei Stress</a>.</li>
  <li><strong>Langeweile und Warten:</strong> Die Hände haben nichts zu tun.</li>
  <li><strong>Konzentration:</strong> Beim Lesen, Lernen oder Nachdenken arbeitet die Hand allein weiter.</li>
  <li><strong>Bildschirmzeit:</strong> Serien, Spiele, Scrollen.</li>
  <li><strong>Nervosität:</strong> vor Prüfungen, Terminen oder Auftritten.</li>
  <li><strong>Raue Kanten und Nagelhaut:</strong> Eine kleine Unebenheit, die „nur kurz“ glatt gemacht werden soll.</li>
  <li><strong>Starke Gefühle:</strong> Frust, Ärger oder Traurigkeit.</li>
</ul>
<p>Manche kauen bewusst, andere fast immer unbewusst. Beides ist häufig und lässt sich verändern.</p>

<h2 id="krankheit">Ist Nägelkauen eine Krankheit?</h2>
<p>Gelegentliches Nägelkauen ist in erster Linie eine Gewohnheit. Fachleute zählen häufiges, schwer kontrollierbares Nägelkauen zu den körperbezogenen, sich wiederholenden Verhaltensweisen. Ob daraus eine behandlungsbedürftige Störung wird, hängt unter anderem davon ab, wie stark du darunter leidest, ob es deinen Alltag beeinträchtigt und ob mehrere Versuche, aufzuhören, gescheitert sind.</p>
<p>Nägelkauen kann außerdem gemeinsam mit anderen Themen auftreten, zum Beispiel mit Ängsten oder Aufmerksamkeitsproblemen. Wenn du dich darin wiedererkennst oder unsicher bist, ist ein Gespräch mit deiner Hausärztin oder deinem Hausarzt ein guter erster Schritt.</p>

<h2 id="selbsttest">Dein Muster in fünf Fragen</h2>
<ol>
  <li>In welchen zwei oder drei Situationen kaust du am häufigsten?</li>
  <li>Zu welcher Tageszeit passiert es öfter?</li>
  <li>Bemerkst du es vorher, währenddessen oder erst hinterher?</li>
  <li>Welche Finger oder Stellen sind besonders betroffen?</li>
  <li>Was hast du in diesem Moment eigentlich gebraucht: Ruhe, Beschäftigung, Bewegung?</li>
</ol>
<p>Schreib die Antworten auf, zum Beispiel auf dem <a href="../arbeitsblatt/">Arbeitsblatt</a>. Sie sind die Grundlage für deinen persönlichen Plan.</p>

<h2 id="weiter">Was du jetzt tun kannst</h2>
<p>Wenn du deine Auslöser kennst, kannst du gezielt vorbereiten, was deine Hände stattdessen tun. Wie das geht, zeigt die <a href="../haende-stopp/">HÄNDE-STOPP-Methode</a>. Eine Übersicht über alle Schritte findest du im Ratgeber <a href="../naegelkauen-abgewoehnen/">Nägelkauen abgewöhnen</a>.</p>
"""
    guide("warum-kaue-ich-naegel/",
          "Warum kaue ich Nägel? Ursachen und Auslöser | NagelNEU",
          "Warum kaue ich Nägel? Die Gewohnheitsschleife, häufige Auslöser wie Stress, Langeweile und Konzentration, und wann Nägelkauen mehr als eine Gewohnheit ist.",
          "Warum kaue ich Nägel? Häufige Auslöser und was dahintersteckt",
          "Nägelkauen hat selten nur einen Grund. Hier erfährst du, wie die Gewohnheit funktioniert, welche Auslöser typisch sind und woran du dein eigenes Muster erkennst.",
          [("haeufig", "Wie häufig ist Nägelkauen?"), ("schleife", "Die Gewohnheitsschleife"), ("ausloeser", "Häufige Auslöser"),
           ("krankheit", "Ist Nägelkauen eine Krankheit?"), ("selbsttest", "Dein Muster in fünf Fragen"), ("weiter", "Was du jetzt tun kannst")],
          content)


def stress():
    content = """
<p>Stress ist einer der häufigsten Auslöser für Nägelkauen. Unter Druck sucht der Körper nach einem Ventil, und die Hand am Mund ist schnell und immer verfügbar. Die Erleichterung hält allerdings nur kurz. Danach kommen oft Schmerzen, Ärger über sich selbst und eine neue Anspannung.</p>

<h2 id="warum-stress">Warum gerade Stress zum Kauen führt</h2>
<p>In angespannten Momenten ist der Körper auf Aktivität eingestellt. Muskeln spannen sich an, die Atmung wird flacher, und die Hände suchen etwas zu tun. Nägelkauen ist eine sehr schnelle Art, diese Spannung kurz abzubauen. Gerade weil es so schnell geht, wird es leicht zur Gewohnheit.</p>

<h2 id="sofort">Die Sofort-Übung: HÄNDE-STOPP in einer Minute</h2>
<ol>
  <li><strong>Wahrnehmen:</strong> „Meine Hand will zum Mund.“ Achte kurz auf Schultern, Kiefer und Atem.</li>
  <li><strong>Innehalten:</strong> Fäuste 3 Sekunden fest ballen, lösen, Hände flach auf die Oberschenkel oder den Tisch.</li>
  <li><strong>Atmen:</strong> 4 Sekunden ein, 6 Sekunden aus, etwa eine Minute lang. Das längere Ausatmen hilft vielen, ruhiger zu werden.</li>
  <li><strong>Alternative wählen:</strong> Etwas zum Drücken in die Hand, zum Beispiel einen Knetball.</li>
  <li><strong>Reflektieren:</strong> Was hat den Stress ausgelöst? Ein Wort reicht.</li>
</ol>
<p>Du kannst die Minute auf der Seite zur <a href="../haende-stopp/#ueben">HÄNDE-STOPP-Methode</a> direkt mitmachen.</p>

<h2 id="vorbereiten">Sieben Wege, die Hände bei Stress zu beruhigen</h2>
<ol>
  <li><strong>Ein Schreibtisch-Set:</strong> Feile, Handcreme und etwas zum Drücken in Reichweite.</li>
  <li><strong>Nägel vor wichtigen Terminen feilen:</strong> Keine Kante, keine Einladung.</li>
  <li><strong>Hände im Meeting beschäftigen:</strong> Stift halten, Notizen machen, Hände flach auf den Tisch.</li>
  <li><strong>Beim Telefonieren:</strong> Die freie Hand hält etwas, zum Beispiel einen Drehring oder eine Tasse.</li>
  <li><strong>Kurze Pausen einplanen:</strong> Alle 25 bis 50 Minuten kurz aufstehen, Schultern lockern, Hände ausschütteln.</li>
  <li><strong>Einen Wenn-dann-Satz festlegen:</strong> „Wenn ich merke, dass der Druck steigt, balle ich die Fäuste und atme eine Minute lang langsam aus.“</li>
  <li><strong>Abends nachsorgen:</strong> Hände eincremen, Nagelhaut pflegen, den Tag kurz notieren.</li>
</ol>

<h2 id="langfristig">Langfristig: weniger Druck, weniger Anlässe</h2>
<p>Je weniger Dauerstress, desto seltener der Griff zum Mund. Ausreichend Schlaf, Bewegung und regelmäßige Pausen sind keine Wundermittel, aber sie senken bei vielen das Grundniveau an Anspannung. Wenn Stress dauerhaft sehr hoch ist oder mit Schlafproblemen, Ängsten oder Niedergeschlagenheit einhergeht, sprich bitte mit deiner Hausärztin oder deinem Hausarzt.</p>

<h2 id="rueckschlag">Wenn es doch passiert</h2>
<p>Gerade in stressigen Phasen kommen Ausrutscher vor. Feile den Nagel glatt, creme ein und mach weiter. Ein Ausrutscher sagt nichts darüber aus, ob du es schaffen kannst. Er zeigt dir nur, wo du dich noch besser vorbereiten kannst.</p>
"""
    guide("naegelkauen-bei-stress/",
          "Nägelkauen bei Stress: Sofort-Übung und 7 Wege | NagelNEU",
          "Nägelkauen bei Stress stoppen: eine Sofort-Übung für den akuten Moment und sieben praktische Wege, die Hände in Arbeit, Meetings und am Abend zu beruhigen.",
          "Nägelkauen bei Stress: So beruhigst du deine Hände",
          "Unter Druck geht die Hand besonders schnell zum Mund. Mit einer Sofort-Übung für den akuten Moment und etwas Vorbereitung im Alltag wird es seltener.",
          [("warum-stress", "Warum gerade Stress zum Kauen führt"), ("sofort", "Die Sofort-Übung"), ("vorbereiten", "Sieben Wege, die Hände zu beruhigen"),
           ("langfristig", "Langfristig: weniger Druck"), ("rueckschlag", "Wenn es doch passiert")],
          content)


def build_guides():
    abgewoehnen()
    warum()
    stress()
