import cv2
from model import FacialExpressionModel
font = cv2.FONT_HERSHEY_SIMPLEX
import numpy as np

image=cv2.imread('C://Users//HP//Downloads//photo (4).jpg')
gray_fr=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(image)

facec = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
model = FacialExpressionModel("model.json", "model_weights.h5")

faces = facec.detectMultiScale(gray_fr, 1.3, 5)

for (x, y, w, h) in faces:
            fc = gray_fr[y:y+h, x:x+w]

            roi = cv2.resize(fc, (48, 48))
            pred = model.predict_emotion(roi[np.newaxis, :, :, np.newaxis])

            cv2.putText(image, pred, (x, y), font, 1, (255, 255, 0), 2)
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)


cv2.imwrite('new.jpg',image)