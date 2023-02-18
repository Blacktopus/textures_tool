import os
from window import *
from assist_funcs import *
from csv_manipulation import *
from img_manipulation import *
from buffer import *



def run_program():
    global source_path, target_path, field1, field1_1, field2, get_mode
    file_indx = 1
    try:
        source_files = sorted(os.listdir(source_path())) # get names from directory
        target_files = sorted(os.listdir(target_path()))
        if source_path() != target_path():
            if csv_name not in target_files:
                csv_create()
            if get_mode() == 0: # numbering all images
                if len(source_file()) == 0:
                    for name in source_files:
                        if '_Sgn_' and '.png' in name:
                            csv_append(numbering(file_indx),name)
                            save_img(name, numbering(file_indx))
                            print(file_indx, ' files ready')
                            count(file_indx)
                            file_indx += 1
                        else:
                            continue
                else:
                    tags = []
                    if ',' in source_file():
                        tags.extend(source_file().split(','))
                    else:
                        tags.append(source_file())
                    for name in source_files:
                        for tag in tags:
                            if tag and '.png' in name:
                                csv_append(numbering(file_indx),name)
                                save_img(name, numbering(file_indx))
                                print(file_indx, ' files ready')
                                count(file_indx)
                                file_indx += 1
                            else:
                                continue
                error_codes()
            elif get_mode() == 1: # replacing one image
                if source_file() in source_files:
                    file_indx = csv_search(source_file())
                    save_img(source_file(), numbering(file_indx))
                    count(1)
                    error_codes()
                else:
                    error_codes(6)
            elif get_mode() == 2: # add one image
                if source_file() in source_files:
                    file_indx = csv_len()
                    csv_append(numbering(file_indx),source_file())
                    save_img(source_file(), numbering(file_indx))
                    count(1)
                    error_codes()
                else:
                    error_codes(6)
        else:
            error_codes(1)
    except:
        error_codes(4)

# Коды ошибок
    #1: 'укажите отличающиеся пути',
    #2: 'в поле цвета могут быть только цифры от 0 до 255',
    #3: 'размер шрифта может быть указан только цифрами от 0 до 255',
    #4: 'путь не найден',
    #5: 'файл "Help" не найден',
    #6: 'файл с таким именем не найден',
    #7: 'файл не является изображением'


help_button = tk.Button(mn_win, text = 'Help', command = open_help).grid(row=0,column=0, stick='w',padx=[10,0])

go_button = tk.Button(mn_win, text = 'Поехали!', command = run_program)\
    .grid(row=7,column=1, stick='w', padx=20, pady=[20,0]) 

tk.Button(mn_win, text = 'Применить', command = font_change)\
    .grid(row=9,column=2, columnspan=3) # look window color_field_R - font_sz_field

mn_win.mainloop()