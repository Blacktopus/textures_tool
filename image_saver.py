from PIL import Image, ImageDraw, ImageFont
from file_path import source_path, target_path
from errors import error_codes

#  Это должно находиться в файле со стилями
color_font = ()
font_size = 70

def save_img(file_name, text):
    try:
        font = ImageFont.truetype('arial.ttf', font_size)
        image = Image.open(source_path + '\\' + file_name)
        text_pos = (image.size[0] - font_size * 3, 0 + font_size*2)
        drawer = ImageDraw.Draw(image)
        drawer.text(text_pos, text, font=font, fill=color_font)
        image.save(target_path + '\\' + file_name)
        error_codes()
    except:
        error_codes(7)