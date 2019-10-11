"""
Extraemos data de una imagen usamos tesseract-
reconocimiento de caracteres
Dani Risaro
"""

from PIL import Image
import pytesseract
import matplotlib.pyplot as plt
image = Image.open('/home/daniu/Documentos/ocr/prueba_penguin.jpg')

upper_image = image.crop([0, 0, 1619, 120]) #(left, upper, right, lower)

text = pytesseract.image_to_string(image, lang='eng')
metadata = pytesseract.image_to_string(upper_image, config='--psm 11')
print(text)
print(metadata)

plt.imshow(image)
plt.show()
