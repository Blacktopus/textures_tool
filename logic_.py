#import main
from main import *
import os



def mode_num_all(): # numbering all images
    pass

def run_program():
    global source_path, target_path, field1, field1_1, field2, get_mode
    source_path = r'' + field1.get()
    target_path = r'' + field2.get()
    source_file = field1_1.get()
    file_indx = 1
    try:
        source_files = sorted(os.listdir(source_path)) # get names from directory
        target_files = sorted(os.listdir(target_path))
        if csv_name not in target_files:
                csv_file = open(f'{target_path}\\{csv_name}', 'w+') #create csv file
                csv_file.write('Index image,name of image\n') #headers for csv
                csv_file.close()
        if get_mode.get() == 0:
            if len(source_file) == 0:
                for name in source_files:
                    if '_Sgn_' and '.png' in name:
                        create_file(file_indx,name)
                        file_indx += 1
                    else:
                        continue
            else:
                tags = []
                if ',' in source_file:
                    tags.extend(source_file.split(','))
                else:
                    tags.append(source_file)
                for name in source_files:
                    for tag in tags:
                        if tag and '.png' in name:
                            create_file(file_indx,name)
                            file_indx += 1
                        else:
                            continue
            error_codes()
        elif get_mode.get() == 1:
            if source_file in source_files:
                csv_file = open(f'{target_path}\\{csv_name}', 'r')
                for indx, row in enumerate(csv_file):
                    if source_file in row:
                        file_indx = indx + 1
                        save_img(source_file, numbering(file_indx))
                        csv_file.close()
                        error_codes()
                        break
                    else:
                        continue
            else:
                error_codes(6)
        elif get_mode.get() == 2:
            if source_file in source_files:
                csv_file = open(f'{target_path}\\{csv_name}', 'r')
                file_indx = len(csv_file.readlines())
                save_img(source_file, numbering(file_indx))
                csv_file.close()
                error_codes()
            else:
                error_codes(6)
    except:
        error_codes(4)


