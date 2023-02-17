import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont
from errors import error_codes
from work_report import create_file
from file_path import csv_name
from image_saver import save_img
from counter_mark import numbering




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
            elif 1 <= get_mode.get() <= 2:
                if source_file in source_files: #if source_file in source_files:
                    if get_mode.get() == 1:
                        csv_file = open(f'{target_path}\\{csv_name}', 'r')
                        chr_fr_rplce = ['(', ')', '0']
                        for row in csv_file:
                            if source_file in row:
                                row_list = row.split(',')
                                row_numb = row_list[1]
                                for char in row_numb:
                                    if char in chr_fr_rplce:
                                        row_numb = row_numb.replace(char, '')
                                    else:
                                        continue
                                file_indx = int(row_numb)
                                save_img(source_file, numbering(file_indx))
                                csv_file.close()
                                error_codes()
                                break
                            else:
                                continue
                    elif get_mode.get() == 2:
                        csv_file = open(f'{target_path}\\{csv_name}', 'r')
                        last_row = csv_file[-1]
                        chr_fr_rplce = ['(', ')', '0']
                        row_list = last_row.split(',')
                        row_numb = row_list[1]
                        for char in row_numb:
                            if char in chr_fr_rplce:
                                row_numb = row_numb.replace(char, '')
                            else:
                                continue
                        file_indx = int(row_numb+1)
                        save_img(source_file, numbering(file_indx))
                        csv_file.close()
                        error_codes()
                else:
                    error_codes(6)
        except:
            error_codes(4)
    else:
        error_codes(1)
