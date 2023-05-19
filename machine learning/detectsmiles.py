# to detect face smile
import cv2

#import matplotlib.pyplot as plt
from time import sleep


fd=cv2.CascadeClassifier(cv2.data.haarcascades 
                        + "haarcascade_frontalface_default.xml")

sd=cv2.CascadeClassifier(cv2.data.haarcascades 
                         + "haarcascade_smile.xml")


#cv2 m gray scale img lete h

vid=cv2.VideoCapture(0)
while True:
    flag,img=vid.read()
    if flag:
        img_gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        x1,y1,w,h=(200,400,300,400)
      
        faces=fd.detectMultiScale(img_gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(80,80) #no of pixels in the face
        )
    

        for x1,y1,w,h in faces:
            face=img_gray[y1:y1+h,x1:x1+w].copy()
            smile=sd.detectMultiScale(face,1.1,5,minSize=(50,50))
            
            if len(smile)==1:
                
                xs,ys,ws,hs=smile[0]
                
                cv2.rectangle(img,pt1=(x1+xs,y1+ys),pt2=(x1+xs+ws,y1+ys+hs),
                          color=(255,0,0),thickness=10)

            cv2.rectangle(img,pt1=(x1,y1),pt2=(x1+w,y1+h),
                        color=(0,0,255),thickness=10)
        
        
        cv2.imshow("preview",img)



   
        key= cv2.waitKey(1)
        if key == ord("x"):
             break
    else:
        break
    sleep(0.1)

cv2.destroyAllWindows() 
vid.release()