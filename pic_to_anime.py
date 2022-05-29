import cv2
import numpy as np
import os

img = cv2.imread(os.path.dirname(os.path.abspath(__file__))+"/Mandrill.bmp")

### kmeans
Z = img.reshape((-1, 3))

Z = np.float32(Z)

criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 15
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)

center = np.uint8(center)
res = center[label.flatten()]
kmeans = res.reshape((img.shape))


### canny
canny = cv2.Canny(img, 150, 300, L2gradient=True)

### add
canny = cv2.resize(canny, kmeans.shape[1::-1])
canny2 = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)
canny3 = cv2.bitwise_not(canny2)

dst = cv2.bitwise_and(canny3, kmeans)

print(canny.shape)
print(kmeans.shape)

cv2.imshow('canny',canny)
cv2.imshow('kmeans',kmeans)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()