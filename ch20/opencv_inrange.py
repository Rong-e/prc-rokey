import cv2
import numpy as np


image = cv2.imread(r'ch20\sky.jpg')
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

green_lower = np.array([85,100,100])
green_upper = np.array([125,255,255])
mask = cv2.inRange(hsv,green_lower,green_upper)
result = cv2.bitwise_and(image,image,mask = mask)


cv2.imshow('imaged',result)
cv2.waitKey(0)
cv2.destroyAllWindows()

