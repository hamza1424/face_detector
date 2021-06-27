


# Importing Lib
import cv2

# Loading Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Reading video from WebCam
cap = cv2.VideoCapture(0)

cap.set(3,600)
cap.set(4,480)



#Showing Video 
while True:
    
    success, img = cap.read()
    
    # Converting to GrayScale

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #Detecting Faces 
    
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    #Draw Rectangle around face
#Func for Text


    for ( x, y, w, h) in faces:
        cv2.rectangle(img, (x,y),( x + w, y + h),(255,0,0),2)
        cv2.putText(img,'Face',(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,0,255),2)
        cv2.imshow("Face",img)
    


    
    if cv2.waitKey(30) == 27:
        break
        
cv2.destroyAllWindows()
cap.release()









