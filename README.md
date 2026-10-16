# Ao Li — legacy website gateway

Ao Li’s current website is **[iamliao.com](https://iamliao.com/)**, covering tactile intelligence, embodied robotics, publications and experience.

This repository preserves the previous GitHub Pages site’s assets and provides redirects from its old HTML entry points. The current website’s source is maintained separately in a local project and is not published in this repository.

## Maintain the redirects

Edit the explicit mapping in `scripts/generate_redirects.py`, then run:

```sh
python3 scripts/generate_redirects.py
```

Only the listed HTML files are generated. Existing assets, `LICENSE`, and GitHub Pages configuration are preserved. No wildcard path rewriting is used; project sites such as `/xhs-studio/` keep their own routing and deployment.

The legacy CV, teaching, services and awards URLs lead to the current experience page. This routing does not imply a separate awards or services section on the new site.
