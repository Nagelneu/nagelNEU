"""Startseite (Deutsch) und Homepage (English)."""
import json
import os
from site_base import E, ROOT, SITE, YT_URL, YT_NAME, img, page, rel, breadcrumb_ld

with open(os.path.join(ROOT, "tools", "program.json"), encoding="utf-8") as _f:
    PROG = json.load(_f)
PHOTO_DAYS = {1, 7, 14, 21}

T = {
    "de": {
        "phase_desc": [
            "Muster erkennen, Ausreden durchschauen, ertappen lernen.",
            "Gegenreaktion üben, Hände beschäftigen, Verbündete finden.",
            "Schwierige Situationen, Gefühle und Ausrutscher vorbereiten.",
            "Neues festigen, Bilanz ziehen, Plan für danach.",
        ],
        "day": "Tag",
        "trig_label": "Dein Auslöser Nr. {n}",
        "trig_small": "Stufe {lv}: {name} · passt sich an dich an",
        "photo": "Foto-Tag",
        "legend": ["Fester Tagesinhalt", "Passt sich an deine Auslöser an", "📷 Foto-Tag"],
    },
    "en": {
        "phase_desc": [
            "Spot your patterns, see through the excuses, learn to catch it.",
            "Practise the competing response, keep your hands busy, find allies.",
            "Prepare for tricky situations, feelings and slips.",
            "Consolidate what is new, take stock, plan for afterwards.",
        ],
        "day": "Day",
        "trig_label": "Your trigger no. {n}",
        "trig_small": "Level {lv}: {name} · adapts to you",
        "photo": "Photo day",
        "legend": ["Fixed daily content", "Adapts to your triggers", "📷 Photo day"],
    },
}


def overview(lang, detailed=False):
    """Die 21 Tage als Übersicht, direkt aus der App-Struktur."""
    P, t = PROG[lang], T[lang]
    cols = []
    for ph in range(4):
        days = [d for d in range(1, 22) if PROG["phaseOfDays"][d - 1] == ph]
        name = P["phases"][ph].split("·", 1)[1].strip()
        lis = []
        for d in days:
            photo = " 📷" if d in PHOTO_DAYS else ""
            if str(d) in P["gen"]:
                lis.append(f'<li><span class="d">{d:02d}</span><span class="t">{E(P["gen"][str(d)])}{photo}</span></li>')
            else:
                n, lv = PROG["trig"][str(d)]
                lis.append(
                    f'<li><span class="d">{d:02d}</span><span class="t">{t["trig_label"].format(n=n + 1)}{photo}'
                    f'<small>{t["trig_small"].format(lv=lv, name=E(P["level"][lv]))}</small></span></li>'
                )
        rng = f'{t["day"]} {days[0]}–{days[-1]}'
        cols.append(
            f'<div class="phase reveal"><div class="phase-head"><small>Phase {ph + 1} · {rng}</small>'
            f'<h3>{E(name)}</h3><p>{E(t["phase_desc"][ph])}</p></div><ol class="days">{"".join(lis)}</ol></div>'
        )
    lg = t["legend"]
    legend = f'<div class="legend"><span class="tag">{lg[0]}</span><span class="tag green">{lg[1]}</span><span class="tag amber">{lg[2]}</span></div>'
    return f'<div class="phases">{"".join(cols)}</div>{legend}'


def exercise(lang, sheet_href, r=None):
    if lang == "de":
        opts = [("stress", "⚡", "Stress oder Nervosität"), ("bored", "🕰️", "Langeweile"), ("focus", "🧠", "Konzentriertes Arbeiten"),
                ("auto", "👀", "Ohne es zu merken"), ("other", "✍️", "Etwas anderes")]
        legend, other_l, other_ph = "Wann kaust du am ehesten?", "Dein Auslöser (optional)", "z. B. beim Telefonieren"
        empty = "Wähle eine Situation. Deine Übung erscheint hier."
        nos = ("Diese Übung braucht JavaScript. So geht sie auch ohne: 1. Wahrnehmen: Sag dir „Meine Hand will zum Mund.“ "
               "2. Innehalten: Fäuste 3 Sekunden ballen, lösen, Hände flach ablegen, 4 Sekunden ein, 6 Sekunden aus. "
               "3. Alternative wählen: Knetball, Stift oder Handcreme. 4. Reflektieren: Was hat es ausgelöst?")
        submit = "Übung anzeigen"
    else:
        opts = [("stress", "⚡", "Stress or nerves"), ("bored", "🕰️", "Boredom"), ("focus", "🧠", "Focused work"),
                ("auto", "👀", "Without noticing"), ("other", "✍️", "Something else")]
        legend, other_l, other_ph = "When do you bite your nails most?", "Your trigger (optional)", "e.g. when I am on the phone"
        empty = "Choose a situation. Your exercise will appear here."
        nos = ("This exercise needs JavaScript. Here it is without: 1. Notice: tell yourself “My hand wants to go to my mouth.” "
               "2. Pause: clench your fists for 3 seconds, release, hands flat, breathe in for 4, out for 6. "
               "3. Choose an alternative: stress ball, pen or hand cream. 4. Reflect: what set it off?")
        submit = "Show exercise"
    radios = "".join(
        f'<div class="opt"><input type="radio" name="trigger" id="t-{k}" value="{k}"><label for="t-{k}"><span aria-hidden="true">{ico}</span>{E(l)}</label></div>'
        for k, ico, l in opts
    )
    if r is None:
        r = "../" if lang == "en" else ""
    return f"""<div class="ex">
  <form id="ex-form" data-sheet="{sheet_href}" novalidate>
    <fieldset>
      <legend>{legend}</legend>
      {radios}
      <div class="ex-other" id="ex-other">
        <label class="field" for="ex-other-in"><span class="vh">{other_l}</span>
          <input class="input" id="ex-other-in" maxlength="60" autocomplete="off" placeholder="{other_ph}" aria-label="{other_l}">
        </label>
      </div>
      <noscript><p class="note">{nos}</p></noscript>
      <button class="btn btn-secondary vh" type="submit">{submit}</button>
    </fieldset>
  </form>
  <div class="ex-out" id="ex-out" aria-live="polite">
    <div class="ex-empty"><div>{img(r, 'knibbler-2.svg', '', 84, 112)}<p>{empty}</p></div></div>
  </div>
</div>"""


# ------------------------------------------------------------------
# Deutsch
# ------------------------------------------------------------------
def faq_de(r):
    return [
        ("Kann ich mir das Nägelkauen abgewöhnen?",
         "<p>Viele Menschen schaffen es, deutlich seltener oder gar nicht mehr zu kauen. Wie schnell und wie vollständig das gelingt, ist sehr unterschiedlich. "
         "Hilfreich ist, nicht nur auf Willenskraft zu setzen: die eigenen Auslöser kennen, den Moment früher bemerken und eine feste Alternative für die Hände haben. "
         f"Genau das übst du mit HÄNDE-STOPP. Mehr dazu im Ratgeber <a href=\"{r}naegelkauen-abgewoehnen/\">Nägelkauen abgewöhnen</a>.</p>"),
        ("Was passiert, wenn ich an einem Tag wieder kaue?",
         "<p>Dann machst du weiter. Ein Ausrutscher ist eine Information, kein Urteil. Feile den Nagel glatt, damit keine Kante lockt, notiere kurz, was los war, "
         "und setz beim nächsten Moment wieder an. Im Programm gibt es dafür einen eigenen Ablauf, und dein Tagesziel passt sich an.</p>"),
        ("Wie funktioniert das 21-Tage-Programm?",
         "<p>Du richtest in wenigen Minuten dein Profil ein: deine Auslöser, deine Gründe, dein Startdatum. Danach öffnet sich jeden Tag eine Einheit von etwa fünf Minuten: "
         "eine typische Ausrede durchschauen, zwei kurze Fragen, eine Tagesaufgabe und ein paar Zeilen Tagebuch. Was du einträgst, beeinflusst die nächsten Tage. "
         f"Am Ende kannst du dein Tagebuch als PDF speichern. <a href=\"{r}21-tage-programm/\">Alle Details zum Programm</a></p>"),
        ("Was mache ich bei Stress?",
         "<p>Bei Stress hilft eine Gegenbewegung, die mit Kauen nicht zusammenpasst: Fäuste fest ballen, lösen, Hände flach ablegen und länger aus- als einatmen. "
         f"Dazu etwas zum Drücken in Reichweite, zum Beispiel einen Knetball. Mehr dazu im Ratgeber <a href=\"{r}naegelkauen-bei-stress/\">Nägelkauen bei Stress</a>.</p>"),
        ("Brauche ich besondere Materialien?",
         "<p>Nein. Hilfreich sind eine Nagelfeile, Handcreme und etwas für die Hände, zum Beispiel ein Knetball oder ein Drehring. "
         "Manche nutzen zusätzlich ein Pflaster oder Bitterlack als spürbare Erinnerung. Für das Programm brauchst du nur ein Smartphone oder einen Computer mit aktuellem Browser.</p>"),
        ("Ist das Programm für Erwachsene geeignet?",
         "<p>Ja, NagelNEU ist für Erwachsene geschrieben, besonders für Menschen, die schon lange kauen. Für Kinder ist es nicht gedacht. "
         "Bei Kindern helfen eher Gelassenheit, kein Schimpfen und, wenn es stark belastet, ein Gespräch mit der Kinderärztin oder dem Kinderarzt.</p>"),
        ("Was kann ich tun, wenn die Gewohnheit sehr ausgeprägt ist?",
         "<p>Wenn deine Nagelbetten oft bluten oder sich entzünden, wenn du sehr darunter leidest oder es trotz vieler Versuche nicht besser wird, sprich mit deiner Hausärztin oder deinem Hausarzt. "
         "Verhaltenstherapeutische Unterstützung kann helfen. NagelNEU kannst du begleitend nutzen.</p>"),
        ("Ersetzt das Programm eine professionelle Behandlung?",
         "<p>Nein. NagelNEU ist ein Selbsthilfe-Begleiter und kein Medizinprodukt. Es stellt keine Diagnosen und ersetzt keine ärztliche oder psychotherapeutische Behandlung.</p>"),
        ("Was kostet NagelNEU?",
         "<p>Das Programm ist kostenlos, ohne Abo und ohne Vertrag. Beim Start bitte ich um deine E-Mail-Adresse und darum, meinem YouTube-Kanal zu folgen. "
         "Wer möchte, kann das Projekt freiwillig unterstützen.</p>"),
        ("Was passiert mit meinen Daten?",
         "<p>Deine Einträge, Fotos und Sprachnotizen bleiben in deinem Browser auf deinem Gerät. Sie werden nicht an NagelNEU übertragen, und du kannst sie in der App jederzeit löschen. "
         f"Details findest du in der <a href=\"{r}datenschutz/\">Datenschutzerklärung</a>.</p>"),
    ]


def faq_html(items, lang):
    title = "Häufige Fragen" if lang == "de" else "Frequently asked questions"
    eyebrow = "FAQ"
    rows = "".join(f"<details><summary>{E(q)}</summary><div>{a}</div></details>" for q, a in items)
    more = "Noch eine Frage? Frag den Assistenten" if lang == "de" else "Another question? Ask the assistant"
    return f"""<section id="faq" class="bg-2">
  <div class="wrap">
    <span class="eyebrow">{eyebrow}</span>
    <h2>{title}</h2>
    <div class="faq">{rows}</div>
    <p style="margin-top:28px"><button class="btn btn-secondary" type="button" data-open-chat>💬 {more}</button></p>
  </div>
</section>"""


def home_de():
    path, r = "", ""
    body = f"""
<section class="hero">
  <div class="wrap grid-2">
    <div>
      <p class="welcome" role="status"><span class="welcome-text"></span> <a class="arrow-link" href="app/">Weiter</a></p>
      <span class="eyebrow">Für Erwachsene, die schon lange Nägel kauen</span>
      <h1>Du kaust an deinen Nägeln. Vielleicht seit Jahren. <em>Dafür musst du dich nicht schämen.</em></h1>
      <p class="lead">NagelNEU hilft dir, den automatischen Moment früher zu bemerken und deinen Händen etwas anderes anzubieten. Mit der HÄNDE-STOPP-Methode und einem 21-Tage-Programm: etwa fünf Minuten am Tag, kostenlos, direkt im Browser.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="app/">Meine 21 Tage entdecken</a>
        <a class="btn btn-secondary" href="#uebung">Erst die 60-Sekunden-Übung testen</a>
      </div>
      <div class="hero-meta"><span>Kostenlos</span><span>Etwa 5 Minuten am Tag</span><span>Deine Einträge bleiben auf deinem Gerät</span></div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="phone"><img src="assets/img/app-start-de.webp" alt="" width="390" height="823" fetchpriority="high"></div>
      {img(r, 'knibbler-2.svg', '', 120, 160, 'hero-fig', lazy=False)}
      <div class="hero-note"><span class="hand">Erst bemerken.<br>Dann neu entscheiden.</span></div>
    </div>
  </div>
</section>

<section class="situations bg-2" aria-labelledby="h-problem">
  <div class="wrap">
    <span class="eyebrow">Kommt dir das bekannt vor?</span>
    <h2 id="h-problem">Meistens passiert es, bevor du darüber nachdenkst.</h2>
    <p class="lead">Nägelkauen hat selten nur einen Grund. Viele erkennen sich in einer oder mehreren dieser Situationen wieder. Deine können auch ganz andere sein.</p>
    <div class="grid-3" style="margin-top:32px">
      <div class="card reveal"><span class="ico" aria-hidden="true">⚡</span><h3>Wenn der Druck steigt</h3><p>Eine Frist, ein schwieriges Gespräch, zu viel auf einmal. Die Hand wandert zum Mund, als könnte sie die Anspannung kurz abbauen.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🕰️</span><h3>Wenn nichts passiert</h3><p>Warten, Scrollen, Fernsehen. Die Hände haben nichts zu tun und suchen sich selbst etwas.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🧠</span><h3>Wenn du dich konzentrierst</h3><p>Beim Lesen, Lernen oder Nachdenken ist der Kopf beschäftigt, und die Hand arbeitet allein weiter.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">👀</span><h3>Wenn du es erst hinterher merkst</h3><p>Oft fällt es erst auf, wenn der Nagel schon kürzer ist. Das ist kein Zeichen von Schwäche, sondern typisch für eine eingeschliffene Gewohnheit.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🤲</span><h3>Wenn du aufhören willst, aber nicht weißt wie</h3><p>Vorsätze allein reichen oft nicht, weil die Bewegung schneller ist als der Gedanke. Es fehlt eine konkrete Alternative für genau diesen Moment.</p></div>
      <div class="card reveal" style="background:var(--rose-soft);border-color:transparent"><h3>Darum setzt NagelNEU nicht auf Willenskraft.</h3><p>Sondern auf einen kurzen Ablauf, den du üben kannst, bis er in schwierigen Momenten von selbst greift.</p><p><a class="arrow-link" href="warum-kaue-ich-naegel/">Warum kaue ich Nägel?</a></p></div>
    </div>
  </div>
</section>

<section id="methode" aria-labelledby="h-method">
  <div class="wrap">
    <span class="eyebrow">Die Methode</span>
    <h2 id="h-method"><span class="method-word">HÄNDE-STOPP</span>: vier Schritte für den automatischen Moment</h2>
    <p class="lead">HÄNDE-STOPP ist eine Übungsstruktur, mit der du den Griff zum Mund unterbrichst. Du kannst sie überall einsetzen, ohne Hilfsmittel, in etwa einer Minute.</p>
    <ol class="method-steps" style="list-style:none;padding:0">
      <li class="step reveal"><span class="num" aria-hidden="true">01</span><h3>Wahrnehmen</h3><p class="q">Was passiert gerade?</p><p>Du bemerkst die Bewegung und benennst sie innerlich: „Meine Hand will zum Mund.“ Schon das ist ein Erfolg.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">02</span><h3>Innehalten</h3><p class="q">Kann ich kurz unterbrechen?</p><p>Fäuste 3 Sekunden ballen, lösen, Hände flach ablegen. 4 Sekunden ein, 6 Sekunden aus. Die Welle wird meist schnell kleiner.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">03</span><h3>Alternative wählen</h3><p class="q">Was können meine Hände stattdessen tun?</p><p>Etwas halten, drücken oder pflegen: Knetball, Stift, Handcreme, Feile. Vorher festgelegt, fällt es im Ernstfall leichter.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">04</span><h3>Reflektieren</h3><p class="q">Was habe ich bemerkt?</p><p>Ein kurzer Blick zurück: Wo war ich, was hat es ausgelöst, was hat geholfen? So erkennst du mit der Zeit dein Muster.</p></li>
    </ol>
    <p class="note soft" style="margin-top:28px"><strong>Gut zu wissen:</strong> HÄNDE-STOPP ist eine praktische Übungsstruktur. Sie greift Elemente auf, die auch in der Verhaltenstherapie bei Gewohnheiten wie dem Nägelkauen genutzt werden, ist selbst aber kein medizinisch geprüftes Verfahren.</p>
    <p><a class="arrow-link" href="haende-stopp/">Mehr zur Methode und weitere Übungen</a></p>
  </div>
</section>

<section id="uebung" class="night" aria-labelledby="h-ex">
  <div class="wrap">
    <span class="eyebrow">Jetzt ausprobieren</span>
    <h2 id="h-ex">Deine erste HÄNDE-STOPP-Übung</h2>
    <p class="lead">Wähle, wann du am ehesten kaust. Du bekommst sofort eine passende Übung und kannst die 60 Sekunden direkt mitmachen. Ohne Anmeldung.</p>
    {exercise('de', 'arbeitsblatt/')}
  </div>
</section>

<section id="programm" aria-labelledby="h-prog">
  <div class="wrap">
    <span class="eyebrow">Das 21-Tage-Programm</span>
    <h2 id="h-prog">21 Tage üben, bemerken und notieren</h2>
    <p class="lead">Das Programm führt dich drei Wochen lang durch die HÄNDE-STOPP-Methode. Jeden Tag gibt es eine kurze Einheit, die sich an deine Auslöser und Einträge anpasst.</p>
    <div class="facts" style="margin-top:32px">
      <div class="fact reveal"><h3>Für wen?</h3><p>Für Erwachsene, die schon länger Nägel kauen oder an der Nagelhaut knibbeln und das ohne Druck verändern möchten.</p></div>
      <div class="fact reveal"><h3>Was machst du?</h3><p>Jeden Tag eine typische Ausrede durchschauen, zwei kurze Fragen beantworten, eine Tagesaufgabe erledigen und ein paar Zeilen Tagebuch schreiben oder einsprechen. Für akute Momente gibt es den Knopf „Ertappt!“ und den 60-Sekunden-HÄNDE-STOPP.</p></div>
      <div class="fact reveal"><h3>Wie viel Zeit?</h3><p>Etwa fünf Minuten am Tag, dazu die Momente, in denen du übst. Ein neuer Tag öffnet sich jeweils 24 Stunden nach dem vorherigen.</p></div>
      <div class="fact reveal"><h3>Was ist enthalten?</h3><p>21 Tagesmissionen, Tage zu deinen persönlichen Auslösern, ein Tagebuch mit Spracheingabe, Fotos an Tag 1, 7, 14 und 21, eine Notfallkarte, ein druckbarer Hände-Plan und zum Schluss dein Tagebuch als PDF. Auf Deutsch und Englisch.</p></div>
      <div class="fact reveal"><h3>Wie siehst du Fortschritt?</h3><p>Du zählst, wie oft du dich ertappst und wie oft du doch kaust. Dein Tagesziel sinkt Schritt für Schritt. Kurven, Fotos und Tagebuch zeigen dir, was sich verändert.</p></div>
      <div class="fact reveal"><h3>Was brauchst du?</h3><p>Ein Smartphone oder einen Computer mit aktuellem Browser. Hilfreich sind eine Nagelfeile, Handcreme und etwas für die Hände, etwa ein Knetball.</p></div>
      <div class="fact reveal"><h3>Was kannst du erwarten? <span class="tag green">realistisch</span></h3><p>Mehr Bewusstsein für deine Momente, konkrete Alternativen und einen Plan für schwierige Tage. Wie schnell sich etwas verändert, ist sehr unterschiedlich. Rückschritte gehören dazu.</p></div>
      <div class="fact reveal"><h3>Wo sind die Grenzen? <span class="tag amber">wichtig</span></h3><p>NagelNEU ist ein Selbsthilfe-Begleiter, keine Behandlung, und es gibt keine Erfolgsgarantie. Bei Entzündungen, starkem Leidensdruck oder wenn das Kauen mit Ängsten oder Zwängen verbunden ist, hol dir bitte ärztliche oder psychotherapeutische Unterstützung.</p></div>
    </div>
    <div class="btn-row" style="margin-top:32px">
      <a class="btn btn-primary" href="app/">Meine 21 Tage entdecken</a>
      <a class="arrow-link" href="21-tage-programm/">Alle Details zum Programm</a>
    </div>
  </div>
</section>

<section class="bg-2" aria-labelledby="h-days">
  <div class="wrap">
    <span class="eyebrow">Übersicht</span>
    <h2 id="h-days">Die 21 Tage auf einen Blick</h2>
    <p class="lead">Vier Phasen mit einem roten Faden: erst verstehen, dann umlernen, dann absichern. An neun Tagen geht es um deine persönlichen Auslöser, in drei Stufen.</p>
    {overview('de')}
    <p class="mute small" style="margin-top:20px">Knibbler sind kleine Fingerfiguren im Programm. Sie stehen für die inneren Ausreden, die zum Kauen verleiten, etwa „Nur die eine Kante“.</p>
  </div>
</section>

<section aria-labelledby="h-story">
  <div class="wrap story">
    <div class="story-figs" aria-hidden="true">{img(r, 'knibbler-0.svg', '', 72, 96)}{img(r, 'knibbler-4.svg', '', 88, 117)}{img(r, 'knibbler-2.svg', '', 72, 96)}</div>
    <div>
      <span class="eyebrow">Warum es NagelNEU gibt</span>
      <h2 id="h-story">Entstanden aus eigener Erfahrung</h2>
      <!-- OFFENER PUNKT: Persönliche Details von Frank (z. B. wie lange er gekaut hat, was ihm geholfen hat, ein Foto) bestätigen und hier ergänzen. Siehe docs/OFFENE-PUNKTE.md -->
      <p class="lead">Hinter NagelNEU steht Frank Zimmermann. Er kennt das Nägelkauen aus eigener Erfahrung, und er kennt den Weg, es zu verändern.</p>
      <p>Aus dieser Erfahrung ist NagelNEU entstanden: keine Belehrung und kein Versprechen, sondern eine Begleitung, die ernst nimmt, wie schnell und automatisch Nägelkauen passiert. Und die zeigt, was du in genau diesem Moment tun kannst.</p>
      <div class="yt" style="margin-top:24px">
        <span class="yt-ico" aria-hidden="true"></span>
        <div style="flex:1;min-width:220px"><strong>Auf YouTube: {YT_NAME}</strong><br><span class="mute">Kurze Übungen und Gedanken rund ums Nägelkauen. Ein Abo hilft, das Programm weiter kostenlos anzubieten.</span></div>
        <a class="btn btn-secondary btn-sm" href="{YT_URL}" rel="noopener" target="_blank">Zum Kanal</a>
      </div>
    </div>
  </div>
</section>

{faq_html(faq_de(r), 'de')}

<section class="cta-final" aria-labelledby="h-cta">
  <div class="wrap">
    <div class="card">
      <h2 id="h-cta">Bereit für den ersten Tag?</h2>
      <p class="lead">Du musst nichts perfekt machen. Es reicht, heute einmal zu bemerken, wann deine Hand zum Mund will.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="app/">Meine 21 Tage entdecken</a>
        <a class="btn btn-secondary" href="#uebung">Erst die Übung testen</a>
      </div>
      <p class="small" style="margin-top:20px">Kostenlos · für Erwachsene · keine Erfolgsgarantie, aber ein klarer Plan</p>
    </div>
  </div>
</section>
"""
    head = """
<script>/* Alte Links auf das Tagebuch oder die Sprachwahl führen direkt in die App */
(function(){function go(){var h=location.hash,s=location.search;if(/^#tagebuch/i.test(h)||/[?&]lang=/.test(s)){location.replace('app/'+(location.protocol==='file:'?'index.html':'')+s+h)}}go();window.addEventListener('hashchange',go)})();</script>"""
    ld = [
        {"@type": "WebSite", "@id": SITE + "#website", "url": SITE, "name": "NagelNEU", "inLanguage": "de-DE", "publisher": {"@id": SITE + "#org"}},
        {"@type": "WebPage", "@id": SITE + "#webpage", "url": SITE, "name": "NagelNEU: Nägelkauen abgewöhnen mit der HÄNDE-STOPP-Methode",
         "isPartOf": {"@id": SITE + "#website"}, "inLanguage": "de-DE", "dateModified": "2026-10-22"},
    ]
    page(path, "de", "NagelNEU: Nägelkauen abgewöhnen mit der HÄNDE-STOPP-Methode",
         "Du kaust seit Jahren Nägel? NagelNEU hilft Erwachsenen, den automatischen Moment früher zu bemerken. Kostenloses 21-Tage-Programm mit der HÄNDE-STOPP-Methode.",
         body, alternates={"de": "", "en": "en/", "x-default": ""}, ld=ld, extra_head=head)


# ------------------------------------------------------------------
# English
# ------------------------------------------------------------------
def faq_en(r):
    return [
        ("Can I stop biting my nails?",
         "<p>Many people manage to bite much less often or stop altogether. How quickly and how completely that happens varies a lot. "
         "It helps not to rely on willpower alone: know your triggers, notice the moment earlier and have a set alternative for your hands. That is exactly what you practise with HANDS STOP.</p>"),
        ("What if I bite my nails again one day?",
         "<p>Then you carry on. A slip is information, not a verdict. File the nail smooth so no edge tempts you, briefly note what was going on, and start again at the next moment. "
         "The programme has its own routine for this, and your daily goal adapts.</p>"),
        ("How does the 21-day programme work?",
         "<p>You set up your profile in a few minutes: your triggers, your reasons, your start date. Then a session of about five minutes opens each day: "
         "see through a typical excuse, answer two short questions, do a daily task and write or speak a few lines in your diary. What you enter shapes the following days. "
         "At the end you can save your diary as a PDF.</p>"),
        ("What do I do when I am stressed?",
         "<p>Under stress, a counter-movement that does not fit with biting helps: clench your fists firmly, release, lay your hands flat and breathe out for longer than you breathe in. "
         "Keep something to squeeze within reach, such as a stress ball.</p>"),
        ("Do I need any special materials?",
         "<p>No. A nail file, hand cream and something for your hands, such as a stress ball or spinner ring, are helpful. "
         "Some people also use a plaster or bitter nail polish as a noticeable reminder. For the programme, you only need a smartphone or computer with an up-to-date browser.</p>"),
        ("Is the programme suitable for adults?",
         "<p>Yes, NagelNEU is written for adults, especially people who have been biting their nails for a long time. It is not designed for children.</p>"),
        ("What can I do if the habit is very strong?",
         "<p>If your nail beds often bleed or become inflamed, if it causes you a lot of distress, or if nothing improves despite many attempts, talk to your GP. "
         "Behavioural therapy can help. You can use NagelNEU alongside it.</p>"),
        ("Does the programme replace professional treatment?",
         "<p>No. NagelNEU is a self-help companion, not a medical device. It does not diagnose anything and does not replace medical or psychotherapeutic treatment.</p>"),
        ("What does NagelNEU cost?",
         "<p>The programme is free, with no subscription and no contract. When you start, I ask for your email address and for you to follow my YouTube channel. "
         "If you like, you can support the project voluntarily.</p>"),
        ("What happens to my data?",
         "<p>Your entries, photos and voice notes stay in your browser on your device. They are not transferred to NagelNEU, and you can delete them in the app at any time. "
         f"See the <a href=\"{r}datenschutz/\" hreflang=\"de\">privacy policy (German)</a> for details.</p>"),
    ]


def home_en():
    path, r = "en/", "../"
    body = f"""
<section class="hero">
  <div class="wrap grid-2">
    <div>
      <p class="welcome" role="status"><span class="welcome-text"></span> <a class="arrow-link" href="../app/?lang=en">Continue</a></p>
      <span class="eyebrow">For adults who have bitten their nails for a long time</span>
      <h1>You bite your nails. Maybe for years. <em>There is nothing to be ashamed of.</em></h1>
      <p class="lead">NagelNEU helps you notice the automatic moment earlier and offer your hands something else. With the HANDS STOP method and a 21-day programme: about five minutes a day, free, right in your browser.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="../app/?lang=en">Discover my 21 days</a>
        <a class="btn btn-secondary" href="#exercise">Try the 60-second exercise first</a>
      </div>
      <div class="hero-meta"><span>Free</span><span>About 5 minutes a day</span><span>Your entries stay on your device</span></div>
    </div>
    <div class="hero-visual" aria-hidden="true">
      <div class="phone"><img src="../assets/img/app-start-en.webp" alt="" width="390" height="823" fetchpriority="high"></div>
      {img(r, 'knibbler-2.svg', '', 120, 160, 'hero-fig', lazy=False)}
      <div class="hero-note"><span class="hand">Notice first.<br>Then decide anew.</span></div>
    </div>
  </div>
</section>

<section class="situations bg-2" aria-labelledby="h-problem">
  <div class="wrap">
    <span class="eyebrow">Sound familiar?</span>
    <h2 id="h-problem">It usually happens before you even think about it.</h2>
    <p class="lead">Nail biting rarely has just one cause. Many people recognise themselves in one or more of these situations. Yours may be quite different.</p>
    <div class="grid-3" style="margin-top:32px">
      <div class="card reveal"><span class="ico" aria-hidden="true">⚡</span><h3>When the pressure rises</h3><p>A deadline, a difficult conversation, too much at once. Your hand drifts to your mouth as if it could briefly release the tension.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🕰️</span><h3>When nothing is happening</h3><p>Waiting, scrolling, watching TV. Your hands have nothing to do and find something on their own.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🧠</span><h3>When you are concentrating</h3><p>While reading, studying or thinking, your mind is busy and your hand carries on by itself.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">👀</span><h3>When you only notice afterwards</h3><p>Often you only realise once the nail is shorter. That is not a sign of weakness, it is typical of an ingrained habit.</p></div>
      <div class="card reveal"><span class="ico" aria-hidden="true">🤲</span><h3>When you want to stop but do not know how</h3><p>Good intentions alone often fall short, because the movement is faster than the thought. What is missing is a concrete alternative for exactly that moment.</p></div>
      <div class="card reveal" style="background:var(--rose-soft);border-color:transparent"><h3>That is why NagelNEU does not rely on willpower.</h3><p>It relies on a short routine you can practise until it kicks in by itself in difficult moments.</p></div>
    </div>
  </div>
</section>

<section id="method" aria-labelledby="h-method">
  <div class="wrap">
    <span class="eyebrow">The method</span>
    <h2 id="h-method"><span class="method-word">HANDS STOP</span>: four steps for the automatic moment</h2>
    <p class="lead">HANDS STOP (in German: HÄNDE-STOPP) is a practice routine that interrupts the reach to your mouth. You can use it anywhere, without any tools, in about a minute.</p>
    <ol class="method-steps" style="list-style:none;padding:0">
      <li class="step reveal"><span class="num" aria-hidden="true">01</span><h3>Notice</h3><p class="q">What is happening right now?</p><p>You notice the movement and name it to yourself: “My hand wants to go to my mouth.” That alone is a success.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">02</span><h3>Pause</h3><p class="q">Can I interrupt it briefly?</p><p>Clench your fists for 3 seconds, release, lay your hands flat. Breathe in for 4, out for 6. The wave usually gets smaller quickly.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">03</span><h3>Choose an alternative</h3><p class="q">What can my hands do instead?</p><p>Hold, squeeze or care for something: a stress ball, a pen, hand cream, a nail file. Decided in advance, it is easier when it counts.</p></li>
      <li class="step reveal"><span class="num" aria-hidden="true">04</span><h3>Reflect</h3><p class="q">What did I notice?</p><p>A quick look back: where was I, what set it off, what helped? Over time you will recognise your pattern.</p></li>
    </ol>
    <p class="note soft" style="margin-top:28px"><strong>Good to know:</strong> HANDS STOP is a practical exercise routine. It draws on elements that are also used in behavioural therapy for habits like nail biting, but it is not a medically tested procedure in itself.</p>
  </div>
</section>

<section id="exercise" class="night" aria-labelledby="h-ex">
  <div class="wrap">
    <span class="eyebrow">Try it now</span>
    <h2 id="h-ex">Your first HANDS STOP exercise</h2>
    <p class="lead">Choose when you bite your nails most. You get a matching exercise straight away and can do the 60 seconds right here. No sign-up.</p>
    {exercise('en', 'worksheet/')}
  </div>
</section>

<section id="programme" aria-labelledby="h-prog">
  <div class="wrap">
    <span class="eyebrow">The 21-day programme</span>
    <h2 id="h-prog">21 days of practising, noticing and noting</h2>
    <p class="lead">The programme takes you through the HANDS STOP method over three weeks. Each day there is a short session that adapts to your triggers and entries.</p>
    <div class="facts" style="margin-top:32px">
      <div class="fact reveal"><h3>Who is it for?</h3><p>Adults who have bitten their nails or picked at their cuticles for a long time and want to change that without pressure.</p></div>
      <div class="fact reveal"><h3>What do you do?</h3><p>Every day you see through a typical excuse, answer two short questions, do a daily task and write or speak a few lines in your diary. For acute moments there is the “Caught it!” button and the 60-second HANDS STOP.</p></div>
      <div class="fact reveal"><h3>How much time?</h3><p>About five minutes a day, plus the moments when you practise. Each new day opens 24 hours after the previous one.</p></div>
      <div class="fact reveal"><h3>What is included?</h3><p>21 daily missions, days for your personal triggers, a diary with voice input, photos on days 1, 7, 14 and 21, an emergency card, a printable hands plan and, at the end, your diary as a PDF. In English and German.</p></div>
      <div class="fact reveal"><h3>How do you see progress?</h3><p>You count how often you catch yourself and how often you bite anyway. Your daily goal drops step by step. Charts, photos and your diary show you what is changing.</p></div>
      <div class="fact reveal"><h3>What do you need?</h3><p>A smartphone or computer with an up-to-date browser. A nail file, hand cream and something for your hands, such as a stress ball, are helpful.</p></div>
      <div class="fact reveal"><h3>What can you expect? <span class="tag green">realistic</span></h3><p>More awareness of your moments, concrete alternatives and a plan for difficult days. How quickly things change varies a lot. Setbacks are part of it.</p></div>
      <div class="fact reveal"><h3>What are the limits? <span class="tag amber">important</span></h3><p>NagelNEU is a self-help companion, not a treatment, and there is no guarantee of success. If there is inflammation, significant distress, or if the biting is linked to anxiety or compulsions, please seek medical or psychotherapeutic support.</p></div>
    </div>
    <div class="btn-row" style="margin-top:32px">
      <a class="btn btn-primary" href="../app/?lang=en">Discover my 21 days</a>
    </div>
  </div>
</section>

<section class="bg-2" aria-labelledby="h-days">
  <div class="wrap">
    <span class="eyebrow">Overview</span>
    <h2 id="h-days">The 21 days at a glance</h2>
    <p class="lead">Four phases with one common thread: understand first, then relearn, then secure. On nine days the focus is on your personal triggers, in three levels.</p>
    {overview('en')}
    <p class="mute small" style="margin-top:20px">Nibblers are little finger characters in the programme. They stand for the inner excuses that tempt you to bite, such as “Just that one edge”.</p>
  </div>
</section>

<section aria-labelledby="h-story">
  <div class="wrap story">
    <div class="story-figs" aria-hidden="true">{img(r, 'knibbler-0.svg', '', 72, 96)}{img(r, 'knibbler-4.svg', '', 88, 117)}{img(r, 'knibbler-2.svg', '', 72, 96)}</div>
    <div>
      <span class="eyebrow">Why NagelNEU exists</span>
      <h2 id="h-story">Born from personal experience</h2>
      <p class="lead">NagelNEU was created by Frank Zimmermann. He knows nail biting from his own experience, and he knows the path to changing it.</p>
      <p>That experience is where NagelNEU comes from: no lecturing and no promises, but a companion that takes seriously how fast and automatic nail biting is. And that shows you what you can do in exactly that moment.</p>
      <div class="yt" style="margin-top:24px">
        <span class="yt-ico" aria-hidden="true"></span>
        <div style="flex:1;min-width:220px"><strong>On YouTube: {YT_NAME}</strong><br><span class="mute">Short exercises and thoughts about nail biting (in German).</span></div>
        <a class="btn btn-secondary btn-sm" href="{YT_URL}" rel="noopener" target="_blank">Visit the channel</a>
      </div>
    </div>
  </div>
</section>

{faq_html(faq_en(r), 'en')}

<section class="cta-final" aria-labelledby="h-cta">
  <div class="wrap">
    <div class="card">
      <h2 id="h-cta">Ready for day one?</h2>
      <p class="lead">You do not have to do anything perfectly. Today it is enough to notice once when your hand wants to go to your mouth.</p>
      <div class="btn-row">
        <a class="btn btn-primary" href="../app/?lang=en">Discover my 21 days</a>
        <a class="btn btn-secondary" href="#exercise">Try the exercise first</a>
      </div>
      <p class="small" style="margin-top:20px">Free · for adults · no guarantee of success, but a clear plan</p>
    </div>
  </div>
</section>
"""
    ld = [
        {"@type": "WebPage", "@id": SITE + "en/#webpage", "url": SITE + "en/", "name": "NagelNEU: Stop biting your nails with the HANDS STOP method",
         "inLanguage": "en-GB", "isPartOf": {"@id": SITE + "#website"}, "dateModified": "2026-10-22"},
    ]
    page(path, "en", "NagelNEU: Stop biting your nails with the HANDS STOP method",
         "Biting your nails for years? NagelNEU helps adults notice the automatic moment earlier. A free 21-day programme built on the HANDS STOP method.",
         body, alternates={"de": "", "en": "en/", "x-default": ""}, ld=ld, alt_path="")
