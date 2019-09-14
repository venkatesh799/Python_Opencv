import cv2
face_cascade = cv2.CascadeClassifier("---HASCADE_FONTFACE_XML FILE lOACTION")
img=cv2.imread("----IMAGE PATH-----")
gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.10,minNeighbors=5)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
cv2.imshow("Gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

