import cv2 as cv
import numpy as np

img = np.zeros((512,512,3),np.uint8)
#img[128:384,128:384] = 0,0,255

#cv.line(img,(0,128),(128,256),(12,234,23),256)
#cv.line(img,(0,384),(128,256),(12,234,23),256)

#cv.rectangle(img,(0,0),(256,256),(123,234,45),cv.FILLED)

#cv.rectangle(img,(0,0),(512,256),(256,0,0),cv.FILLED)
#cv.rectangle(img,(0,257),(512,512),(0,0,256),cv.FILLED)
#cv.triangle(img,(0,0),(128,256),(0,512),(0,0,0),cv.FILLED)
cv.imshow("Image",img)

cv.waitKey(0)