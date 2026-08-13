import cv2
import os
import json

class ImageManager:
    def __init__(self, config_file="config.json"):
        try:
            with open(config_file, "r", encoding="utf-8") as f:
                config = json.load(f)
                self.images = config.get("imagenes", {})
        except Exception as e:
            print(f"[ERROR] No se pudo cargar el archivo de configuración: {e}")
            self.images = {}

    def mostrar(self, estado):
        data = self.images.get(estado, self.images.get("ninguno"))
        if not data:
            print(f"[ERROR] No hay configuración para estado '{estado}'")
            return

        ruta = data.get("ruta")
        resize = data.get("resize")

        if not ruta or not os.path.exists(ruta):
            print(f"[ERROR] No se encontró la imagen: {ruta}")
            return

        img = cv2.imread(ruta)
        if img is None:
            print(f"[ERROR] No se pudo cargar la imagen: {ruta}")
            return

        if resize and isinstance(resize, list) and len(resize) == 2:
            img = cv2.resize(img, tuple(resize))

        cv2.imshow("Imagenes", img)
