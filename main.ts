// gta6-meme-x-01 v7 entry (Node 22, standard library only).
//
// The entry is the X post itself: a GTA 6 jury-duty meme posted from a public
// account with make.fun / @makefunai and the play code in its text. This program
// only hands the house the post's address: it copies POST.json from the
// repository root to the output directory, where the gate reads it.
//
//   MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
//
// No network, no wall clock, no files outside the repository. The two runs of
// an entry must write the same bytes: this program is deterministic.

import { copyFileSync, mkdirSync, readFileSync } from "node:fs";
import { join } from "node:path";

const botDir = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const outputDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

mkdirSync(outputDir, { recursive: true });
const source = join(botDir, "POST.json");
const target = join(outputDir, "POST.json");
copyFileSync(source, target);

// Read-back self-check: the copy must be byte-identical to the source.
// A silent partial write would hand the gate a corrupt POST.json.
const written = readFileSync(target);
const expected = readFileSync(source);
if (!written.equals(expected)) {
  console.error(`POST.json copy mismatch: wrote ${written.length} bytes, expected ${expected.length}`);
  process.exit(1);
}
