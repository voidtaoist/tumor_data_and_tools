import matplotlib
import pydicom
import matplotlib.pyplot as plt
import imageio
import numpy as np
import os


kidney_path = '/home/a123/kidney_dataset/'
class_list = os.listdir(kidney_path)
new_path = '/home/a123/new_data_path_png'
for class_name in class_list:
    person_name_path = os.path.join(kidney_path, class_name)
    person_name_lists = os.listdir(person_name_path)
    for person_name in person_name_lists:
        pic_path = os.path.join(person_name_path, person_name)
        for pic in os.listdir(pic_path):
            ds = pydicom.read_file(os.path.join(pic_path, pic))  # 读取.dcm文件
            img = ds.pixel_array  # 提取图像信息
            #print(img.shape)
            #plt.imshow(img, cmap='gray')
            #plt.show()
            #lens = img.shape[0]*img.shape[1]# 获取像素点的最大值和最小值
            #arr_temp = np.reshape(img, (lens,))
            #max_val = max(arr_temp)
            #min_val = min(arr_temp)# 图像归一化
            #img_arr = (img-min_val)/(max_val-min_val) * 255
            #img_arr = img_arr.astype(np.uint8)
            out_path = os.path.join(new_path, class_name, person_name)
            out_dir = os.path.join(out_path, '{}.png'.format(pic[0:-4]))
            if os.path.exists(out_path):
                imageio.imwrite(out_dir, img)
            else:
                os.makedirs(out_path)
                imageio.imwrite(out_dir, img)
