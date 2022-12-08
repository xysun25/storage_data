# 使用json.load()将这个列表读取到内存中

import json

filename='number.json'
with open(filename) as f_obj:
    numbers=json.load(f_obj)

print(numbers)