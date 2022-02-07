# Format rawdata to workable data
# Void 1.0
# author : @notforunder

import re
import void_colorized

bc = void_colorized.Color


def format():
    print(bc.WARNING + "Formatting started..." + bc.ENDC)
    string = open('rawdata.txt').read()
    new_str = re.sub('[^a-zA-z0-9\n\.]', '', string)
    open('rawdata.txt', 'w').write(new_str)
    print(bc.OKGREEN + "File successfully formatted" + bc.ENDC)
