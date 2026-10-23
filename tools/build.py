"""NagelNEU · baut alle statischen Seiten, robots.txt und sitemap.xml.

Aufruf (im Projektordner):  python3 tools/build.py
Die App unter app/ wird dabei nicht verändert.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_base import ROOT, SITE, UPDATED  # noqa: E402
from pages_home import home_de, home_en  # noqa: E402
from pages_program import program_de, method_de  # noqa: E402
from pages_guides import build_guides  # noqa: E402
from pages_misc import build_misc  # noqa: E402

SITEMAP = [
    ("", "1.0", {"de": "", "en": "en/"}),
    ("en/", "0.8", {"de": "", "en": "en/"}),
    ("haende-stopp/", "0.9", None),
    ("21-tage-programm/", "0.9", None),
    ("naegelkauen-abgewoehnen/", "0.8", None),
    ("warum-kaue-ich-naegel/", "0.8", None),
    ("naegelkauen-bei-stress/", "0.8", None),
    ("arbeitsblatt/", "0.6", {"de": "arbeitsblatt/", "en": "en/worksheet/"}),
    ("en/worksheet/", "0.5", {"de": "arbeitsblatt/", "en": "en/worksheet/"}),
    ("app/", "0.7", None),
]


def write(name, text):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(text)


def main():
    home_de()
    home_en()
    program_de()
    method_de()
    build_guides()
    build_misc()

    write("robots.txt", f"""User-agent: *
Allow: /
Disallow: /docs/
Disallow: /tools/
Disallow: /server/
Disallow: /tagebuch-einbetten.html

Sitemap: {SITE}sitemap.xml
""")

    urls = []
    for path, prio, alts in SITEMAP:
        alt = ""
        if alts:
            alt = "".join(f'\n    <xhtml:link rel="alternate" hreflang="{hl}" href="{SITE + p}"/>' for hl, p in alts.items())
        urls.append(f"""  <url>
    <loc>{SITE + path}</loc>
    <lastmod>{UPDATED}</lastmod>
    <priority>{prio}</priority>{alt}
  </url>""")
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n'
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">\n'
          + "\n".join(urls) + "\n</urlset>\n")
    print("Fertig: Seiten, robots.txt und sitemap.xml erzeugt.")


if __name__ == "__main__":
    main()
