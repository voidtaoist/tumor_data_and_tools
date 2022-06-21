from sklearn.model_selection import train_test_split
from glob import glob


import os


data_dir = '/home/a123/new_data_path/'
iteams_list = sorted(glob(data_dir+'*'))
images_list = []
for id, iteam in enumerate(iteams_list):
    iteam_images = sorted(glob(iteam+'/*'))
    for iteam_images_id, image_name in enumerate(iteam_images):
        images_list.append(image_name)
print(len(images_list))
namelist_train, namelist_test = train_test_split(images_list, test_size=0.3, random_state=2)
print('namelist_train', namelist_train)
print('namelist_test', namelist_test)
train_dir = '/home/a123/tumor_data_and_tools/kidney_dataset/train_set/'
test_dir = '/home/a123/tumor_data_and_tools/kidney_dataset/test_set/'
for id, image_name in enumerate(namelist_train):
    save_name = image_name.replace(data_dir, train_dir)
    iteam_name = save_name.split('/')[-2]
    iteam_dir = train_dir+iteam_name+'/'
    if not os.path.exists(iteam_dir):
        print(iteam_dir)
        os.makedirs(iteam_dir)
    os.popen('cp -rf {} {}'.format(image_name, save_name))
for id, image_name in enumerate(namelist_test):
    save_name = image_name.replace(data_dir, test_dir)
    iteam_name = save_name.split('/')[-2]
    iteam_dir = test_dir+iteam_name+'/'
    if not os.path.exists(iteam_dir):
        print(iteam_dir)
        os.makedirs(iteam_dir)
    os.popen('cp -rf {} {}'.format(image_name, save_name))
