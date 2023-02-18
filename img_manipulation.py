from PIL import Image, ImageDraw, ImageFont
from window import color_field_R, color_field_G, color_field_B, font_sz_field
from assist_funcs import *
from buffer import *


color_font = ()
font_size = 70

def save_img(file_name, text):
    read_actions()
    print(f'-{source_path},\n-{target_path}')
    try:
        font = ImageFont.truetype('arial.ttf', font_size)
        image = Image.open(source_path + '\\' + file_name)
        text_pos = (image.size[0] - font_size * 3, 0 + font_size*2)
        drawer = ImageDraw.Draw(image)
        drawer.text(text_pos, text, font=font, fill=color_font)
        image.save(target_path + '\\' + file_name)
        error_codes()
    except:
        print('error in save_img')
        error_codes(7)


def font_change():
    global color_font, font_size
    if (color_field_R.get() or color_field_G.get() or color_field_B.get()) != '':
        try:
            color_tuple = (int(color_field_R.get()), int(color_field_G.get()), int(color_field_B.get()))
            for clr in color_tuple:
                if 0 < clr < 256:
                    color_font = color_tuple
                    error_codes()
                else:
                    error_codes(2)
        except:
            print('error in font_change colors')
            error_codes(2)
    else:
        color_font = (77, 201, 122)

    if font_sz_field.get() != '':
        try:
            fnt_sz = int(font_sz_field.get())
            if 0 < fnt_sz < 256:
                font_size = fnt_sz
                error_codes()
            else:
                error_codes(3)
        except:
            print('error in font_change font size')
            error_codes(3)

def numbering(index):
    qntt_zrs = str('0' * (4 - len(str(index)))) #quantity zeros
    return f'({qntt_zrs}{index})'

#def create_img(index,file_name):
#    csv_append(numbering(index),file_name)
#    save_img(file_name, numbering(index))
#    print(index, ' files ready')
#    count(index)
