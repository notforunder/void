# Read results of combiner
# Void 1.1
# author : @notforunder

import __main__ as m
import time


def read_file():
    textfile = open("rawdata.txt", "r")
    tr = textfile.read()
    print(tr)
    time.sleep(1)
    m.main()
