import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier("cascadas/haarcascade_frontalface_default.xml")
profile_cascade = cv2.CascadeClassifier("cascadas/haarcascade_profileface.xml")
eye_cascade = cv2.CascadeClassifier("cascadas/haarcascade_eye.xml")

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    profiles = profile_cascade.detectMultiScale(gray, 1.3, 5)

    # Dibujar rostros frontales
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Dibujar rostros de perfil
    for (x, y, w, h) in profiles:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)

    # Dibujar ojos
    eyes = eye_cascade.detectMultiScale(gray)
    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(frame, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)

    cv2.imshow("Camara", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
