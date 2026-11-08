"""Build both public book editions before audit/deployment; no Studio dependencies."""
import argparse
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import subprocess
import tomllib


def build_editions(root: Path) -> Path:
    root = root.resolve()
    config = tomllib.loads((root / "book.toml").read_text())
    output = root / config["build"]["build-dir"]
    subprocess.run(["mdbook", "build", str(root)], check=True)
    bangla = root / "editions/bn/book.toml"
    if bangla.exists():
        subprocess.run(["mdbook", "build", str(bangla.parent), "--dest-dir", str(output / "bn")], check=True)
    return output


def main() -> int:
    build_editions(Path.cwd())
    return 0


def serve() -> int:
    parser = argparse.ArgumentParser(description="Build and preview both book editions locally.")
    parser.add_argument("--port", type=int, default=3000)
    args = parser.parse_args()
    root = Path.cwd()
    output = build_editions(root)
    config = tomllib.loads((root / "book.toml").read_text())
    prefix = config.get("output", {}).get("html", {}).get("site-url", "/").rstrip("/")
    class Handler(SimpleHTTPRequestHandler):
        def translate_path(self, path):
            if prefix and (path == prefix or path.startswith(prefix + "/")):
                path = path[len(prefix):] or "/"
            return super().translate_path(path)
    with ThreadingHTTPServer(("127.0.0.1", args.port), partial(Handler, directory=str(output))) as server:
        print(f"Book preview: http://127.0.0.1:{args.port}/ — English / Bangla; rebuild after edits.", flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0
