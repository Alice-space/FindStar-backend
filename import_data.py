import csv
import os
import re
from datetime import date

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'star.settings')
django.setup()

from apps.find_star.models import Birth, Image

filename = "ymd2NGC_withUrl_1901_2020.csv"

reader = csv.DictReader(open(filename, "r"))

print("开始导入...........")

for row in reader:
    time = row['date'].split('/')
    birth = date(int(time[0]), int(time[1]), int(time[2]))
    birth = Birth.objects.create(birth=birth, word=row['message'])
    cnt = 0
    if row['url1']:
        assert (re.match(r'^https?:/{2}\w.+$', row['url1']))
        Image.objects.create(url=row['url1'], birth_id=birth.id)
        cnt += 1
    if row['url2']:
        assert (re.match(r'^https?:/{2}\w.+$', row['url2']))
        Image.objects.create(url=row['url2'], birth_id=birth.id)
        cnt += 1
    if row['url3']:
        assert (re.match(r'^https?:/{2}\w.+$', row['url3']))
        Image.objects.create(url=row['url3'], birth_id=birth.id)
        cnt += 1
    if row['url4']:
        assert (re.match(r'^https?:/{2}\w.+$', row['url4']))
        Image.objects.create(url=row['url4'], birth_id=birth.id)
        cnt += 1
    if row['url5']:
        assert (re.match(r'^https?:/{2}\w.+$', row['url5']))
        Image.objects.create(url=row['url5'], birth_id=birth.id)
        cnt += 1
    assert (birth.image_set.count() == cnt)

print("导入完成！")
