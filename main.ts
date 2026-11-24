// Entry point for the news-image-20261124 submission.
//
// The poster itself is rendered at build time by draw_poster.py and
// committed as entry.png beside this file. At grade time this program
// does the smallest honest job possible: it copies that committed
// image to the output directory the harness asks for, byte for byte,
// with no network, no randomness and no third-party code — only the
// Node 22 standard library.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const source = join(here, "entry.png");
const targetDir = process.env.MAKEFUN_OUTPUT_DIR || "/output";
const target = join(targetDir, "entry.png");

try {
  mkdirSync(targetDir, { recursive: true });
  copyFileSync(source, target);
} catch (err) {
  const reason = err instanceof Error ? err.message : String(err);
  console.error(
    `news-image-20261124: cannot copy ${source} to ${target}: ${reason}`,
  );
  process.exit(1);
}

console.log(`news-image-20261124: wrote ${target}`);
