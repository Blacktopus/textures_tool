import tkinter as tk
from tkinter import ttk
from about import open_help
from main import run_program
from style import font_change



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

tk.Button(mn_win, text = 'Применить', command = font_change)\
    .grid(row=9,column=2, columnspan=3)


#mn_win.grid_rowconfigure(1, minsize=20)
mn_win.grid_columnconfigure(0, minsize=20)
mn_win.grid_columnconfigure(1, minsize=400)
mn_win.grid_columnconfigure(2, minsize=25)
mn_win.grid_columnconfigure(3, minsize=25)
mn_win.grid_columnconfigure(4, minsize=25)
mn_win.grid_columnconfigure(5, minsize=25)

mn_win.mainloop()