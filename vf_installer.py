#!/usr/bin/env python3
import requests
import os
import zipfile
from pathlib import Path

# remote resource
url: str = 'https://rubjo.github.io/victor-mono/VictorMonoAll.zip'

# fonts directory
fonts_dir_path = f'{os.environ["HOME"]}/.fonts'
file_name = f'{fonts_dir_path}/VictorMonoAll.zip'

# check if .fonts dir exists
if not os.path.exists(fonts_dir_path):
    os.mkdir(fonts_dir_path)

# donwload resource
response = requests.get(url)
if response.status_code == 200:
    with open(file_name, mode='wb') as local_file:
        local_file.write(response.content)

# extract files
with zipfile.ZipFile(file_name, mode='r') as zip_ref:
    zip_ref.extractall(fonts_dir_path)


# delete filtered items
items = os.listdir(fonts_dir_path)
for item in items:
    if item != 'TTF':
        os.system(f'rm -rf {fonts_dir_path}/{item}')

# move ttfs files to .fonts and remove TTF directory
os.system(f'mv {fonts_dir_path}/TTF/*.ttf {fonts_dir_path}')
os.system(f'rm -rf {fonts_dir_path}/TTF')
