#!/usr/bin/env python3
"""Regenerate the explicitly listed legacy HTML entry points."""

from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
REDIRECTS = {
    "index.html": ("https://iamliao.com/", "Ao Li’s website"),
    "publications/index.html": ("https://iamliao.com/publications/", "Publications"),
    "cv/index.html": ("https://iamliao.com/experience/", "Experience and CV"),
    "teaching/index.html": ("https://iamliao.com/experience/", "Experience and teaching"),
    "services/index.html": ("https://iamliao.com/experience/", "Experience"),
    "awards/index.html": ("https://iamliao.com/experience/", "Experience"),
    "404.html": ("https://iamliao.com/", "Ao Li’s website"),
    "404/index.html": ("https://iamliao.com/", "Ao Li’s website"),
}

TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta http-equiv="refresh" content="3; url={url}">
  <link rel="canonical" href="{url}">
  <title>{title} — New address</title>
  <meta name="description" content="Ao Li’s website has moved to iamliao.com.">
  <style>
    :root {{ color-scheme: light dark; font-family: system-ui, sans-serif; }}
    body {{ max-width: 40rem; margin: 12vh auto; padding: 1.5rem; line-height: 1.6; }}
    h1 {{ font-size: 1.8rem; line-height: 1.25; }}
    a {{ color: #086e99; text-underline-offset: .2em; overflow-wrap: anywhere; }}
    a:focus-visible {{ outline: 3px solid currentColor; outline-offset: 4px; }}
    @media (prefers-color-scheme: dark) {{ a {{ color: #80d8ff; }} }}
  </style>
</head>
<body>
  <main>
    <h1>Ao Li’s website has moved</h1>
    <p>You will be redirected to the new website in a few seconds.</p>
    <p><a href="{url}">Continue to {title} →</a></p>
    <p lang="zh-CN">李敖的个人网站已迁至新地址，稍后将自动跳转。也可以点击上方链接访问。</p>
    <p><a href="{url}">{url}</a></p>
  </main>
</body>
</html>
"""


def main():
    for path, (url, title) in REDIRECTS.items():
        (ROOT / path).write_text(
            TEMPLATE.format(url=escape(url, quote=True), title=escape(title)),
            encoding="utf-8",
        )


if __name__ == "__main__":
    main()
