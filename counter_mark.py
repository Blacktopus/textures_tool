from file_path import source_path, target_path, csv_name

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