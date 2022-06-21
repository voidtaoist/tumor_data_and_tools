import matplotlib.pyplot as plt
import numpy as np
import cv2

img = 'output.png'
a=cv2.imread(img)
plt.imshow(a, cmap='gray')
plt.show()