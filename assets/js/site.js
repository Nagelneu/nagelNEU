/* NagelNEU · Website-Skript · Design by Frank Zimmermann © 2026
   Navigation, Willkommen zurück, sanftes Einblenden, HÄNDE-STOPP-Einstiegsübung.
   Die Übung speichert und überträgt nichts. */
(function () {
  'use strict';
  var EN = (document.documentElement.lang || '').slice(0, 2) === 'en';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var reduce = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Lokal geöffnet (Doppelklick auf die Datei): Ordner-Links zeigen sonst nur eine Dateiliste.
     Darum wird dort an jeden Ordner-Link „index.html“ angehängt. Online ändert sich nichts. */
  if (location.protocol === 'file:') {
    $$('a[href]').forEach(function (a) {
      var h = a.getAttribute('href');
      if (/^(https?:|mailto:|tel:|#|data:|javascript:)/i.test(h)) return;
      var m = h.match(/^([^?#]*)(\?[^#]*)?(#.*)?$/); if (!m) return;
      var p = m[1], q = m[2] || '', x = m[3] || '';
      if (p === '' && (q || x)) { if (!q) return; p = './'; }
      if (p === '' || p === '.' ) p = './';
      if (/\/$/.test(p)) a.setAttribute('href', p + 'index.html' + q + x);
    });
  }

  /* Kopfzeile & Menü */
  var hdr = $('.site-header');
  var onScroll = function () { if (hdr) hdr.classList.toggle('scrolled', window.scrollY > 8); };
  window.addEventListener('scroll', onScroll, { passive: true }); onScroll();
  var tog = $('.nav-toggle'), nav = $('#nav');
  if (tog && nav) {
    var setOpen = function (o) { nav.classList.toggle('open', o); tog.setAttribute('aria-expanded', o ? 'true' : 'false'); };
    tog.addEventListener('click', function () { setOpen(!nav.classList.contains('open')); });
    $$('a', nav).forEach(function (a) { a.addEventListener('click', function () { setOpen(false); }); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape') setOpen(false); });
  }

  /* Willkommen zurück: liest nur lokal gespeicherte App-Daten auf diesem Gerät, sendet nichts */
  var wb = $('.welcome');
  if (wb) {
    try {
      var st = JSON.parse(localStorage.getItem('nn_app_v1') || 'null');
      var p = st && st.profile;
      if (p && p.startTs) {
        var d = Math.max(1, Math.min(21, Math.floor((Date.now() - p.startTs) / 864e5) + 1));
        var name = String(p.name || '').slice(0, 40);
        $('.welcome-text', wb).textContent = EN
          ? 'Welcome back' + (name ? ', ' + name : '') + '. Your journey continues with day ' + d + '.'
          : 'Willkommen zurück' + (name ? ', ' + name : '') + '. Deine Reise geht weiter mit Tag ' + d + '.';
        wb.classList.add('show');
      }
    } catch (e) { /* kein Zugriff auf lokalen Speicher: Hinweis bleibt aus */ }
  }

  /* Sanftes Einblenden */
  if (!reduce && 'IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (es) {
      es.forEach(function (en) { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    $$('.reveal').forEach(function (el) { io.observe(el); });
  } else { $$('.reveal').forEach(function (el) { el.classList.add('in'); }); }

  /* Chat-Assistent: öffnet den Chat der App als Fenster. Er wird erst beim ersten Klick geladen. */
  (function () {
    var root = document.body.getAttribute('data-root');
    if (root === null || document.body.classList.contains('no-chat')) return;
    var local = location.protocol === 'file:';
    var src = root + 'app/' + (local ? 'index.html' : '') + '?chat=1&lang=' + (EN ? 'en' : 'de');
    var fab = document.createElement('button');
    fab.type = 'button'; fab.className = 'chat-fab';
    fab.setAttribute('aria-haspopup', 'dialog'); fab.setAttribute('aria-controls', 'chat-panel');
    fab.innerHTML = '<span class="chat-ico" aria-hidden="true">💬</span><span>' + (EN ? 'Ask me' : 'Fragen?') + '</span>';
    fab.setAttribute('aria-label', EN ? 'Open the chat assistant' : 'Chat-Assistent öffnen');
    var panel = document.createElement('div');
    panel.id = 'chat-panel'; panel.className = 'chat-panel'; panel.setAttribute('role', 'dialog');
    panel.setAttribute('aria-label', EN ? 'NagelNEU assistant' : 'NagelNEU-Assistent'); panel.hidden = true;
    document.body.appendChild(fab); document.body.appendChild(panel);
    var frame = null, last = null;
    function open() {
      last = document.activeElement;
      if (!frame) {
        frame = document.createElement('iframe');
        frame.title = EN ? 'NagelNEU assistant' : 'NagelNEU-Assistent';
        frame.setAttribute('allow', 'microphone');
        frame.src = src; panel.appendChild(frame);
      }
      panel.hidden = false; fab.hidden = true; document.documentElement.classList.add('chat-open');
      setTimeout(function () { try { frame.focus(); } catch (e) {} }, 60);
    }
    function close() {
      panel.hidden = true; fab.hidden = false; document.documentElement.classList.remove('chat-open');
      if (last && last.focus) last.focus(); else fab.focus();
    }
    fab.addEventListener('click', open);
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !panel.hidden) close(); });
    window.addEventListener('message', function (e) { if (e.data && e.data.nagelneu === 'chatclose') close(); });
    $$('[data-open-chat]').forEach(function (b) { b.addEventListener('click', function (e) { e.preventDefault(); open(); }); });
  })();

  /* Drucken */
  $$('[data-print]').forEach(function (b) { b.addEventListener('click', function () { window.print(); }); });

  /* ---------- HÄNDE-STOPP-Einstiegsübung ---------- */
  var form = $('#ex-form');
  if (!form) return;
  var out = $('#ex-out'), other = $('#ex-other'), otherIn = $('#ex-other-in');

  var X = EN ? {
    title: 'Your HANDS STOP exercise',
    forT: 'For: ',
    steps: ['Notice', 'Pause', 'Choose an alternative', 'Reflect'],
    start: 'Try 60 seconds now', again: 'Start again', stop: 'Stop',
    print: 'Print the worksheet',
    fallback: 'your own trigger',
    hint: 'Nothing you choose or type here is saved or sent.',
    done: 'Done. How strong is the urge now?',
    r: { less: 'Weaker', same: 'Same', more: 'Stronger' },
    msg: {
      less: 'That is exactly how the method works: the wave passes, and you noticed it. Repeat this minute the next time the urge comes.',
      same: 'That is normal at the beginning. The first goal is noticing, not perfection. Try the minute again later, or start with step 1 only: noticing.',
      more: 'That happens. Sometimes the urge peaks before it fades. Repeat the minute, keep your hands busy and file any rough edge. If it stays very strong over a long period, it is worth talking to your GP.'
    },
    cues: { fist: 'Clench your fists firmly', release: 'Release', flat: 'Lay your hands flat on your thighs', inh: 'Breathe in … 4', exh: 'Breathe out … 6', end: 'Well done.' }
  } : {
    title: 'Deine HÄNDE-STOPP-Übung',
    forT: 'Für: ',
    steps: ['Wahrnehmen', 'Innehalten', 'Alternative wählen', 'Reflektieren'],
    start: '60 Sekunden jetzt ausprobieren', again: 'Noch einmal', stop: 'Abbrechen',
    print: 'Arbeitsblatt drucken',
    fallback: 'deinen eigenen Auslöser',
    hint: 'Was du hier auswählst oder eintippst, wird nicht gespeichert und nicht gesendet.',
    done: 'Geschafft. Wie stark ist der Drang jetzt?',
    r: { less: 'Schwächer', same: 'Gleich', more: 'Stärker' },
    msg: {
      less: 'Genau so funktioniert die Methode: Die Welle geht vorbei, und du hast es bemerkt. Wiederhole diese Minute, wenn der Drang das nächste Mal kommt.',
      same: 'Das ist am Anfang normal. Das erste Ziel ist Bemerken, nicht Perfektion. Probier die Minute später noch einmal oder beginne nur mit Schritt 1: Wahrnehmen.',
      more: 'Das kommt vor. Manchmal steigt der Drang kurz an, bevor er abflaut. Wiederhole die Minute, beschäftige deine Hände und feile raue Kanten glatt. Bleibt er über lange Zeit sehr stark, lohnt sich ein Gespräch mit deiner Hausärztin oder deinem Hausarzt.'
    },
    cues: { fist: 'Fäuste fest ballen', release: 'Lösen', flat: 'Hände flach auf die Oberschenkel', inh: 'Einatmen … 4', exh: 'Ausatmen … 6', end: 'Gut gemacht.' }
  };

  var DATA = EN ? {
    stress: { l: 'Stress or nerves', s: [
      'Check your shoulders, jaw and breathing. Say to yourself: “My hand wants to go to my mouth.”',
      'Clench your fists firmly for 3 seconds, release, lay your hands flat. Breathe in for 4, out for 6.',
      'Give your hands something to press: a stress ball, a pen, the edge of the table. Under pressure, squeezing helps more than fidgeting.',
      'What set off the stress just now? One word is enough.'] },
    bored: { l: 'Boredom', s: [
      'Boredom is quiet. Waiting, scrolling and watching TV are typical moments. Today, just notice when it happens.',
      'Lay your hands flat for 10 seconds and consciously look at three things around you.',
      'Keep your hands busy: a spinner ring, a stress ball, or massage in some hand cream.',
      'What did you actually need right then: movement, a break or something to do?'] },
    focus: { l: 'Focused work', s: [
      'When you are thinking hard, your hand often works on its own. A plaster on your favourite finger makes the movement noticeable.',
      'Put the pen down, hands flat on the desk, two long breaths out.',
      'Give your thinking hand something: a pen, a spinner ring, a stress ball. Take a short hands break every 25 minutes.',
      'During which task does it happen most often?'] },
    auto: { l: 'Without noticing', s: [
      'The goal is not perfection but noticing earlier. Every catch counts, even afterwards.',
      'As soon as you notice: gently put your hand back on your thigh and breathe out. No anger.',
      'Put an “alarm” on your finger: a plaster, a ring or bitter nail polish. File your nails smooth so no edge tempts you.',
      'Where were you just now, and what were you doing? Note it briefly.'] },
    other: { l: '', s: [
      'Watch the situation “{x}” closely today: what happens just before your hand goes to your mouth?',
      'Clench your fists for 3 seconds, release, hands flat. Breathe in for 4, out for 6.',
      'Decide in advance what your hands will do in this situation: hold, press or care for something.',
      'Write an if-then plan: “When {x}, then I …”'] }
  } : {
    stress: { l: 'Stress oder Nervosität', s: [
      'Achte auf Schultern, Kiefer und Atem. Sag dir innerlich: „Meine Hand will zum Mund.“',
      'Ball die Fäuste 3 Sekunden fest, lös sie und leg die Hände flach ab. 4 Sekunden ein, 6 Sekunden aus.',
      'Gib deinen Händen etwas zum Drücken: Knetball, Stift, die Tischkante. Unter Druck hilft festes Drücken mehr als Zappeln.',
      'Was hat den Stress gerade ausgelöst? Ein Wort reicht.'] },
    bored: { l: 'Langeweile', s: [
      'Langeweile ist leise. Warten, Scrollen und Fernsehen sind typische Momente. Bemerke heute einfach, wann es passiert.',
      'Leg die Hände 10 Sekunden flach ab und schau dir bewusst drei Dinge in deiner Umgebung an.',
      'Beschäftige deine Hände: Drehring, Knetball oder Handcreme einmassieren.',
      'Was hättest du gerade eigentlich gebraucht: Bewegung, Pause oder eine Beschäftigung?'] },
    focus: { l: 'Konzentriertes Arbeiten', s: [
      'Beim Nachdenken arbeitet die Hand oft allein. Ein Pflaster am Lieblingsfinger macht die Bewegung spürbar.',
      'Stift ablegen, Hände flach auf den Tisch, zwei lange Ausatmer.',
      'Gib der Denkhand etwas: Stift, Drehring, Knetball. Alle 25 Minuten eine kurze Hände-Pause.',
      'Bei welcher Aufgabe passiert es am häufigsten?'] },
    auto: { l: 'Ohne es zu merken', s: [
      'Das Ziel ist nicht Perfektion, sondern früheres Bemerken. Jedes Ertappen zählt, auch hinterher.',
      'Sobald du es merkst: Hand sanft zurück auf den Oberschenkel, kurz ausatmen. Kein Ärger.',
      'Ein „Wecker“ am Finger: Pflaster, Ring oder Bitterlack. Feile die Nägel glatt, damit keine Kante lockt.',
      'Wo warst du gerade, und was hast du getan? Notiere es kurz.'] },
    other: { l: '', s: [
      'Beobachte die Situation „{x}“ heute genau: Was passiert kurz bevor die Hand zum Mund geht?',
      'Ball die Fäuste 3 Sekunden, lös sie, Hände flach. 4 Sekunden ein, 6 Sekunden aus.',
      'Leg vorher fest, was deine Hände in dieser Situation tun: halten, drücken oder pflegen.',
      'Schreib dir einen Wenn-dann-Satz: „Wenn {x}, dann …“'] }
  };

  var el = function (tag, cls, txt) { var n = document.createElement(tag); if (cls) n.className = cls; if (txt != null) n.textContent = txt; return n; };

  function current() { var c = $('input[name="trigger"]:checked', form); return c ? c.value : null; }

  function render() {
    var k = current(); if (!k) return;
    if (T) { clearInterval(T); T = null; }
    other.classList.toggle('show', k === 'other');
    var x = (otherIn.value || '').trim().slice(0, 60) || X.fallback;
    var d = DATA[k];
    out.innerHTML = '';
    out.appendChild(el('span', 'eyebrow', X.title));
    out.appendChild(el('h3', null, X.forT + (k === 'other' ? x : d.l)));
    var ol = el('ol');
    d.s.forEach(function (s, i) {
      var li = el('li'); li.appendChild(el('b', null, X.steps[i])); li.appendChild(document.createTextNode(s.replace(/\{x\}/g, x))); ol.appendChild(li);
    });
    out.appendChild(ol);
    var row = el('div', 'btn-row');
    var b = el('button', 'btn btn-primary', X.start); b.type = 'button'; b.id = 'ex-start';
    var pr = el('a', 'btn btn-secondary', X.print); var sh = form.getAttribute('data-sheet') || 'arbeitsblatt/'; pr.setAttribute('href', location.protocol === 'file:' ? sh + 'index.html' : sh);
    row.appendChild(b); row.appendChild(pr); out.appendChild(row);
    out.appendChild(el('p', 'hint', X.hint)).style.marginTop = '14px';
    var tm = el('div', 'timer'); tm.id = 'ex-timer';
    tm.innerHTML = '<div class="ring" aria-hidden="true"><div>60</div></div><div class="breath" aria-hidden="true"></div><p class="cue" aria-live="polite"></p>';
    var stop = el('button', 'btn btn-secondary btn-sm', X.stop); stop.type = 'button'; tm.appendChild(stop);
    var rf = el('div', 'reflect'); rf.appendChild(el('p', 'cue', X.done));
    var rr = el('div', 'btn-row');
    ['less', 'same', 'more'].forEach(function (key) { var bb = el('button', 'btn btn-secondary btn-sm', X.r[key]); bb.type = 'button'; bb.setAttribute('data-r', key); rr.appendChild(bb); });
    rf.appendChild(rr); var msg = el('p', 'reflect-msg'); msg.setAttribute('aria-live', 'polite'); rf.appendChild(msg);
    out.appendChild(tm); out.appendChild(rf);
    b.addEventListener('click', function () { runTimer(tm, rf, b); });
    stop.addEventListener('click', function () { stopTimer(tm, b); });
    $$('[data-r]', rf).forEach(function (bb) { bb.addEventListener('click', function () { msg.textContent = X.msg[bb.getAttribute('data-r')]; }); });
  }

  var T = null;
  function stopTimer(tm, b) { if (T) { clearInterval(T); T = null; } tm.classList.remove('show'); if (b) { b.disabled = false; b.textContent = X.start; b.focus(); } }
  function runTimer(tm, rf, b) {
    if (T) clearInterval(T);
    rf.classList.remove('show'); tm.classList.add('show'); b.disabled = true;
    var ring = $('.ring', tm), num = $('.ring div', tm), cue = $('.cue', tm), br = $('.breath', tm);
    var t = 0, last = '';
    var setCue = function (c) { if (c !== last) { cue.textContent = c; last = c; } };
    var tick = function () {
      num.textContent = String(60 - t);
      ring.style.setProperty('--p', String(Math.round(t / 60 * 100)));
      ring.style.background = 'conic-gradient(var(--rose-light) ' + (t / 60 * 100) + '%, rgba(255,255,255,.08) 0)';
      if (t < 3) setCue(X.cues.fist);
      else if (t < 5) setCue(X.cues.release);
      else if (t < 8) setCue(X.cues.flat);
      else {
        var ph = (t - 8) % 10;
        if (ph < 4) { setCue(X.cues.inh); br.className = 'breath in'; } else { setCue(X.cues.exh); br.className = 'breath out'; }
      }
      if (t >= 60) {
        clearInterval(T); T = null; setCue(X.cues.end); br.className = 'breath';
        b.disabled = false; b.textContent = X.again; rf.classList.add('show');
        var first = $('[data-r]', rf); if (first) first.focus();
      }
      t++;
    };
    tick(); T = setInterval(tick, 1000);
    tm.scrollIntoView({ behavior: reduce ? 'auto' : 'smooth', block: 'nearest' });
  }

  form.addEventListener('change', function (e) { if (e.target && e.target.name === 'trigger') render(); });
  otherIn.addEventListener('input', function () { if (current() === 'other') render(); });
  form.addEventListener('submit', function (e) { e.preventDefault(); render(); });
})();
