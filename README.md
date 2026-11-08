# Story Studio companion book

Public book: https://kkibria.github.io/storybuilderbook/ — [English](https://kkibria.github.io/storybuilderbook/) · [বাংলা](https://kkibria.github.io/storybuilderbook/bn/).

Studio itself remains private and experimental. Available/Prototype/Envisioned labels separate demonstrated behavior from future ideas. No Studio source, private research, credentials or user database is part of this book.

## Build and preview both editions

```sh
uv run bookbuild
uv run bookserve
```

The preview binds only to `127.0.0.1:3000`; use `--port 3001` if needed. It builds on startup; restart it after editing. Requires `mdbook` and `mdbook-frntmtr` on PATH. The existing frontmatter preprocessor is retained. `mdbook build` alone builds English only; use `bookbuild` for both editions.

English source stays in `booksrc/` and keeps its existing URLs. Bangla source is `booksrc-bn/`, configured by `editions/bn/book.toml`, built into `gh-pages/docs/bn/`. Every chapter links to its corresponding page in the other edition. The first three chapters are complete; later chapters remain outlines. Both beginner exercises and authentic screenshots were verified on 8 November 2026, including saved properties, interface switching, Bangla text and the complete story. Refresh affected examples/images when UI behavior changes.

## Deploy through the existing workflow

```sh
uv run deploy --dry-run
uv run deploy
```

Deployment now builds English and Bangla before applying the existing asset audit. A failed build prevents publication. The established helper force-pushes an orphan `gh-pages` artifact commit to this book repository’s `origin`; GitHub Pages uses `gh-pages` and `/docs`. This is a public action. Keep the Studio repository separate. The source history remains on `main`.
