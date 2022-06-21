import os
import re
import nibabel as nb
import numpy as np
import pandas


from xpinyin import Pinyin


kidney_dataset_path = '/home/a123/kidney_dataset'
file = open('test1.txt', mode='w')
sheet = pandas.read_excel(os.path.join(kidney_dataset_path, 'kidney_data.xls'), keep_default_na=False)
kidney_sub_paths = ['first', 'second']
lists = ['弱阳性', '阳性', '强阳性']
p = Pinyin()
name_lists = open('class.txt', mode='r')
name_lists = name_lists.readlines()
name_dict = {}
for name_list in name_lists:
    print(name_list)
    j = name_list.split()
    name_dict[j[1]] = j[0]
for kidney_sub_path in kidney_sub_paths:
    kidney_dataset_lists = os.listdir(os.path.join(kidney_dataset_path, kidney_sub_path))
    for i in kidney_dataset_lists:
        kidney_full_path = os.path.join(kidney_dataset_path, kidney_sub_path, i)
        kidney_sub_lists = os.listdir(kidney_full_path)
        new_string = re.sub(r'\d+', '', i)
        if "{}.nii".format(new_string) in kidney_sub_lists:
            label_name = "{}.nii".format(new_string)
            label_full_path = os.path.join(kidney_dataset_path, kidney_sub_path, i, label_name)
            label = nb.load(label_full_path)
            # print(label.header.get_data_dtype())
            label_data = label.get_fdata()
            for j in range(label_data.shape[2]):
                img_arr = label_data[:, :, j]
                # print(new_string[0:-1])
                if np.any(img_arr):
                    file.write(os.path.join(kidney_full_path, new_string))
                    file.write('_{}.Dcm'.format(j))
                    file.write('\n')
                    if name_dict[new_string[0:-1]]:
                        origin_dir = os.path.join(kidney_full_path, new_string) + "_{}.Dcm".format(j)
                        new_dir = os.path.join(kidney_dataset_path, name_dict[new_string[0:-1]], new_string[0:-1]) + '/'
                        if os.path.exists(new_dir):
                            os.popen('cp -rf {0} {1}'.format(origin_dir, new_dir))
                        else:
                            os.makedirs(new_dir)
                            os.popen('cp -rf {0} {1}'.format(origin_dir, new_dir))
        else:
            print('{}.nii not exist'.format(new_string))
