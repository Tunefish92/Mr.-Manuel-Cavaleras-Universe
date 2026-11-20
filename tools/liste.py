"""Write figuren/README.md: one row per still with character, video and time stamp, grouped by world."""
import json
import sys

rows = {name: (vid, sec, title) for name, vid, sec, title in json.load(open(sys.argv[1], encoding='utf-8'))}
worlds = [
    ('Herberts Show', [
        ('herbert-brunnthaler', 'Herbert Brunnthaler', 'Stellt sich als „Brunnthaler Herbert“ vor'),
        ('hildegard', 'Hildegard', 'Herberts Frau'),
        ('heidi-die-kuh', 'Heidi', 'Die Kuh, von einer Katze aufgezogen; Bärbel nennt sie „Frau Kätzchen-Kuh“'),
        ('baerbel-unterranacher', 'Bärbel Unterranacher', 'Das Nachbarsmädchen'),
        ('osterhase', 'Der Osterhase', 'Von Bärbel auf der Straße „gefunden“'),
        ('alfons', 'Alfons', 'Herberts Freund aus Wien'),
        ('herberts-vater', 'Herberts Vater', 'Auf dem Skifoto, beschriftet mit „Vader“'),
        ('englische-lady', 'Die englische Lady', 'Fragt im Freundlichkeits-Beweis nach der Kirche'),
        ('nikolaus', 'Der Nikolaus', 'In Herberts Erinnerung „a very sick man“'),
        ('herbert-als-krampus-und-pichler-jakob', 'Herbert als Krampus und Pichler Jakob', 'Im Bild beschriftet: „Me“ und „Pichler Jakob“'),
        ('herberts-cousin', 'Herberts Cousin', 'Gegner bei der Krampus-Vorführung'),
    ]),
    ('Das Tiroler Dorf', [
        ('ruppert-kofler', 'Ruppert Kofler (Kofler-Bauer)', 'Vorname fällt im Steuersünder (0:04) und in Dorfmedizin (2:56)'),
        ('die-koflerische', 'Die Koflerische', 'Seine Frau, so vom Pater angesprochen'),
        ('kofler-bub', 'Der Bub', 'Sohn der Koflers, namenlos'),
        ('pater-vinzenz', 'Pater Vinzenz', 'Namentlich genannt im Steuersünder (0:26)'),
        ('steuerhund', 'Steuerhund der Kirche', 'Einer der beiden Begleiter des Paters'),
        ('arno', 'Arno', '„Der Diplomierte“'),
        ('irmgard', 'Irmgard', '„Die alte Kräuterhexe“, mit Pendel und Globuli'),
        ('tourist', 'Der Tourist', 'Spricht nur Englisch, Bein ausgekegelt'),
        ('notarzt', 'Der Notarzt', 'Vom Bub gerufen'),
        ('sepp-kruatlhuba', 'Sepp (Joseph) Kruatlhuba', 'Magister, Referatsleiter Gartenzaunsanierung'),
        ('gumpitsch', 'Gumpitsch', 'Hutladenbesitzer; im Dorfgerücht der „Tratschkopf“'),
        ('ploner', 'Ploner („der alte Plona“)', 'Hutkunde; früher Speckhandel Plona'),
        ('hannelores-mann', 'Hannelores Mann', 'Zweiter in der Gerüchtekette, namenlos'),
        ('hannelore', 'Hannelore', 'Arbeitet im Salon'),
        ('kundin-mit-lockenwicklern', 'Kundin im Salon', 'Erzählt es dem Ruppert weiter'),
        ('peppi-raffl', 'Peppi Raffl', 'Edith nennt ihn auch „Beppo“'),
        ('gamper', 'Gamper', 'Essenslieferant; Peppi hält ihn für den Bub vom Plona und nennt ihn „Muchl“'),
        ('eisverkaeufer', 'Der Eisverkäufer', 'Veganer Eissalon im früheren Speckhandel Plona'),
        ('vater-ins-hittl-gschaut', 'Der Vater', 'Ins Hittl g\'schaut Folge 3; vergisst den Namen seines Sohns'),
        ('bua-ins-hittl-gschaut', 'Der Bua', 'Will in Wien Wirtschaft studieren'),
        ('wirtshaus-philosophen', 'Die zwei Wirtshaus-Philosophen', 'Reden über Stadträtin Steinmeyer'),
        ('krippele', 'Krippele', 'Spottname des Mannes mit Krücken'),
        ('alm-date-sie', 'Die Frau vom Alm-Date', 'Namenlos'),
        ('alm-date-brunner', 'Brunner', 'Name und Alter (26) stehen im Dating-Profil'),
        ('almgespraech-bauer-mit-hut', 'Bauer mit Hut', 'Almgespräch'),
        ('almgespraech-bauer-ohne-hut', 'Bauer ohne Hut', 'Almgespräch'),
        ('gespraechsthema-stammtisch', 'Die zwei vom Stammtisch', 'Gesprächsthema Nummer 1 in Tirol'),
        ('telefoniererin', 'Die Telefoniererin', 'Telefonieren auf Österreichisch'),
        ('josef', 'Josef', 'Krippenspiel in der Tiroler Dorfgemeinde Bethlehem'),
        ('paketbote-koenig', 'Der dritte König', 'Bringt die Myrrhe als Paket und braucht eine Unterschrift'),
        ('engel', 'Der Engel', 'Krippenspiel'),
    ]),
    ('Wien', [
        ('edith', 'Edith', 'Die Backfee'),
        ('burli', 'Burli', 'Sagt „Mama“ zu Edith'),
        ('dr-eberhard-zupffinger', 'Dr. Eberhard Zupffinger', 'Beauty-Doc'),
        ('frau-simacek', 'Frau Simacek', 'Vor dem Eingriff'),
        ('hutmaennchen-mahue', 'Das Hutmännchen (Mahü)', 'Mit Zylinder'),
        ('hutmaennchen-interview', 'Das Hutmännchen (Interview)', 'Mit Spitzhut; die Sonne nennt ihn „Piefke“ und „Burli“'),
        ('monologiker', 'Der Monologiker', 'Gleicher Spitzhut wie der Interviewer'),
        ('donauinsel-grantler', 'Der Grantler von der Donauinsel', 'Will den Monologiker „abdrehen“'),
        ('wiener-sonne', 'Die Wiener Sonne', 'Besteht auf „Herr Sonne“'),
        ('wolke-nachbarin', 'Die Wolke', '„Frau Nachbarin“, verlangt eine Drehgenehmigung'),
        ('wiener-bub', 'Der Wiener Bub', '9 Jahre alt'),
        ('wiener-bub-vater', 'Vater des Wiener Bubs', 'Das Versprechen Teil 2'),
        ('wiener-bub-mutter', 'Mutter des Wiener Bubs', 'Das Versprechen Teil 2'),
        ('deutscher-hipster', 'Der deutsche Hipster', 'Wohnt in Berlin'),
        ('der-neue-praesident', 'Der neue Präsident', ''),
        ('herr-lobbinger', 'Herr Lobbinger', 'Roboz 4 se Wörld GmbH'),
        ('praesidenten-begleiter', 'Begleiter des Präsidenten', 'Flüstert ihm zu, was er nicht zeigen darf'),
        ('floetenbernhard', 'Flötenbernhard', 'Geheimes Genexperiment der Regierung, nur als Schautafel'),
        ('zunderer', 'Zunderer', 'Flammenwerfer-Roboter von Roboz 4 se Poor'),
        ('bewerbungsbetrueger', 'Der Bewerbungsbetrüger', ''),
        ('gernot-hofbauer', 'Gernot Hofbauer', 'Bewerber'),
        ('echter-mitarbeiter', 'Echter Mitarbeiter der Firma', 'Will ein Wurfnetz aufstellen'),
        ('internetz-tv-moderator', 'Moderator von Internetz-TV', ''),
        ('da-kusoen', 'Da Kusön', 'Der Cousin des Moderators'),
        ('frau-brennsackl', 'Frau Brennsackl', 'Profilbild von franzbrennsackl77'),
        ('mandale', 'Das Mandale', 'Sitzt am Baum, Handy in der Wohnung vergessen'),
        ('polizist', 'Polizist', 'Mit dem Mandale im Hintergrund'),
        ('vogel-fotograf', 'Der Vogelfotograf', 'Der Vogel, 11. Bezirk'),
        ('vogel-nachbar', 'Der Nachbar', 'Der Vogel'),
        ('klomandl', 'Klomandl', 'Links der Wartende, rechts der am Tisch vor dem WC'),
    ]),
    ('Parodien und Sonstiges', [
        ('gandalf', 'Gandalf', ''),
        ('frodo', 'Frodo', ''),
        ('aragorn', 'Aragorn', 'Sucht sein Schwert'),
        ('gimli-gimmlitzer', 'Gimli („der Gimmlitzer“)', 'Schulfreund des Wiener Nachbarn'),
        ('wiener-nachbar-moria', 'Der Nachbar von der 1er-Stiege', 'War im Poly Seidlergasse in der Parallelklasse'),
        ('morpheus', 'Morpheus', ''),
        ('gernot-hofstaetter', 'Gernot Hofstätter', 'Neo-Kandidat; sein Arzt heißt Dr. Feldgruber'),
        ('nomad-carl', 'Nomad Carl', 'Kurzfilm ohne Dialog'),
        ('bogenschuetzen-anfuehrer', 'Anführer der Bogenschützen', '„Der schlaue General“'),
        ('ritter-anfuehrer', 'Anführer der Ritter', 'Ritter gegen Bogenschützen'),
    ]),
]
out = ['# Figuren', '', 'Ein Standbild pro Figur, aus den Videos des Kanals [Mr. Manuel Cavaleras](https://www.youtube.com/@manuelcavaleras) geschnitten. Stand 2026-11-20. Alle Figuren und Bilder gehören ihrem Schöpfer.', '']
used = set()
for world, entries in worlds:
    out += [f'## {world}', '', '| Bild | Figur | Video | Stelle | Anmerkung |', '|---|---|---|---|---|']
    for slug, name, note in entries:
        vid, sec, title = rows[slug]
        used.add(slug)
        out.append(f'| [{slug}.jpg]({slug}.jpg) | {name} | [{title}](https://www.youtube.com/watch?v={vid}&t={sec}s) | {sec // 60}:{sec % 60:02d} | {note} |')
    out.append('')
missing = set(rows) - used
assert not missing, missing
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out))
print(len(used), 'figures listed')
