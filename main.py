from camera import Camera
from detector import Detector
from image_manager import ImageManager
import cv2

def main():
    cam = Camera()
    detector = Detector()
    img_manager = ImageManager()

    mostrar_camara = True

    while True:
        frame = cam.get_frame()
        if frame is None:
            break

        estado = detector.detectar(frame)
        img_manager.mostrar(estado)

        if mostrar_camara:
            cv2.imshow("Camara", frame)

        tecla = cv2.waitKey(1) & 0xFF
        if tecla == ord('q'):
            break
        elif tecla == ord('c'):
            mostrar_camara = not mostrar_camara
            if not mostrar_camara:
                cv2.destroyWindow("Camara")

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
