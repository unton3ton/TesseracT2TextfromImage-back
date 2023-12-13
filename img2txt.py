# conda activate TesseracT

import os.path
from PIL import Image

import easyocr
import pytesseract

# Если вы используете ОС Windows # путь к исполняемому файлу tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

OEM = 3 
PSM = 1 # 6

# распозавание с помощью pytesseract, открытие картинки PIL.Image
def teseract_recognition(path_img):
    return pytesseract.image_to_string(Image.open(path_img), lang='rus+eng', config=fr'--oem {OEM} --psm {PSM}')

contrast_ths = 0.1
adjust_contrast = 0.5
text_threshold = 0.8
low_text = 0.4
mag_ratio = 2
slope_ths = 0.1

# распознавание с помощью easyocr, параметры: отключена детализация вывода,
# включены параграфы и установлена точность текста
def easyocr_recognition(path_img):
    return easyocr.Reader(['ru','en'], gpu=False).readtext(path_img,
        detail=1,
# detail= если значение равно 1 (по умолчанию), то вывод будет подробным с координатами ограничивающего прямоугольника.
# В противном случае, если значение равно 0, выходные данные состоят только из распознанных текстов.
        paragraph=True, # объединить результат в параграф
        contrast_ths=contrast_ths, 
# Текстовое поле с контрастом ниже этого значения будет передано в модель 2 раза.
# Первый - с исходным изображением, второй - с контрастом, отрегулированным по значению 'adjust_contrast'.
# В результате будет возвращено изображение с более уверенным уровнем.
        adjust_contrast=adjust_contrast, # целевой уровень контрастности для низкоконтрастного текстового поля
        text_threshold=text_threshold, # порог достоверности текста
        low_text=low_text, # оценка низкой границы текста
        mag_ratio=mag_ratio, # коэффициент увеличения изображения
        slope_ths=slope_ths)
# Максимальный наклон (delta y/delta x) для рассматриваемого слияния.
# Малое значение означает, что плиточные боксы не будут объединяться.


# сохранение текста в текстовый файл
def save_text(text, name):
    with open(f'{name}.txt', 'w', encoding='utf-8') as file:
        file.write(str(text))
    print(f'[+] Распознанный текст сохранен в файл: "{name}.txt"')


path_img = input('\n[+] Введите путь к картинке >>> ')

save_text(teseract_recognition(path_img), "text-from-teseract/" 
+ os.path.split(path_img)[1].split(".")[0])

save_text(easyocr_recognition(path_img), "text-from-easy/" 
+ os.path.split(path_img)[1].split(".")[0])


# name_change_param = PSM
# h = 1

# for i in range(1):
#     save_text(teseract_recognition(path_img), "text-from-teseract/" 
# + os.path.split(path_img)[1].split(".")[0] + "PSM=" 
# + str(name_change_param))
#     name_change_param += h

# name_change_param = mag_ratio
# h = 0.2

# for i in range(1):
#     save_text(easyocr_recognition(path_img), "text-from-easy/" 
# + os.path.split(path_img)[1].split(".")[0] 
# + "mag_ratio=" 
# + str(name_change_param))

#     name_change_param += h