import cv2 as cv
import numpy as np

img = cv.imread("PTRB.png")
print(img.shape)

imgResize = cv.resize(img,(640,480))

cv.imshow("Image",img)
cv.imshow("Resize",imgResize)

imgCropped = img[200:300,300:400]
cv.imshow("Cropped",imgCropped)

cv.waitKey(0)