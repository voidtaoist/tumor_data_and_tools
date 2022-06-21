import os

img_path = '/home/a123/tumor_data_and_tools/gbm_png'
img_lists = os.listdir(img_path)
i = 0
for img_list in img_lists:  # todo range change list &&str
    img_full_path = os.listdir(img_path+'/'+img_list)
    for img in img_full_path:
        i += 1
        print(i)
        src = os.path.join(os.path.abspath(img_path), img_list, img)  # 原先的图片名字
        dst = os.path.join(img_list, '{}.{:0>5d}.bmp'.format(img_list,i))  # 根据自己的需要重新命名
        os.rename(src, dst)  # 重命名,覆盖原先的名字
