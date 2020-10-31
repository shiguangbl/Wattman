import json
import os

file_dir = os.getcwd()
file_path = open(file_dir+'/boxes.json')
box = json.load(file_path)
print(box['boxes'][1]['rectangle'])