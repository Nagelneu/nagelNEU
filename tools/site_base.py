"""NagelNEU · Website-Bausteine (Kopf, Fuß, Metadaten).

Alle Seiten werden mit `python3 tools/build.py` erzeugt. Wer keine Python-Umgebung hat,
kann die fertigen HTML-Dateien auch direkt bearbeiten; beim nächsten Bauen werden sie
allerdings überschrieben.
"""
import html
import json
import os

# ------------------------------------------------------------------
# Zentrale Einstellungen
# ------------------------------------------------------------------
SITE = "https://nagelneu.github.io/nagelNEU/"   # öffentliche Adresse, mit Schrägstrich am Ende
BASE_PATH = "/nagelNEU/"                         # Pfad-Anteil der Adresse (für die 404-Seite)
YT_URL = "https://www.youtube.com/@fingern%C3%A4gelkauen"
YT_NAME = "@fingernägelkauen"
AUTHOR = "Frank Zimmermann"
UPDATED = "2026-10-22"
GSC_VERIFICATION = ""   # Google Search Console: Code aus dem HTML-Tag hier eintragen, dann neu bauen
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

E = html.escape


def rel(path):
    """Relativer Weg von einer Seite (z. B. 'en/worksheet/') zur Wurzel."""
    depth = len([p for p in path.split("/") if p])
    return "../" * depth


NAV = {
    "de": [
        ("haende-stopp/", "Methode"),
        ("21-tage-programm/", "21-Tage-Programm"),
        ("naegelkauen-abgewoehnen/", "Ratgeber"),
        ("#faq", "Fragen"),
    ],
    "en": [
        ("en/#method", "Method"),
        ("en/#programme", "Programme"),
        ("en/#faq", "FAQ"),
    ],
}

LOGO_SVG = (
    '<svg viewBox="0 0 32 32" width="30" height="30" aria-hidden="true" focusable="false">'
    '<rect width="32" height="32" rx="9" fill="#c21f5b"/>'
    '<path d="M11 24V12.5a5 5 0 0 1 10 0V24" fill="none" stroke="#fff" stroke-width="2.6" stroke-linecap="round"/>'
    '<path d="M13.2 13.2a2.8 2.6 0 0 1 5.6 0" fill="#fff" opacity=".9"/>'
    "</svg>"
)


def logo(r, lang):
    href = r + ("en/" if lang == "en" else "")
    return f'<a class="logo" href="{href or "./"}" aria-label="NagelNEU {"home page" if lang == "en" else "Startseite"}">{LOGO_SVG}<span class="brand-mark">Nagel<b>NEU</b></span></a>'


def header(path, lang, active=None, alt_path=None):
    r = rel(path)
    items = []
    home = path in ("", "en/")
    for href, label in NAV[lang]:
        if href.startswith("#"):
            url = (r + href) if not home else href
        elif href.startswith("en/#"):
            url = href[3:] if path == "en/" else r + href
        else:
            url = r + href
        cur = ' aria-current="page"' if active and href == active else ""
        items.append(f'<a href="{url}"{cur}>{label}</a>')
    if lang == "de":
        other = r + (alt_path if alt_path is not None else "en/")
        items.append(f'<a class="lang" href="{other}" hreflang="en" lang="en" aria-label="English version">EN</a>')
        items.append(f'<a class="btn btn-primary btn-sm" href="{r}app/">App öffnen</a>')
        menu = "Menü"
    else:
        other = r + (alt_path if alt_path is not None else "")
        items.append(f'<a class="lang" href="{other or "../"}" hreflang="de" lang="de" aria-label="Deutsche Version">DE</a>')
        items.append(f'<a class="btn btn-primary btn-sm" href="{r}app/?lang=en">Open the app</a>')
        menu = "Menu"
    skip = "Zum Inhalt springen" if lang == "de" else "Skip to content"
    return f"""<a class="skip" href="#main">{skip}</a>
<header class="site-header">
  <div class="wrap hdr">
    {logo(r, lang)}
    <button class="nav-toggle" type="button" aria-controls="nav" aria-expanded="false"><span></span><span class="vh">{menu}</span></button>
    <nav id="nav" class="nav" aria-label="{'Hauptnavigation' if lang == 'de' else 'Main navigation'}">
      {"".join(items)}
    </nav>
  </div>
</header>"""


def footer(path, lang):
    r = rel(path)
    if lang == "de":
        return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="ft-grid">
      <div class="ft-brand">
        {logo(r, 'de')}
        <p>Erst bemerken. Dann neu entscheiden.<br>Ein kostenloser Begleiter für Erwachsene, die das Nägelkauen verändern möchten.</p>
        <p><a href="{YT_URL}" rel="noopener" target="_blank">YouTube {YT_NAME}</a></p>
      </div>
      <div>
        <h2>Programm</h2>
        <ul>
          <li><a href="{r}haende-stopp/">HÄNDE-STOPP-Methode</a></li>
          <li><a href="{r}21-tage-programm/">21-Tage-Programm</a></li>
          <li><a href="{r}app/">App öffnen</a></li>
          <li><a href="{r}arbeitsblatt/">Arbeitsblatt zum Ausdrucken</a></li>
        </ul>
      </div>
      <div>
        <h2>Ratgeber</h2>
        <ul>
          <li><a href="{r}naegelkauen-abgewoehnen/">Nägelkauen abgewöhnen</a></li>
          <li><a href="{r}warum-kaue-ich-naegel/">Warum kaue ich Nägel?</a></li>
          <li><a href="{r}naegelkauen-bei-stress/">Nägelkauen bei Stress</a></li>
        </ul>
      </div>
      <div>
        <h2>Rechtliches</h2>
        <ul>
          <li><a href="{r}impressum/">Impressum</a></li>
          <li><a href="{r}datenschutz/">Datenschutz</a></li>
          <li><a href="{r}en/" hreflang="en" lang="en">English</a></li>
        </ul>
      </div>
    </div>
    <div class="ft-bottom">
      <span>Design by Frank Zimmermann © 2026 · Alle Rechte vorbehalten</span>
      <span>NagelNEU ist ein Selbsthilfe-Begleiter und keine medizinische Behandlung.</span>
    </div>
  </div>
</footer>"""
    return f"""<footer class="site-footer">
  <div class="wrap">
    <div class="ft-grid">
      <div class="ft-brand">
        {logo(r, 'en')}
        <p>Notice first. Then decide anew.<br>A free companion for adults who want to change their nail-biting habit.</p>
        <p><a href="{YT_URL}" rel="noopener" target="_blank">YouTube {YT_NAME}</a></p>
      </div>
      <div>
        <h2>Programme</h2>
        <ul>
          <li><a href="{r}en/#method">HANDS STOP method</a></li>
          <li><a href="{r}en/#programme">21-day programme</a></li>
          <li><a href="{r}app/?lang=en">Open the app</a></li>
          <li><a href="{r}en/worksheet/">Printable worksheet</a></li>
        </ul>
      </div>
      <div>
        <h2>Guides (German)</h2>
        <ul>
          <li><a href="{r}naegelkauen-abgewoehnen/" hreflang="de" lang="de">Nägelkauen abgewöhnen</a></li>
          <li><a href="{r}warum-kaue-ich-naegel/" hreflang="de" lang="de">Warum kaue ich Nägel?</a></li>
          <li><a href="{r}naegelkauen-bei-stress/" hreflang="de" lang="de">Nägelkauen bei Stress</a></li>
        </ul>
      </div>
      <div>
        <h2>Legal</h2>
        <ul>
          <li><a href="{r}impressum/" hreflang="de">Legal notice (Impressum)</a></li>
          <li><a href="{r}datenschutz/" hreflang="de">Privacy policy (Datenschutz)</a></li>
          <li><a href="{r}" hreflang="de" lang="de">Deutsch</a></li>
        </ul>
      </div>
    </div>
    <div class="ft-bottom">
      <span>Design by Frank Zimmermann © 2026 · All rights reserved</span>
      <span>NagelNEU is a self-help companion, not medical treatment.</span>
    </div>
  </div>
</footer>"""


def org_ld():
    return {
        "@type": "Organization",
        "@id": SITE + "#org",
        "name": "NagelNEU",
        "url": SITE,
        "logo": SITE + "assets/img/logo-512.png",
        "sameAs": [YT_URL],
        "founder": {"@type": "Person", "name": AUTHOR},
    }


def breadcrumb_ld(items):
    return {
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": n, "item": SITE + p} for i, (n, p) in enumerate(items)
        ],
    }


def page(path, lang, title, desc, body, *, active=None, alternates=None, ld=None, robots="index, follow",
         og_type="website", og_image="assets/img/og-image.png", extra_head="", body_class="", alt_path=None):
    """Schreibt eine komplette Seite nach ROOT/path/index.html (oder ROOT/path bei .html)."""
    r = rel(path) if not path.endswith(".html") else ""
    if lang == "en" and og_image == "assets/img/og-image.png":
        og_image = "assets/img/og-image-en.png"
    url = SITE + path
    alt_links = ""
    if alternates:
        for hl, p in alternates.items():
            alt_links += f'\n<link rel="alternate" hreflang="{hl}" href="{SITE + p}">'
    graph = [org_ld()] + (ld or [])
    ld_json = json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)
    gsc = f'\n<meta name="google-site-verification" content="{E(GSC_VERIFICATION)}">' if GSC_VERIFICATION and path == "" else ""
    locale = "de_DE" if lang == "de" else "en_GB"
    doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{E(title)}</title>
<meta name="description" content="{E(desc)}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">{alt_links}
<meta name="author" content="{AUTHOR}">
<meta name="theme-color" content="#fbf7f2">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="NagelNEU">
<meta property="og:locale" content="{locale}">
<meta property="og:title" content="{E(title)}">
<meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE + og_image}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="NagelNEU: {'Erst bemerken. Dann neu entscheiden.' if lang == 'de' else 'Notice first. Then decide anew.'}">
<meta name="twitter:card" content="summary_large_image">{gsc}
<link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
<link rel="icon" href="{r}assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="{r}assets/img/apple-touch-icon.png">
<link rel="preload" href="{r}assets/fonts/archivo-var.woff" as="font" type="font/woff" crossorigin>
<link rel="stylesheet" href="{r}assets/css/site.css">{extra_head}
<script type="application/ld+json">
{ld_json}
</script>
</head>
<body data-root="{r}"{(' class="' + body_class + '"') if body_class else ''}>
{header(path, lang, active, alt_path)}
<main id="main">
{body}
</main>
{footer(path, lang)}
<script src="{r}assets/js/site.js" defer></script>
</body>
</html>
"""
    out = os.path.join(ROOT, path if path.endswith(".html") else os.path.join(path, "index.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(typo_html(doc))
    return out


def img(r, name, alt="", w=120, h=160, cls="", lazy=True):
    return (f'<img src="{r}assets/img/{name}" alt="{E(alt)}" width="{w}" height="{h}"'
            f'{" class=" + chr(34) + cls + chr(34) if cls else ""}{" loading=" + chr(34) + "lazy" + chr(34) if lazy else ""} decoding="async">')


# ------------------------------------------------------------------
# Typografie: geschützte Leerzeichen zwischen Zahl und Einheit, bei
# Abkürzungen und Marken. Wird nur auf sichtbaren Text angewendet.
# ------------------------------------------------------------------
import re as _re
_NB = "\u00a0"
_UNITS = (r"Minuten|Minute|Sekunden|Sekunde|Tagen|Tage|Tag|Wochen|Woche|Monaten|Monate|Monat|Stunden|Stunde|Std\.?|"
          r"Min\.?|Sek\.?|mm|cm|Millimeter|Uhr|Punkte|Prozent|%|Zeichen|minutes|minute|seconds|second|days|day|"
          r"weeks|week|months|month|hours|hour|hrs|points")
_TYPO = [
    (_re.compile(r"(\d)\s(?=(?:" + _UNITS + r")(?![A-Za-zÄÖÜäöüß]))"), r"\1" + _NB),
    (_re.compile(r"(^|[\s(])(Tag|Day|Nr\.|No\.|Art\.|Abs\.|§|Phase|Stufe|Level|Seite|Page|Woche|Week|Schritt|Step)\s(?=\d)"), r"\1\2" + _NB),
    (_re.compile(r"\bz\.\s?B\."), "z." + _NB + "B."),
    (_re.compile(r"\bd\.\s?h\."), "d." + _NB + "h."),
    (_re.compile(r"©\s(?=\d)"), "©" + _NB),
    (_re.compile(r"0800\s111\s0\s111"), "0800" + _NB + "111" + _NB + "0" + _NB + "111"),
    (_re.compile(r"\.\.\."), "…"),
]


def typo_text(t):
    for rx, rp in _TYPO:
        t = rx.sub(rp, t)
    return t


def typo_html(doc):
    """Wendet die Typografie nur auf Text zwischen Tags an, nicht in script/style/Attributen."""
    out, pos, skip = [], 0, None
    for m in _re.finditer(r"<[^>]+>", doc):
        text = doc[pos:m.start()]
        out.append(text if skip else typo_text(text))
        tag = m.group(0)
        low = tag.lower()
        if skip and low.startswith("</" + skip):
            skip = None
        elif low.startswith("<script") or low.startswith("<style"):
            skip = "script" if low.startswith("<script") else "style"
        out.append(tag)
        pos = m.end()
    out.append(typo_text(doc[pos:]))
    return "".join(out)
