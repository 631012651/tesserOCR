import tesserocr
import pytesseract
from PIL import Image
import os
import cv2
import PIL.ImageOps
import matplotlib.pyplot as plt
class languages:
    CHS = 'chi_sim'
    CHT = 'chi_tra'
    ENG = 'eng'
    NA = 'num'

def img_to_str(image_path, lang):
    return pytesseract.image_to_string(Image.open(image_path), lang)

def save(text):
    fs = open("../OCR/gg_ocr.txt", 'w+', encoding='utf-8')  # 遍历后的图片提取文字，保存到txt
    fs.write(text)
    fs.close()

def main(image_path):
    if image_path is None or len(image_path) == 0:
        print("图片不存在。")
    else:
        # 识别
        lang = languages.NA
        text = img_to_str(image_path, lang)
        print("内容:", text, type(text))
        # 保存
        save(text)

if __name__=='__main__':
    print('当前路径是：', os.getcwd())
    image_path = '../OCR/bchuan.test.exp0.jpg'
    main(image_path)
    print("识别完成。")





print(tesserocr.tesseract_version())  # print tesseract-ocr version
print(tesserocr.get_languages())  # prints tessdata path and list of available languages

#image = Image.open('num.jpg')
#image2=image.convert('L')
#image2=image1.convert('1')
#inverted_image = PIL.ImageOps.invert(image)
#im = PIL.ImageOps.invert(image)
#plt.show()
#image2.save('image2.jpg')

#lang = languages.CHS
#print(tesserocr.image_to_text(image))  # print ocr text from image
# or
#print(tesserocr.image_to_text(image))
#print(pytesseract.image_to_string(image),lang)