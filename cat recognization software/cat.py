
import cv2

face_cascade=cv2.CascadeClassifier("cat.xml")

image=cv2.imread("cat3.jpg")

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)        # convert color image into gray image 

catfaces=face_cascade.detectMultiScale(gray,scaleFactor=1.01,minNeighbors=5)

#print(type(catfaces))     # to check type of catfaces
#print(catfaces)           # to check values of variable x & y and also width and hight placements

for x,y,w,h in catfaces:
    image=cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

cv2.imshow("CAT",image)
cv2.waitKey()