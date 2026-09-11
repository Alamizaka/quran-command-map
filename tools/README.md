Rebuild pipeline (Python 3 + Node):

1. `npm install quran-json@3.1.2 quran-search-engine` — gives the Uthmani text + Saheeh International (quran-json) and the Quranic Arabic Corpus lemmas (quran-search-engine).
2. Dump the per-verse lemma map to `morph.json` (see `dump2.mjs` logic: iterate `loadMorphology()` Map → `{gid: {roots, lemmas}}`).
3. Edit `concepts.py` — each concept is a set of Arabic lemmas (spelled as the corpus spells them) plus optional explicit verse refs.
4. `python3 build.py` → `data.json`.
5. Inject `data.json` into `page_template.html` at `__DATA__` → `index.html`.
