import json, collections, sys
sys.path.insert(0, '/home/user/quran')
from concepts import C, CATEGORIES

m = json.load(open('/home/user/quran/morph.json'))
q = json.load(open('/home/user/quran/node_modules/quran-json/dist/quran_en.json'))
verses = {}  # gid -> dict
g = 0
for s in q:
    for v in s['verses']:
        g += 1
        verses[g] = dict(gid=g, s=s['id'], a=v['id'], sname=s['transliteration'], ar=v['text'], en=v['translation'])
all_lemmas = set()
for v in m.values(): all_lemmas.update(v['lemmas'])

missing = []
for con in C:
    for l in con['lemmas']:
        if l not in all_lemmas: missing.append((con['id'], l))
print('MISSING LEMMAS:', missing)

used = set()
out_nodes = []
for con in C:
    ls = set(con['lemmas'])
    vids = []; tok = 0
    for gid, v in m.items():
        n = sum(1 for l in v['lemmas'] if l in ls)
        if n:
            vids.append(int(gid)); tok += n
    ref2gid={(v['s'],v['a']):g for g,v in verses.items()}
    for r in con.get('refs',[]):
        a,b=map(int,r.split(':')); gid=ref2gid[(a,b)]
        if gid not in vids: vids.append(gid); tok+=1
    vids.sort()
    used.update(vids)
    node = {k: con[k] for k in ('id','ar','en','root','pol','cat','opposite','key','note')}
    node['lemmas'] = con['lemmas']
    node['verses'] = vids
    node['count'] = len(vids)
    node['tokens'] = tok
    out_nodes.append(node)

out_verses = {str(g): verses[g] for g in sorted(used)}
data = dict(categories=CATEGORIES, nodes=out_nodes, verses=out_verses,
            meta=dict(text='Uthmani text (quranenc.com via quran-json 3.1.2)', translation='Saheeh International (tanzil.net)', morphology='Quranic Arabic Corpus lemmas (via quran-search-engine)', total_verses=6236))
json.dump(data, open('/home/user/quran/data.json','w'), ensure_ascii=False)
print('nodes', len(out_nodes), 'verses used', len(out_verses))
for n in sorted(out_nodes, key=lambda x: -x['count']):
    print(f"{n['count']:4d} {n['tokens']:4d}  {n['pol']:6s} {n['cat']:9s} {n['id']:12s} {n['ar']}")
