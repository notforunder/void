# Combiner
# Void 1.0
# author : @notforunder

import sys
from itertools import *
import __main__ as m
import void_colorized

bc = void_colorized.Color


def contscript():
    print("Want to continue?")
    choice = input("[Y/N]\n>>")
    if choice == "Y":
        m.menu()
    elif choice == "N":
        print("Ending...")
        sys.exit()
    else:
        print(bc.WARNING + "Wrong option" + bc.ENDC)
        contscript()


def permutationprocess():
    print(bc.WARNING + "Combiner started..." + bc.ENDC)
    # Count how many keywords will be used
    input_num = int(input("Keywords amount : "))

    # Creating blank array
    keywords_list = []

    # Input words and check words amount by input_num
    for i in range(input_num):
        # Counting starts from 0 (Keyword_0, Keyword_1, ...)
        num = str(++i)
        input_words = str(input("Keyword_" + num + " : "))
        keywords_list.append(input_words)

    max_list = 1 + input_num

    # PERMUTATION MAIN PROCESS
    print(bc.OKGREEN + "\nSuccessfully complete. Raw output saved to rawdata.txt")
    print(bc.WARNING + "Run main.py again and use option [2] from menu to format data!!!" + bc.ENDC)
    sys.stdout = open("rawdata.txt", "w")
    for min_list in range(max_list):
        for i in permutations(keywords_list, min_list):
            print(i, end='\n')
    sys.stdout.close()


