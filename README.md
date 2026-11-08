# Story Studio companion book

This is the separate public-facing mdBook for the envisioned Story Studio writer experience. The Studio application remains private and experimental. Available/Prototype/Envisioned labels distinguish demonstrated behavior from future interactions. No Studio application source or private research is included.

## Local preview

Use the existing mdBook starter and frontmatter preprocessor:

```sh
mdbook build
mdbook serve
```

Prerequisites: `mdbook` and `mdbook-frntmtr` on PATH. The foundation was built with mdbook 0.5.2 and the installed `mdbook-frntmtr`. Source is `booksrc/`; configured output is `gh-pages/docs/`. Chapter frontmatter and `{{ page.title }}` use the starter’s preprocessor. Existing Python maintenance tools are retained; they are not required just to read or build this foundation.

The first three chapters are written. Later chapters are explicitly outlines. The borrowed-umbrella walkthrough was executed in the real private application on 8 November 2026, with fictional sample data. Its embedded PNGs are authentic browser captures and readable crops, not mockups. Re-run affected examples and refresh screenshots whenever the UI changes; do not relabel a mockup as a working screenshot.

## Publication status

Prepared locally; **not published**. No Git remote or confirmed GitHub destination existed during preparation. The starter’s old README URL was not treated as destination authorization. Studio is not part of this book repository and must not be published with it.

The existing `deploy` helper builds, audits assets, and **force-pushes an orphan commit to `origin gh-pages`**, using `/docs` for GitHub Pages. It requires an initialized source history and a confirmed remote. Do not run it until the destination and public action are explicitly authorized. Once configured and authorized, review `uv run deploy --dry-run` first; the dry run builds/audits and does not push. No publication command has been executed for this foundation.
