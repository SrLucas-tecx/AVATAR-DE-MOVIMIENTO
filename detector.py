import cv2

class Detector:
    def __init__(self):
        self.face_cascade = cv2.CascadeClassifier("cascadas/haarcascade_frontalface_default.xml")
        self.profile_cascade = cv2.CascadeClassifier("cascadas/haarcascade_profileface.xml")

    def detectar(self, frame):
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        rostros = self.face_cascade.detectMultiScale(gris, 1.3, 5)
        perfiles = self.profile_cascade.detectMultiScale(gris, 1.3, 5)

        if len(rostros) > 0:
            return "frente"
        elif len(perfiles) > 0:
            return "lado"
        else:
            return "ninguno"
