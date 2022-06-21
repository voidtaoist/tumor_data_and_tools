#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# @Time    : 2022/6/16 下午9:30
# @Author  : wu
# @Site    : 
# @File    : roc.py
# @Software: PyCharm
import os

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sklearn.metrics as metrics
import json

label_file = open('/home/a123/mmclassification/data/val.txt')
true_label = []
for lines in label_file:
    true_label.append(int(lines[-2]))
file_path = '/home/a123/results'
results = os.listdir(file_path)
for i in results:
    file = json.load(open(os.path.join(file_path, i), 'r'))
    class_scores = file.get('class_scores')
    for nums, j in enumerate(class_scores):
        class_scores[nums] = j[1]
    fpr, tpr, threshold = metrics.roc_curve(true_label, class_scores, drop_intermediate=False, pos_label=1)  ###计算真正率和假正率
    sns.set_style('white')
    roc_auc1 = metrics.roc_auc_score(true_label, class_scores)
    ###计算auc的值，auc就是曲线包围的面积，越大越好
    lw = 1.5
    plt.plot(fpr, tpr, lw=lw, label='{} = %0.5f'.format(i) % roc_auc1)###假正率为横坐标，真正率为纵坐标做曲线
    plt.xlim([0, 1])
    plt.ylim([0, 1])
    roc_auc = metrics.auc(fpr, tpr)
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')  # 可以使用中文，但需要导入一些库即字体
    plt.title('ROC Curve')
    plt.legend(loc="lower right")
    plt.savefig('./result.tiff')

