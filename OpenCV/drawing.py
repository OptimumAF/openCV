import cv2 as cv
import numpy as np

#Camera
cap = cv.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

myColors = [14,255,163,19,255,255]
colorValues = [0,119,239]

myPoints = []#[x, y, colorID]

def findColor(img,myColors,colorValues):
    imgHSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    newPoints = []
    lower = np.array(myColors[0:3])
    upper = np.array(myColors[3:6])
    mask = cv.inRange(imgHSV,lower,upper)
    x,y = getContours(mask)
    cv.circle(imgResult,(x,y),10,colorValues[:],cv.FILLED)
    #cv.imshow("img",mask)
    if x!=0 and y!=0:
        newPoints.append([x,y])
    return newPoints


def getContours(img):
    contours,hierarchy = cv.findContours(img,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_NONE)
    x,y,w,h = 0,0,0,0
    for cnt in contours:
        area = cv.contourArea(cnt)
        if area>500:
            #cv.drawContours(imgResult , cnt, -1, (255, 0, 0), 3)
            peri = cv.arcLength(cnt,True)
            approx = cv.approxPolyDP(cnt, 0.02*peri,True)
            x, y, w, h = cv.boundingRect(approx)
    return x+w//2,y

def drawOnCanvas(myPoints,colorValues):
    for point in myPoints:
        cv.circle(imgResult, (point[0],point[1]), 10, (colorValues[:]), cv.FILLED)



#Camera Loop
while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, colorValues)
    if len(newPoints)!=0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints)!=0:
        drawOnCanvas(myPoints, colorValues)

    cv.imshow("Video",img)
    cv.imshow("Result", imgResult)

    if cv.waitKey(1) & 0xFF ==ord('q'):
        break


#cv.imshow("Face",imgResize)
#cv.waitKey(0)