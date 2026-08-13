import cv2
from detector import Detector
from image_manager import ImageManager
from camera import Camera

detector = Detector()
image_manager = ImageManager("config.json")
camera = Camera()

while True:
    frame = camera.get_frame()
    if frame is None:
        break

    estado = detector.detectar(frame)
    print("Detección:", estado)

    # Ventana 1: cámara
    cv2.imshow("Camara", frame)

    # Ventana 2: imagen asociada al estado
    image_manager.mostrar(estado)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()
