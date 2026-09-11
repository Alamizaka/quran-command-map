#!/usr/bin/env python3
"""Download tafsir entries from the quran.com v4 API for every verse used in data.json
and store them as tafsir/<tafsir_id>/<surah>.json  ({ayah: html}).
Run from the repo root:  python3 tools/fetch_tafsir.py 169 16
(169 = Ibn Kathir EN abridged, 14 = Ibn Kathir AR, 16 = Muyassar AR, 91 = Sa'di, 15 = Tabari, 90 = Qurtubi, 168 = Ma'arif)
"""
import json, sys, os, urllib.request, concurrent.futures, time
ids = [int(x) for x in sys.argv[1:]] or [169, 16]
d = json.load(open('data.json'))
verses = sorted({(v['s'], v['a']) for v in d['verses'].values()})
print(len(verses), 'verses')
def get(url, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'quran-command-map'}), timeout=30) as r:
                return json.load(r)
        except Exception as e:
            time.sleep(1.5 * (i + 1))
    return None
for tid in ids:
    out = {}
    os.makedirs(f'tafsir/{tid}', exist_ok=True)
    def work(sa):
        s, a = sa
        j = get(f'https://api.quran.com/api/v4/tafsirs/{tid}/by_ayah/{s}:{a}')
        return s, a, ((j or {}).get('tafsir') or {}).get('text', '') if j else None
    done = 0
    with concurrent.futures.ThreadPoolExecutor(6) as ex:
        for s, a, text in ex.map(work, verses):
            if text is None: print('FAILED', tid, f'{s}:{a}'); continue
            out.setdefault(s, {})[a] = text
            done += 1
            if done % 200 == 0: print(tid, done, '/', len(verses))
    for s, m in out.items():
        json.dump(m, open(f'tafsir/{tid}/{s}.json', 'w'), ensure_ascii=False)
    print('tafsir', tid, 'saved', done, 'entries,', sum(os.path.getsize(f'tafsir/{tid}/{f}') for f in os.listdir(f'tafsir/{tid}')) // 1024, 'KB')
