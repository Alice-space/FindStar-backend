from generate_poster import generate_poster
import csv
import os
from datetime import date

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'star.settings')
django.setup()

from apps.find_star.models import Birth, Post

filename = "../520final.CSV"

reader = csv.DictReader(open(filename, "r"))

print("开始导入...........")

for row in reader:
    if '/' in row['date']:
        time = row['date'].split('/')
    else:
        time = row['date'].split('-')
    birth = date(int(time[0]), int(time[1]), int(time[2]))
    birth = Birth.objects.get(birth=birth)
    print(f'生成{birth.birth.isoformat()}...')
    name = row['name']
    # print(name)
    # assert os.path.exists(f'./all_image/{name}.jpg')

    filename = f'../media/{birth.birth.isoformat()}.jpg'
    generate_poster(row['message'],
                    [f'./all_image/{name}.jpg'],
                    filename)
    Post.objects.create(birth=birth, post=filename)
