import cv2 as cv
import numpy as np

kernel = np.ones((5,5),np.uint8)

img = cv.imread("PTRB.png")

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

imgBlur = cv.GaussianBlur(imgGray,(7,7),0)

imgCanny = cv.Canny(img,100,100)

imgDialation = cv.dilate(imgCanny,kernel,iterations=1)

imgEroded = cv.erode(imgDialation,kernel,iterations=1)

cv.imshow("Gray Image", imgGray)
cv.imshow("Blur Image", imgBlur)
cv.imshow("Canny Image", imgCanny)
cv.imshow("Dilate Image", imgDialation)
cv.imshow("Erode Image", imgEroded)
cv.waitKey(0)