#!/usr/bin/env python3

import subprocess
import os
# To delete a file or a directory using system commands and print according to returncode

book = input("Enter the file or a directory name:")
decison = input("Are You Sure You Want To Delete {} ? (Y/N)".format(book))
if decison == "Y":
    if os.path.isdir(book):
        dir_result = subprocess.run(["rmdir", book])
        if dir_result.returncode == 0:
            print(dir_result.stdout)
        else:
            print(dir_result.stderr)
    elif not os.path.isdir(book):
        file_result = subprocess.run(["rm", book])
        if file_result.returncode == 0:
            print(file_result.stdout)
        else:
            print(file_result.stderr)
