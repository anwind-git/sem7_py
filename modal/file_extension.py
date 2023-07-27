# функция принимает имя файла и возвращает его расширение
def get_file_extension(filename):
    _, _, ext = filename.partition('.')
    return ext if ext else None