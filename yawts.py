from PIL import Image
from pytesseract import pytesseract
import cv2

#tessaract нь бичвэр таних хэрэгсэл юм.
#энэхүү зам нь тухайн хэрэгслийн байршилыг зааж өгч байна.
path_to_tesseract = r"/usr/local/Cellar/tesseract/4.1.1/bin/tesseract"
#Зургийн байршилыг зааж өгч байна.
image_path0 = r"handwritten0.jpeg"
image_path1 = r"handwritten1.jpeg"
image_path2 = r"handwritten2.jpeg"
image_path3 = r"handwritten3.jpeg"
image_path4 = r"handwritten4.jpg"

#Зургийн PIL сангаас Image-ыг дуудаж зургийг онгойлгож байгаа.
img0 = Image.open(image_path0)
img1 = Image.open(image_path1)
img2 = Image.open(image_path2)
img3 = Image.open(image_path3)
img4 = Image.open(image_path4)

#Tesseract-ыг ашиглахад бэлэн болгож өгч байршилыг зааж өгч байгаа.
pytesseract.tesseract_cmd = path_to_tesseract

#Tesseract-ын image_to_string функц ашиглаж зургаас үгсийг салгаж авч байна.
text0 = pytesseract.image_to_string(img0)
text1 = pytesseract.image_to_string(img1)
text2 = pytesseract.image_to_string(img2)
text3 = pytesseract.image_to_string(img3)
text4 = pytesseract.image_to_string(img4)

#таслаж гаргасан үгсийг харуулж байна.
print("-------1-------")
print(text0)
print("-------2-------")
print(text1)
print("-------3-------")
print(text2)
print("-------4-------")
print(text3)
print("-------5-------")
print("Davgatseren")
