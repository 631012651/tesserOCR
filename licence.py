from PIL import Image
import matplotlib.pyplot as plt
import tesserocr
import cv2
import os
import pytesseract

image_raw = Image.open("chuan.jpg") # open colour image
image_gray = image_raw.convert('L')   # 将图片变成灰色
image_gray.show()  #第一次弹
image_black_white = image_gray.point(lambda x: 0 if x > 200 else 255)  #转换成黑白图片
image_black_white.show()  #第二次弹
image_black_white.save('bchuan.test.exp0.jpg')

'''
 # opencv处理,去除噪点
img_cv = cv2.imread('black.jpg')
# 灰值化
im = cv2.cvtColor(img_cv, cv2.COLOR_BGR2GRAY)
 # 二值化
img_bin = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 1)
cv2.imwrite('imbin.jpg',img_bin)
'''

'''
# 噪点处理
def interference_point(img):
    filename = 'code_result.png'
    h, w = img.shape[:2]
    # 遍历像素点进行处理
    for y in range(0, w):
        for x in range(0, h):
            # 去掉边框上的点
            if y == 0 or y == w - 1 or x == 0 or x == h - 1:
                img[x, y] = 255
                continue
            count = 0
            if img[x, y - 1] == 255:
                count += 1
            if img[x, y + 1] == 255:
                count += 1
            if img[x - 1, y] == 255:
                count += 1
            if img[x + 1, y] == 255:
                count += 1
            if count > 2:
                img[x, y] = 255
    cv2.imwrite(filename, img)
    return img, filename
'''
'''
plt.figure('licencePlate')  #图名
plt.imshow(image_gray,cmap='gray') #cmap即colormap，颜色映射
plt.axis('on')  #关闭网格线
plt.show()
'''
#image_gray.save('jin2.jpg')
#box=(70,65,590,190)
#region = image_black_white.crop(box)
#region.show()
#region.save('cutoff.jpg')
#print(tesserocr.image_to_text('cutoff.jpg'))
print(tesserocr.file_to_text('bchuan.test.exp0.jpg'))

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