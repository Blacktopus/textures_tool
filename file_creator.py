from image_saver import save_img
from counter_mark import csv_crtr
from counter_mark import numbering
from counter_mark import count


def create_file(index,file_name):
    csv_crtr(index,file_name)
    save_img(file_name, numbering(index))
    print(index, ' files ready')
    count(index)