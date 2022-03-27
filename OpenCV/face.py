import cv2 as cv

cap = cv.VideoCapture(2)
cap.set(3,640)
cap.set(4,480)
cap.set(10,100)

faceCascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")
#img = cv.imread("face.jpg")
#imgResize = cv.resize(img,(640,360))
#print(img.shape)
#imgGray = cv.cvtColor(imgResize,cv.COLOR_BGR2GRAY)



#face = faceCascade.detectMultiScale(imgGray,1.1,4)




while True:
    success, img = cap.read()
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    face = faceCascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, w, h) in face:
        cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv.imshow("Video",img)
    if cv.waitKey(1) & 0xFF ==ord('q'):
        break


#cv.imshow("Face",imgResize)
#cv.waitKey(0)