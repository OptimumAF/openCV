import cv2 as cv
print("Package imported")

cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)




#cap = cv.VideoCapture("warzone.mp4")
while True:
    success, img = cap.read()
    cv.imshow("Video",img)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break



#img = cv.imread("PTRB.png")
#cv.imshow("Output", img)
#cv.waitKey(0)