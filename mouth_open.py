import cv2
import numpy as np

mouth_cascade = cv2.CascadeClassifier(r'C:\Users\hp\.vscode\advanced_openCV.py\Nullclass_projects/haarcascade_mcs_mouth.xml')

if mouth_cascade.empty():
    raise IOError('Unable to load the mouth cascade classifier xml file')

cap = cv2.VideoCapture(0)
ds_factor = 0.5

# frameWidth = 4500
# frameHeight = 3600
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)
# cap.set(10, 130)

while True:
    flag = True
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx=ds_factor, fy=ds_factor, interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    mouth_rects = mouth_cascade.detectMultiScale(gray, 1.1, 11)
    for (x,y,w,h) in mouth_rects:
        if h > 36:
            cv2.putText(gray, "Mouth open", (20,20), cv2.FONT_HERSHEY_COMPLEX, 1.0, (0,255,0), thickness=2)
            cv2.imshow('Mouth Detector', gray)
            
#             out.write(gray) 
            flag = False
        else:
            cv2.circle(frame, (int(x+0.1*w),y), 3, (0,0,255), 3)
            cv2.circle(frame, (int(x+0.9*w),y), 3, (0,0,255), 3)
        break
    if flag:
        cv2.imshow('Mouth Detector', frame)
#         out.write(frame) 

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
# out.release()
cv2.destroyAllWindows()

