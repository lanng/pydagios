import cv2
import re
from PIL import Image
from google.cloud import vision
import numpy as np


client = vision.ImageAnnotatorClient()
class Calculator:
    @staticmethod
    def extract_value(image_path):
        # TOP_LEFT = [110, 345]  # 112, 350 -- 158, 362
        # BOTTOM_RIGHT = [280, 407]  # 287, 412 - 259, 401

        image = Image.open(image_path)
        # Corta a área desejada da imagem
        # cropped_image = image.crop(
        #     (TOP_LEFT[0], TOP_LEFT[1], BOTTOM_RIGHT[0], BOTTOM_RIGHT[1]))

        image_array = np.array(image)
        image_array_bgr = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)
        vision_image = vision.Image(
            content=cv2.imencode('.png', image_array_bgr)[1].tobytes())

        # Faça a solicitação de OCR
        response = client.text_detection(image=vision_image)

        # Obtenha o texto extraído
        text = response.text_annotations[0].description
        decimal_values = re.findall(r'\d*\,\d+', text).pop()
        print(decimal_values)
        return decimal_values

    @staticmethod
    def sum_values(values):
        print(values)
        values_sum = sum([float(value.replace(',', '.')) for value in values])
        values_sum = round(values_sum, 2)
        return values_sum
