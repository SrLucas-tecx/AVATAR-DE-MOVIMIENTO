import sys
import cv2
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer
from detector import Detector
from image_manager import ImageManager
from camera import Camera

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Presentación Avatar")
        self.setGeometry(100, 100, 1000, 600)

        # Botones
        self.start_btn = QPushButton("▶ Iniciar")
        self.stop_btn = QPushButton("⏸ Detener")
        self.quit_btn = QPushButton("❌ Salir")

        # Labels para mostrar cámara e imagen
        self.camera_label = QLabel("Vista de Cámara")
        self.image_label = QLabel("Imagen Estado")

        # Layout principal
        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.start_btn)
        btn_layout.addWidget(self.stop_btn)
        btn_layout.addWidget(self.quit_btn)

        main_layout = QVBoxLayout()
        main_layout.addLayout(btn_layout)
        main_layout.addWidget(self.camera_label)
        main_layout.addWidget(self.image_label)

        self.setLayout(main_layout)

        # Conexiones
        self.start_btn.clicked.connect(self.start)
        self.stop_btn.clicked.connect(self.stop)
        self.quit_btn.clicked.connect(self.quit)

        # Variables
        self.running = False
        self.detector = Detector()
        self.image_manager = ImageManager("config.json")
        self.camera = Camera()
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def start(self):
        if not self.running:
            self.running = True
            self.timer.start(30)  # refresco cada 30 ms

    def stop(self):
        self.running = False
        self.timer.stop()
        cv2.destroyAllWindows()

    def quit(self):
        self.stop()
        self.camera.release()
        QApplication.quit()

    def update_frame(self):
        frame = self.camera.get_frame()
        if frame is None:
            return

        estado = self.detector.detectar(frame)

        # Mostrar cámara
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb.shape
        qimg = QImage(rgb.data, w, h, ch * w, QImage.Format_RGB888)
        self.camera_label.setPixmap(QPixmap.fromImage(qimg))

        # Mostrar imagen asociada al estado
        data = self.image_manager.images.get(estado, self.image_manager.images.get("ninguno"))
        if data:
            ruta = data.get("ruta")
            img = cv2.imread(ruta)
            if img is not None:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                h, w, ch = img.shape
                qimg = QImage(img.data, w, h, ch * w, QImage.Format_RGB888)
                self.image_label.setPixmap(QPixmap.fromImage(qimg))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Interface()
    window.show()
    sys.exit(app.exec_())
