import os
import shutil

def F_replace_infile(file_path, text2search, text2replace):
    temp_path = file_path+'.tmp'
    new_file = open(temp_path,'w')
    old_file = open(file_path)
    for line in old_file:
        new_file.write(line.replace(text2search, text2replace))
    new_file.close()
    old_file.close()
    os.remove(file_path)
    shutil.move(temp_path, file_path)

def is_non_zero_file(fpath):
    return True if os.path.isfile(fpath) and os.path.getsize(fpath) > 0 else False

