import numpy as np
import cv2

watch_cascade = cv2.CascadeClassifier('watchcascade10stage.xml')


cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    
    watches = watch_cascade.detectMultiScale(gray, 10, 10)
    
    
    for (x,y,w,h) in watches:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, 'Relogio', (x - w, y - h), font, 0.5, (11, 255, 255),  2, cv2.LINE_AA)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]


    cv2.imshow('img',img)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()