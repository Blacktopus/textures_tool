from buffer import *

csv_name = 'imgs_numbering.csv'

def csv_create():
    global targt_path
    csv_file = open(f'{target_path()}\\{csv_name}', 'w+') #create csv file
    csv_file.write('Index image,name of image\n') #headers for csv
    csv_file.close()

def csv_append(index,file_name):
    csv_file = open(f'{target_path()}\\{csv_name}', 'a')
    csv_file.write(f'{index},{file_name}\n')
    csv_file.close()

def csv_search(name):
    csv_file = open(f'{target_path()}\\{csv_name}', 'r')
    for indx, row in enumerate(csv_file):
        if name in row:
            csv_file.close()
            return indx + 1
        else:
            continue

def csv_len():
    num_last_row = int()
    csv_file = open(f'{target_path()}\\{csv_name}', 'r')
    num_last_row = len(csv_file.readlines())
    csv_file.close()
    return num_last_row
