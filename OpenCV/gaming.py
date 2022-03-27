import cv2 as cv
import numpy as np

farm_img = cv.imread("farm.png", cv.IMREAD_UNCHANGED)
wheat_img = cv.imread("needle.png", cv.IMREAD_UNCHANGED)
wheat_w = wheat_img.shape[1]
wheat_h = wheat_img.shape[0]
cv.imshow("farm", farm_img)


result = cv.matchTemplate(wheat_img, farm_img, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)


threshold = .60
yloc, xloc = np.where(result >= threshold)
rectangles = []
for (x, y) in zip(xloc, yloc):
    rectangles.append([int(x), int(y), int(wheat_w), int(wheat_h)])
    rectangles.append([int(x), int(y), int(wheat_w), int(wheat_h)])

rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)

for (x, y, w, h) in rectangles:
    cv.rectangle(farm_img, (x, y), (x + w, y + h), (0, 255, 255), 2)



cv.imshow("result", farm_img)
if cv.waitKey(0) & 0xFF == ord('q'):
    cv.destroyAllWindows()