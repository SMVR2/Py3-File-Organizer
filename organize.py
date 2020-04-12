#Originally Made by Noelia Sales Montes
#Brought to python3 and edited by Sam Morris
"""
Python script that organizes the working directory files according to their
name.

CORRECT USAGE: python organize.py [-v] [-h|-s|-f]
  * -v -> enable verbose mode
  * -h o --help
  * -s o --secure -> copy files
  * -f o --force -> force the movement of files
                    If file already exists, it is deleted
"""

import sys
import os
import shutil
import getopt
import glob

# Regular expressions of files to process
__exreg__ = ['*.mp3', '*.deb','*.AppImage', '*.iso', '*.jpg', '*.jpeg', '*.png',
]
# Directories for each of the above files, change the x's to your username and file folders 
__dirs__ = ['/home/xxxx/Music','/home/xxxx/Apps','/home/xxxx/Apps','/home/xxxx/Iso',
 '/home/xxxx/Pictures/PicDLS/JPG', '/home/xxxx/Pictures/PicDLS/JPG', '/home/xxxx/Pi
ctures/PicDLS/PNG']
# Options
__verbose__ = False
__secure__ = False
__force__ = False

def usage():
    """
    Print usage
    """
    print("USAGE: python organize.py [-v] [-h|-s|-f]")

def organize():
    """
    Main function which classifies files according to the regular expressions
    """
    indice = 0
    for exp in __exreg__:
        if __verbose__ == True:
            print("Regular expression: %s" % exp)

        # Find files that match with the regular expression
        for __f in glob.glob(exp):
            move(__f, indice)
        indice += 1


def move(__f, __ind):
    """
    Files movement
    """
    # Ensures the directory exists
    if not os.path.exists(__dirs__[__ind]):
        if __verbose__ == True:
            print("Creating %s" % __dirs__[__ind])
        os.makedirs(__dirs__[__ind])

    if __verbose__ == True:
        print("%s => %s" % (__f, __dirs__[__ind]))

    # Copy (__secure__ mode) or move
    try:
        if __secure__ == True:
            shutil.copy(__f, __dirs__[__ind])
        else:
            shutil.move(__f, __dirs__[__ind])
    except shutil.Error:
        # If there is any problem, move is forced
        if __force__ == True:
            try:
                os.remove(os.path.join(__dirs__[__ind], __f))
                print(os.path.join(__dirs__[__ind], __f))
                if __secure__ == True:
                    shutil.copy(__f, __dirs__[__ind])
                else:
                    shutil.move(__f, __dirs__[__ind])
            except shutil.Error:
                print("%s wasn't moved" % __f)
        else:
            print("%s wasn't moved'" % __f)


if __name__ == "__main__":
    try:
        __opts__, __args__ = getopt.getopt(sys.argv[1:],
                                           'shvf', ["secure", "help",
                                                    "__force__"])
    except getopt.GetoptError as __err:
        # Print error and help
        print(str(__err))
        usage()
        sys.exit(2)

    # Identify options
    for o, a in __opts__:
        if o == "-v":
            __verbose__ = True
        elif o in ("-h", "--help"):
            usage()
            sys.exit()
        elif o in ("-s", "--secure"):
            __secure__ = True
        elif o in ("-f", "--__force__"):
            __force__ = True
        else:
            assert False, "Unsupported option"

    organize()
