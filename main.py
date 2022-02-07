# Keywords combiner
# Void 1.0
# author : @notforunder

import sys
import void_colorized
import combiner
import formater

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


def menu():
    banner_print()
    print("Welcome to the Void Word Combiner\n            by " + bc.WARNING + bc.BOLD + "notforunder" + bc.ENDC)
    print("         Current version: " + bc.OKGREEN + bc.BOLD + "1.0" + bc.ENDC)
    print("\n[MENU]")
    print(bc.GREEN + "[1]" + bc.ENDC + " Start combining")
    print(bc.GREEN + "[2]" + bc.ENDC + " Format raw data")
    print(bc.RED + "[Q]" + bc.ENDC + " Quit")


menu()
choice = input("\nEnter option [1-Q]\n>>")
if choice == "1":
    print(bc.WARNING + "Running combiner..." + bc.ENDC)
    combiner.permutationprocess()
elif choice == "2":
    print(bc.WARNING + "Running formatter..." + bc.ENDC)
    formater.format()
elif choice == "Q":
    print(bc.FAIL + "Closing..." + bc.ENDC)
    sys.exit()
else:
    print(bc.WARNING + "Wrong option. Try again..." + bc.ENDC)
