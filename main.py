# Keywords combiner
# Void 1.1
# author : @notforunder

import sys
import void_colorized
import combiner
import reader as r

bc = void_colorized.Color


# BANNER PRINT
def banner_print():
    print(bc.RED +
          "\n ██▒   █▓ ▒█████   ██▓▓█████▄ \n"
          "▓██░   █▒▒██▒  ██▒▓██▒▒██▀ ██▌\n"
          " ▓██  █▒░▒██░  ██▒▒██▒░██   █▌\n"
          "  ▒██ █░░▒██   ██░░██░░▓█▄   ▌\n"
          "   ▒▀█░  ░ ████▓▒░░██░░▒████▓ \n"
          "   ░ ▐░  ░ ▒░▒░▒░ ░▓   ▒▒▓  ▒\n"
          "   ░ ░░    ░ ▒ ▒░  ▒ ░ ░ ▒  ▒\n"
          "     ░░  ░ ░ ░ ▒   ▒ ░ ░ ░  ░\n"
          "      ░      ░ ░   ░     ░   \n"
          "     ░                 ░      \n" + bc.ENDC)


def choices():
    choice = input("\nEnter option [1-Q]\n>>")
    if choice == "1":
        print(bc.WARNING + "Running combiner..." + bc.ENDC)
        combiner.permutationprocess()
    elif choice == "2":
        print(bc.WARNING + "Running reader..." + bc.ENDC)
        r.read_file()
    elif choice == "Q" or choice == "q":
        print(bc.FAIL + "Closing..." + bc.ENDC)
        sys.exit()
    else:
        print(bc.WARNING + "Wrong option. Try again..." + bc.ENDC)
        return choices()


def menu():
    print("Welcome to the Void Word Combiner\n            by " + bc.WARNING + bc.BOLD + "notforunder" + bc.ENDC)
    print("         Current version: " + bc.OKGREEN + bc.BOLD + "1.1" + bc.ENDC)
    print("\n[MENU]")
    print(bc.GREEN + "[1]" + bc.ENDC + " Start combining")
    print(bc.GREEN + "[2]" + bc.ENDC + " Read rawdata.txt")
    print(bc.RED + "[Q]" + bc.ENDC + " Quit")
    choices()


def main():
    banner_print()
    menu()


if __name__ == "__main__":
    main()
