from nibabel.viewers import OrthoSlicer3D
from nibabel import nifti1
import nibabel as nib
from matplotlib import pylab as plt
import numpy as np
import matplotlib


def show_nii():
    # matplotlib.use('TkAgg')
    # 需要查看的nii文件名文件名.nii或nii.gz
    filename = r'smb://wu_server/nas/吴金洋/肾癌数据集/第二批/bingli%20done37~73/53wangdelinA/wangdelinA.nii'
    # filename = r'F:\lingjun2019\nodule\MedicalNet\data\MRBrainS18\images\75.nii.gz'
    img = nib.load(filename)
    # 打印文件信息
    print(img)
    print(img.dataobj.shape)
    # shape不一定只有三个参数，打印出来看一下
    width, height, queue = img.dataobj.shape
    print(width, height, queue)
    # # 显示3D图像
    # OrthoSlicer3D(img.dataobj).show()
    # # 计算看需要多少个位置来放切片图
    interval = 1
    x = int((queue / interval) ** 0.5) + 1
    num = 1
    # 按照10的步长，切片，显示2D图像
    plt.figure(figsize=(12, 12))
    for i in range(0, queue, interval):
        img_arr = img.dataobj[:, :, 43]
        plt.subplot(x, x, num)
        # plt.axis('off')  # 去掉坐标轴
        plt.title('num:' + str(i))
        plt.imshow(img_arr, cmap='gray')
        num += 1
    plt.show()


if __name__ == "__main__":
    show_nii()