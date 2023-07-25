import os 
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile 

def main():
    if path.exists('newfile.txt'):
        # Really basic backup script, src is the path of file.txt, then shutil is used to create an exact copy of that file with the .bak extension
        src = path.realpath('newfile.txt')
        dst = src + ".bak"
        shutil.copy(src, dst)

        # Renames a file
        #os.rename('file.txt', 'newfile.txt')

        # Splits the full path of src into a tuple, and then assigns the first part to root_dir and the second to tail
        root_dir, tail = path.split(src)
        #shutil.make_archive("archive", "zip", root_dir)

        with ZipFile("textzip.zip", "w") as newzip:
            newzip.write("newfile.txt")
            newzip.write("file.txt.bak")
            
    return 0



if __name__ == '__main__':
    main()