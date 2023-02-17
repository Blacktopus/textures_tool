from errors import error_codes


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
            error_codes(3)
            
            
#подчеркнутое желтым почему-то не видит, что используется в другом файле
# при этом в файл window_adn_forms импортируется - там жалоб нет