# функция возвращает фрагмент заданного имени файла
def get_slice_of_filename(old_name, name_range):
    if name_range:
        return old_name[name_range[0]-1:name_range[1]]
    else:
        return old_name