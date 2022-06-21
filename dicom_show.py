import os
import pydicom
# 调用本地的 dicom file 
folder_path = '/home/a123/kidney_dataset/first/1yinshipingA'
file_name = "yinshipingA_9.Dcm"
file_path = os.path.join(folder_path, file_name)
ds = pydicom.dcmread(file_path)
print(ds)