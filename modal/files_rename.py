import os
from modal import file_extension, slice_of_filename, new_filename

# основная функция переименования файлов


def rename_files(dir_path, new_file_name, num_digits, ext_in, ext_out, name_range):
    counter = 1
    for file_name in os.listdir(dir_path):
        if file_extension.get_file_extension(file_name) == ext_in:
            old_name = slice_of_filename.get_slice_of_filename(file_name.partition('.')[0], name_range)
            new_name = new_filename.get_new_filename(new_file_name, num_digits, ext_out, counter)
            os.rename(os.path.join(dir_path, file_name), os.path.join(dir_path, old_name + new_name))
            counter += 1