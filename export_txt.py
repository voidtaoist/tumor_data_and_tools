import os
import random


test_img_dir = './kidney_dataset/test_set'
test_kinds = os.listdir(test_img_dir)
origin_file = open('val.txt', 'r+', encoding='utf-8')
out_file = open('classlists.txt', 'w', encoding='utf-8')
lines = []
for kind in test_kinds:
    test_list = os.listdir(os.path.join(test_img_dir, kind))
    for test_img in test_list:
        origin_file.write(kind)
        origin_file.write('/')
        origin_file.write(test_img)
        origin_file.write(' ')
        if kind == '强阳性':
            origin_file.write('2')
        if kind == '弱阳性':
            origin_file.write('0')
        if kind == '阳性':
            origin_file.write('1')
        origin_file.write('\n')
origin_file.seek(0, 0)
for i in origin_file.readlines():
    lines.append(i)
random.shuffle(lines)
for j in lines:
    out_file.write(j)