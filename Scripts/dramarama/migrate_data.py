# **[WARNINGS] Don't run this file.
"""DRAMADATA_DIR = 'dramarama/static/data/dramadata.csv'
with open(DRAMADATA_DIR, newline='', encoding='utf-8') as drama_csv:
reader = csv.DictReader(drama_csv)
for row in reader:
Drama.objects.create(
    value=row['value'],
    title=row['title'],
    channel=row['channel'],
    info_url=row['information']
)

FORM_DIR = 'dramarama/static/data/formdata.csv'
with open(FORM_DIR, newline='', encoding='utf-8') as form_csv:
reader = csv.DictReader(form_csv)
for row in reader:
date_list = row['date'].split('. ')

if row['physicaltrouble'] == "예":
    physicaltrouble_val = True
elif row['physicaltrouble'] == "아니오":
    physicaltrouble_val = False
else: physicaltrouble_val = None

if row['mentaltrouble'] == "예":
    mentaltrouble_val = True
elif row['mentaltrouble'] == "아니오":
    mentaltrouble_val = False
else: mentaltrouble_val = None

Survey.objects.create(
    date=date(int(date_list[0]), int(date_list[1]), int(date_list[2])),
    age=row['age'],
    gender=row['gender'],
    personality=row['personality'],
    activity=True if row['activity'] == "예" else False,
    job=row['job'],
    interested=row['interested'],
    school=True if row['school'] == "예" else False,
    work=True if row['work'] == "예" else False,
    abode=row['abode'],
    siblings=row['siblings'],
    family=row['family'],
    livealone=True if row['livealone'] == "예" else False,
    major=row['major'],
    homeeconomy=row['homeeconomy'],
    havedate=True if row['havedate'] == "예" else False,
    physicaltrouble=physicaltrouble_val,
    mentaltrouble=mentaltrouble_val,
    prefergenre=row['prefergenre'],
    preferchannel=row['preferchannel'],
    watchingtime=row['watchingtime'],
    used=row['used'],
    way=row['way'],
    first=row['first'],
    second=row['second'],
    third=row['third']
)"""