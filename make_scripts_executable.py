#!/usr/bin/python3

import os
import stat

if __name__ == '__main__':
    for file in os.listdir():
        if "." in file and file.split(".")[1] == "py":
            st = os.stat(file)
            os.chmod(file, st.st_mode | stat.S_IEXEC)

