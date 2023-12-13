# https://fixmypc.ru/post/vstavka-teksta-i-izobrazheniia-v-kartinku-s-python-pillow-pil/
# https://fixmypc.ru/post/vstavka-teksta-i-izobrazheniia-v-kartinku-s-python-pillow-pil/

from PIL import Image, ImageDraw, ImageFont


image = Image.open('test2.jpg')

# Создаем объект ImageDraw для рисования
draw = ImageDraw.Draw(image)

# Определяем координаты прямоугольника
x1, y1 = [375, 37]
x2, y2 = [512, 71]

color = 'green'

# Рисуем прямоугольник
draw.rectangle([x1, y1, x2, y2], outline=color, width=2)


font = ImageFont.truetype('Roboto.ttf', size=14)
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (375, 23),
    'Ввеген в депствие I985',
    # Добавляем шрифт к изображению
    font=font,
    fill=color)


# Определяем координаты прямоугольника
x1, y1 = [248, 320]
x2, y2 = [378, 337]

# Рисуем прямоугольник
draw.rectangle([x1, y1, x2, y2], outline=color, width=2)


font = ImageFont.truetype('Roboto.ttf', size=14)
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (248, 295),
    'Кратков содертяние',
    # Добавляем шрифт к изображению
    font=font,
    fill=color)


# Определяем координаты прямоугольника
x1, y1 = [226, 359]
x2, y2 = [419, 411]

# Рисуем прямоугольник
draw.rectangle([x1, y1, x2, y2], outline=color, width=2)


font = ImageFont.truetype('Roboto.ttf', size=14)
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (226, 415),
    'Уточненке текста СРлзя\n зачела: аппараттун CO;-\n CO-70 на CO-72M (сд:оенгы])',
    # Добавляем шрифт к изображению
    font=font,
    fill=color)


# Определяем координаты прямоугольника
x1, y1 = [437, 361]
x2, y2 = [552, 429]

# Рисуем прямоугольник
draw.rectangle([x1, y1, x2, y2], outline=color, width=2)


font = ImageFont.truetype('Roboto.ttf', size=14)
draw_text = ImageDraw.Draw(image)
draw_text.text(
    (437, 435),
    'I54E FI, 5-2\n после вНпопнентя\n дэра; nт =. Rpoне\n экслортннх',
    # Добавляем шрифт к изображению
    font=font,
    fill=color)

# Сохраняем изображение
image.save("result_for_test2.jpg")