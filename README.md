"# tesserOCR" 
����ʶ��
--OCRʵս
һ��	����׼��
Pytesseract
Tesserocr
���԰���װsudo apt install tesseract-ocr-*
Tesseract
Pillow
Opencv
https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/opencv-python/

��������ʶ��
��Ҫ import pytesseract, tesserocr ,image
�������׵ĳ�����Ҫת���ɺ��ְ׵׵�ͼƬ����Ҫת�����Σ���ת��ɫ����ڰ�
image_gray = image_raw.convert('L')   # ��ͼƬ��ɻ�ɫ

image_black_white = image_gray.point(lambda x: 0 if x > 200 else 255)  #ת���ɺڰ�ͼƬ

 

 
 
pytesseract.image_to_string
��ӡ�����ƺ�

FAQ��
1��RuntimeError: Failed to init API, possibly an invalid tessdata path:
����취��
����һ��CMD
tesseract --list-langs
TESSDATA_PREFIX��Ҫ��������·���� C:\Program Files\Tesseract-OCR\tessdata
2������ʶ���������jTessBoxEditor����ѵ������ѵ���õ����Կ�ŵ�tessdata
