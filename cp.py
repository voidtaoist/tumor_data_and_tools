import os


kidney_dataset_path = '/home/a123/new_dataset'
file = open('test.txt', mode='r', newline='\n')
lists = file.readlines()
for i in lists:
    pic_name = i[0:-1]
    os.popen("cp -rf {0}   {1}".format(pic_name, kidney_dataset_path))
