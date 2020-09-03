"# tesserOCR" 

                                                                            车牌识别
                                                                            
                                                                                          --OCR实战
一、	环境准备
Pytesseract
Tesserocr
语言包安装sudo apt install tesseract-ocr-*
Tesseract
Pillow
Opencv
https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/opencv-python/

二、车牌识别
需要 import pytesseract, tesserocr ,image
白字蓝底的车牌需要转换成黑字白底的图片，需要转换两次；先转灰色，后黑白
image_gray = image_raw.convert('L')   # 将图片变成灰色

image_black_white = image_gray.point(lambda x: 0 if x > 200 else 255)  #转换成黑白图片

 

 
 
pytesseract.image_to_string
打印出车牌号

FAQ：
1、RuntimeError: Failed to init API, possibly an invalid tessdata path:
解决办法：
测试一下CMD
tesseract --list-langs
TESSDATA_PREFIX需要配置完整路径： C:\Program Files\Tesseract-OCR\tessdata
2、车牌识别错误，请用jTessBoxEditor进行训练，把训练好的语言库放到tessdata
