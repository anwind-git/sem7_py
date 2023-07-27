# функция возвращает новую отформатированную строку имени файла

def get_new_filename(new_file_name, num_digits, ext_out, counter):
    return new_file_name + '_' + str(counter).zfill(num_digits) + '.' + ext_out