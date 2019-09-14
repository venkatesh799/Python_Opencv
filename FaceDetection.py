import cv2,time
video=cv2.VideoCapture(0)
a=1
while True:
    face_cascade = cv2.CascadeClassifier("hascascade_fontal_face.xml")
    check,frame=video.read()
    faces=face_cascade.detectMultiScale(frame,scaleFactor=1.05,minNeighbors=5)
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    for x,y,w,h in faces:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    cv2.imshow("Gray",frame)
    key=cv2.waitKey(1)
    if key == ord('q'):
        break
    a+=1
video.release()
cv2.destroyAllWindows()
