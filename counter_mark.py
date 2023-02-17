import file_path

def csv_crtr(index,file_name):
    csv_file = open(f'{file_path.target_path}\\{file_path.csv_name}', 'a')
    csv_file.write(f'{numbering(index)},{file_name}\n')
    csv_file.close()

def numbering(index):
    qntt_zrs = str('0' * (4 - len(str(index)))) #quantity zeros
    return f'({qntt_zrs}{index})'

def count(index):
    global complete_count
    complete_count.set(f'Файлов готово: {index}')