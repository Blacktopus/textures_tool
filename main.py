import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont


#operation with path and files

source_path = ''
target_path = ''
csv_name = 'imgs_numbering.csv'


color_font = ()
font_size = 70

def save_img(file_name, text):
    font = ImageFont.truetype('arial.ttf', font_size)
    image = Image.open(source_path + '\\' + file_name)
    text_pos = (image.size[0] - font_size * 3, 0 + font_size*2)
    drawer = ImageDraw.Draw(image)
    drawer.text(text_pos, text, font=font, fill=(77, 201, 122))
    image.save(target_path + '\\' + file_name)

def font_change():
    global color_font, font_size
    if (color_field_R.get() or color_field_G.get() or color_field_B.get()) != '':
        try:
            color_tuple = (int(color_field_R.get()), int(color_field_G.get()), int(color_field_B.get()))
            for clr in color_tuple:
                if 0 < clr < 256:
                    color_font = color_tuple
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
            else:
                error_codes(3)
        except:
            error_codes(3)

def csv_crtr(index,file_name):
    csv_file = open(f'{target_path}\\{csv_name}', 'a')
    csv_file.write(f'{numbering(index)},{file_name}\n')
    csv_file.close()

def numbering(index):
    qntt_zrs = str('0' * (4 - len(str(index)))) #quantity zeros
    return f'({qntt_zrs}{index})'

def count(index):
    global complete_count
    complete_count.set(f'Файлов готово: {index}')

def create_file(index,file_name):
    csv_crtr(index,file_name)
    save_img(file_name, numbering(index))
    print(index, ' files ready')
    count(index)

def run_program():
    global source_path, target_path, field1, field1_1, field2, get_mode
    source_path = r'' + field1.get()
    target_path = r'' + field2.get()
    source_file = field1_1.get()
    if source_path != target_path:
        try:
            source_files = sorted(os.listdir(source_path)) # get names from directory
            target_files = sorted(os.listdir(target_path))
            if csv_name not in target_files:
                csv_file = open(f'{target_path}\\{csv_name}', 'w+') #create csv file
                csv_file.write('Index image,name of image\n') #headers for csv
                csv_file.close()
    
            file_indx = 1
            if get_mode.get() == 0:
                if source_file == '':
                    for name in source_files:
                        if '_Sgn_' and '.png' in name:
                            create_file(file_indx,name)
                            file_indx += 1
                        else:
                            continue
                elif source_file != '':
                    list_tags = source_file.split(',')
                    for name in source_files:
                        for tag in list_tags:
                            if tag and '.png' in name:
                                create_file(file_indx,name)
                                file_indx += 1
                            else:
                                continue
            if get_mode.get() == 1 or 2:
                if source_file in source_path:
                    if get_mode.get() == 1:
                        csv_file = open(f'{target_path}\\{csv_name}', 'r')
                        chr_fr_rplce = ['(', ')', '0']
                        for row in csv_file:
                            if source_file in row:
                                row_numb = row.split(',')[1]
                                for char in row_numb:
                                    if char in chr_fr_rplce:
                                        row_numb = row_numb.replace(char, '')
                                    else:
                                        continue
                                file_indx = int(row_numb)
                                save_img(source_file, numbering(file_indx))
                                csv_file.close()
                                break
                            else:
                                continue
                    elif get_mode.get() == 2:
                        csv_file = open(f'{target_path}\\{csv_name}', 'r')
                        last_row = csv_file[-1]
                        chr_fr_rplce = ['(', ')', '0']
                        row_numb = last_row.split(',')[1]
                        for char in row_numb:
                            if char in chr_fr_rplce:
                                row_numb = row_numb.replace(char, '')
                            else:
                                continue
                        file_indx = int(row_numb+1)
                        save_img(source_file, numbering(file_indx))
                        csv_file.close()
                        for row in csv_file:
                            if source_file in row:
                                
                                break
                            else:
                                continue
                        pass
                else:
                    error_codes(6)
        except:
            error_codes(4)
    else:
        error_codes(1)

def open_help():
    try:
        os.startfile('Help textures tool.txt')
    except:
        error_codes(5)

def error_codes(err_code = 0):
    global error_message
    errs_dict = { 1 : 'укажите отличающиеся пути',
                2: 'в поле цвета могут быть только цифры от 0 до 255',
                3: 'размер шрифта может быть указан только цифрами от 0 до 255',
                4: 'неправильно указан путь',
                5: 'файл "Help" не найден',
                6: 'файл с таким именем не найден'
        }
    if err_code in errs_dict:
        error_message.set(f'Ошибка: {errs_dict[err_code]}')
    else:
        error_message.set('Ошибка: неизвестная ошибка')


#create window and forms
mn_win = tk.Tk() #main window
mn_win.title('Texture numb RIGsoft')
mn_win.geometry('800x600')
mn_win.resizable(False, False)
win_logo = tk.PhotoImage(file = 'TeamRIGlogoBlack.png')
mn_win.iconphoto(True, win_logo)
#window wigets
tk.Label(mn_win, text = 'Програма для работы с файлами текстур', font='Arial 15').grid(row=0,column=1, pady=20, columnspan=5)
help_button = tk.Button(mn_win, text = 'Help', command = open_help).grid(row=0,column=0, stick='w',padx=[10,0])
tk.Label(text='1.').grid(row=2, column=0, stick='e')
tk.Label(text='1.1').grid(row=4, column=0, stick='ne')
tk.Label(text='2.').grid(row=6, column=0, stick='ne')

lbl_field1 = tk.Label(text='укажите расположение исходных файлов в формате: D:\\...\\source_dir')\
    .grid(row=1, column=1, stick='w', padx=20)
field1 = ttk.Entry(mn_win)
field1.grid(row=2,column=1, stick='we', padx=20)
lbl_field1_1 = tk.Label(text='укажите ключевые теги в формате: Sgn,DecalGraffiti,PACKED_0...\nили имя файла в формате: name.png', justify='left')\
    .grid(row=3, column=1, stick='ws', padx=20)
field1_1 = ttk.Entry(mn_win)
field1_1.grid(row=4,column=1, stick='wne', padx=20)

lbl_field2 = tk.Label(text='укажите папку для сохранения новых файлов в формате: D:\\...\\target_dir')\
    .grid(row=5, column=1, stick='ws', padx=20) #, pady=[10,0]
field2 = ttk.Entry(mn_win)
field2.grid(row=6,column=1, stick='wne', padx=20)

go_button = tk.Button(mn_win, text = 'Поехали!', command = run_program)\
    .grid(row=7,column=1, stick='w', padx=20, pady=[20,0])
complete_count = tk.StringVar()
complete_lbl = tk.Label(mn_win, textvariable = complete_count)\
    .grid(row=8,column=1, stick='w', padx=20, pady=[20,0])

error_message = tk.StringVar()
error_lbl = tk.Label(mn_win, textvariable = error_message, fg = 'red')\
    .grid(row=9,column=1, stick='w', padx=20, pady=[20,0])

tk.Label(text='3. Выберите что необходимо сделать').grid(row=2, column=2, stick='we', columnspan=3)
get_mode = tk.IntVar(value=0)
tk.Radiobutton(text='3.1) Пронумервать все\nизображения из папки', variable = get_mode, value = 0, justify='left')\
    .grid(row=3, column=2, stick='w', pady=[5,0], columnspan=4)
tk.Radiobutton(text='3.2) Заменить одно\nизображение из папки с нумерацией', variable = get_mode, value = 1, justify='left')\
    .grid(row=4, column=2, stick='w', pady=[5,0], columnspan=4)
tk.Radiobutton(text='3.3) Добавить одно\nизображение из папки с нумерацией', variable = get_mode, value = 2, justify='left')\
    .grid(row=5, column=2, stick='w', pady=[5,0], columnspan=4)

tk.Label(text='4. Укажите высоту и цвет текста в формате RGB\n(если необходимо)')\
    .grid(row=6, column=2, stick='w', columnspan=4)
tk.Label(text='R', justify='center').grid(row=7, column=2)
tk.Label(text='G', justify='center').grid(row=7, column=3)
tk.Label(text='B', justify='center').grid(row=7, column=4)
tk.Label(text='Выс.\nшрифта', justify='center').grid(row=7, column=5)
color_field_R = tk.Entry(mn_win, width=5)
color_field_R.grid(row=8, column=2)
color_field_G = tk.Entry(mn_win, width=5)
color_field_G.grid(row=8, column=3)
color_field_B = tk.Entry(mn_win, width=5)
color_field_B.grid(row=8, column=4)
font_sz_field = tk.Entry(mn_win, width=5)
font_sz_field.grid(row=8, column=5)

font_change()

#mn_win.grid_rowconfigure(1, minsize=20)
mn_win.grid_columnconfigure(0, minsize=20)
mn_win.grid_columnconfigure(1, minsize=400)
mn_win.grid_columnconfigure(2, minsize=25)
mn_win.grid_columnconfigure(3, minsize=25)
mn_win.grid_columnconfigure(4, minsize=25)
mn_win.grid_columnconfigure(5, minsize=25)

mn_win.mainloop()



