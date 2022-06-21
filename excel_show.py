import pandas
import os

kidney_dataset_path = '/home/a123/kidney_dataset'
sheet = pandas.read_excel(os.path.join(kidney_dataset_path, 'kidney_data.xls'), keep_default_na=False)
print(sheet)