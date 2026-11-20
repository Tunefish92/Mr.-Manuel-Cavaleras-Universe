"""Convert downloaded json3 subtitle tracks into one timestamped Markdown transcript per video."""
import glob
import json
import os
import re
import sys

root, out = sys.argv[1], sys.argv[2]
order = [line.split('|')[0] for name in ('list_videos.txt', 'list_shorts.txt') for line in open(os.path.join(root, name), encoding='utf-8')]
labels = {'de': 'Deutsch (vom Kanal)', 'de-AT': 'Dialekt (vom Kanal)', 'de-DE': 'Hochdeutsch (vom Kanal)', 'en': 'Englisch (vom Kanal)', 'en-US': 'Englisch (vom Kanal)'}


def lines(path):
    """Return (seconds, text) pairs of one json3 track, merging rolling auto-caption segments."""
    result = []
    for event in json.load(open(path, encoding='utf-8')).get('events', []):
        text = ''.join(seg.get('utf8', '') for seg in event.get('segs', []))
        text = re.sub(r'\s+', ' ', text).strip()
        if text:
            result.append((event.get('tStartMs', 0) // 1000, text))
    return result


def slug(title):
    """Build a file-name-safe slug from a video title."""
    return re.sub(r'[^a-z0-9]+', '-', title.lower().replace('ä', 'ae').replace('ö', 'oe').replace('ü', 'ue').replace('ß', 'ss')).strip('-')[:60]


index = []
for number, vid in enumerate(order, 1):
    info = json.load(open(f'{root}/dl/{vid}.info.json', encoding='utf-8'))
    tracks = []
    for path in sorted(glob.glob(f'{root}/subs_manual/{vid}.*.json3')):
        lang = path.split('.')[-2]
        tracks.append((labels.get(lang, lang), lines(path)))
    for path in sorted(glob.glob(f'{root}/subs_auto/{vid}.*.json3')):
        lang = path.split('.')[-2]
        tracks.append((f'Automatisch erkannt ({lang.replace("-orig", "")})', lines(path)))
    tracks = [track for track in tracks if track[1]]
    date = info['upload_date']
    date = f'{date[:4]}-{date[4:6]}-{date[6:]}'
    name = f'{date}_{slug(info["title"])}_{vid}.md'
    body = [f'# {info["title"]}', '', f'- Video: https://www.youtube.com/watch?v={vid}', f'- Veröffentlicht: {date}', f'- Länge: {info.get("duration_string", "?")}', '']
    if (info.get('description') or '').strip():
        body += ['## Beschreibung', '', info['description'].strip(), '']
    if not tracks:
        body += ['Keine Untertitel vorhanden.', '']
    for label, rows in tracks:
        body += [f'## {label}', '']
        body += [f'- `{sec // 60}:{sec % 60:02d}` {text}' for sec, text in rows]
        body.append('')
    open(os.path.join(out, name), 'w', encoding='utf-8').write('\n'.join(body))
    index.append((date, info['title'], vid, name, ', '.join(label for label, _ in tracks) or 'keine'))

with open(os.path.join(out, 'README.md'), 'w', encoding='utf-8') as handle:
    handle.write('# Transkripte\n\nUntertitel aller Videos des Kanals, Stand 2026-11-20. Die Texte gehören Manuel Cavaleras.\n\n| Datum | Video | Spuren |\n|---|---|---|\n')
    for date, title, vid, name, kinds in sorted(index, reverse=True):
        handle.write(f'| {date} | [{title}]({name}) | {kinds} |\n')
print(len(index), 'files')
