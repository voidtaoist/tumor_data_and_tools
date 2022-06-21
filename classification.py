import pandas
import os
import re

from xpinyin import Pinyin


kidney_dataset_path = '/home/a123/kidney_dataset'
sheet = pandas.read_excel(os.path.join(kidney_dataset_path, 'kidney_data.xls'), keep_default_na=False)
lists = ['弱阳性', '阳性', '强阳性']
p = Pinyin()
file = open('class.txt', mode='w')
for class_name in lists:
    column = sheet.loc[:, class_name]
    for name in column:
        if name == '姓名' or name == '':
            pass
        else:
            print(name)
            name_pinyin = p.get_pinyin(name, '')
            file.write(class_name)
            file.write('         {}'.format(name_pinyin))
            file.write('\n')



