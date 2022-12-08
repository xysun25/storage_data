# 使用模块json存储数据
# json.dump()和json.load()
# json.dump()接受两个实参：要存储的数据，存储数据的文件对象

import json

number=[2,3,4,5,7,13,35,67]

filename= 'number.json'
with open(filename,'w') as f_obj:
    json.dump(number,f_obj)