import cv2 as cv
import numpy as np
from windowcapture import WindowCapture

steve = cv.imread("Steve.PNG")
steve_w = steve.shape[1]
steve_h = steve.shape[0]
wincap = WindowCapture('minecraft - Google Search - Google Chrome')
while True:

    img = wincap.get_screenshot()
    #imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    result = cv.matchTemplate(steve, img, cv.TM_CCOEFF_NORMED)
    # get location of best match
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    cv.circle(img, (max_loc[1]+steve_w,max_loc[0]+steve_h), 50, (255, 0, 0), 10)

    cv.imshow("Computer Vision", img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        cv.destroyAllWindows()
        break

print("Done.")
