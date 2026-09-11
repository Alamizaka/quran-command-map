# خريطة الأمر والنهي — What the Quran commands, what it forbids

An interactive star map of the Quran's virtues and prohibitions.
104 concepts, gold for what the text commands or praises, red for what it forbids or condemns,
grouped into eight clusters (belief, worship, character, the tongue, money, family & sex, food & drink, blood & aggression).
Star size = number of distinct verses in which the concept's Arabic word appears. Click a star to read every one of those verses,
Uthmani Arabic with Saheeh International underneath. Dotted lines join a virtue to its opposite. A sortable table view is included.

**Live:** open `index.html` in any browser, or enable GitHub Pages on this repo.

## How the counting works

Nothing here is counted in English. Each concept is a hand-curated set of Arabic lemmas
(e.g. الصبر = صبر، صابر، صبّار) matched against the Quranic Arabic Corpus morphology of the Uthmani text.
"Verses" = distinct verses containing any of the lemmas; "occurrences" = total tokens.

Where one Arabic word carries two meanings the count is left as the text has it and the node says so:
كذب is mostly "denying revelation", not "telling lies"; قتل covers murder and battle alike; خمر is wine in 5:90 and head-coverings in 24:31.
A few prohibitions have no dedicated word (bribery, severing kinship, meat slaughtered for other than God, false accusation of chaste women);
those stars are built from explicit verse lists and are small by construction. The full definitions are in `tools/concepts.py`.

Sanity checks against standard concordances: ص-ب-ر 103 tokens, الزكاة 32 verses, الربا in 2:275–279, 3:130, 4:161, 30:39.

This is a word-frequency map of one text, not a fiqh ruling. Most detailed rulings live in hadith and the legal schools, which are not included.

## Sources and attribution

- Uthmani Quran text: The Noble Qur'an Encyclopedia (quranenc.com), packaged by [quran-json](https://www.npmjs.com/package/quran-json) v3.1.2 (CC-BY-4.0).
- English translation: Saheeh International (Umm Muhammad), via [Tanzil.net](https://tanzil.net/trans/en.sahih). Tanzil asks that translations be attributed and reproduced unmodified; they are reproduced here verbatim.
- Morphology (lemmas): the [Quranic Arabic Corpus](https://corpus.quran.com) (Kais Dukes, University of Leeds), GPL, as bundled by [quran-search-engine](https://www.npmjs.com/package/quran-search-engine) (MIT).
- Rendering: [D3.js](https://d3js.org) v7 (ISC), loaded from cdnjs. Fonts: Amiri, Spectral, IBM Plex Mono via Google Fonts.

## License

Code (`index.html`, `tools/`): MIT. The Quran text, translation and morphology data keep their own licenses listed above.
