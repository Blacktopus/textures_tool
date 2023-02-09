import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont

def cnt():
    global count
    global test_lbl
    count += 1
    test_lbl['text'] = f'Нажатий {count}'

count = 0

mn_win = tk.Tk() #main window
mn_win.title('Texture numb RIGsoft')
mn_win.geometry('800x600')
mn_win.resizable(False, False)
win_logo = tk.PhotoImage(file = 'TeamRIGlogoBlack.png')
mn_win.iconphoto(False, win_logo)
start_msg = tk.Label(mn_win, text = 'Програма для работы с файлами текстур')
start_msg.pack()
test_btn = tk.Button(mn_win, text = 'test_btn', command = cnt)
test_btn.pack()
test_lbl = tk.Label(mn_win, text = f'Нажатий {count}')
test_lbl.pack()


mn_win.mainloop()

