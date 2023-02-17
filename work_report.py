import counter_mark # При этом в теле программы надо писать counter_mark.
from image_saver import save_img # При этом можно писать только название функции save_ivg

def create_file(index,file_name):
    counter_mark.csv_crtr(index,file_name)
    save_img(file_name, counter_mark.numbering(index))
    print(index, ' files ready')
    counter_mark.count(index)