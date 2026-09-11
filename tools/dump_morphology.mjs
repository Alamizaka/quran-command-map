import { loadMorphology } from 'quran-search-engine';
import fs from 'fs';
const m = await loadMorphology();
const out = {};
for (const [k,v] of m) out[k] = {roots:v.roots, lemmas:v.lemmas};
fs.writeFileSync('morph.json', JSON.stringify(out));
