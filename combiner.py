# Combiner
# Void 1.1
# author : @notforunder

import sys
from itertools import *
import __main__ as m
import void_colorized
import time

bc = void_colorized.Color


def continue_script():
    time.sleep(1)
    print("\nWant to continue?")
    choice = input("[Y/N]\n>>")
    if choice == "Y" or choice == "y":
        m.main()
    elif choice == "N" or choice == "n":
        print("Ending...")
        sys.exit()
    else:
        print(bc.WARNING + "Wrong option" + bc.ENDC)
        continue_script()


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
    print(bc.OKGREEN + "\nSuccessfully complete. Raw output saved to rawdata.txt" + bc.ENDC)
    with open("rawdata.txt", "w") as textfile:
        for min_list in range(max_list):
            for i in permutations(keywords_list, min_list):
                textfile.write(' '.join(str(s) for s in i) + '\n')

    continue_script()
