
def error_codes(err_code = 0):
    global error_message
    errs_dict = { 
                1: 'укажите отличающиеся пути',
                2: 'в поле цвета могут быть только цифры от 0 до 255',
                3: 'размер шрифта может быть указан только цифрами от 0 до 255',
                4: 'неправильно указан путь',
                5: 'файл "Help" не найден',
                6: 'файл с таким именем не найден',
                7: 'файл не является изображением'
        }
    if err_code == 0:
        error_message.set('')
    elif (err_code > 0) and (err_code in errs_dict):
        error_message.set(f'Ошибка: {errs_dict[err_code]}')
    else:
        error_message.set('Ошибка: неизвестная ошибка')