from os import *
from os.path import *
from ru_local import *
import sys


a = getcwd()
names = listdir(a)
files = []


def acceptCommand(x):
    """ Request a number of the command. """
    try:
        x = int(x)
    except:
        n = input(CORRECT_INPUT)
        acceptCommand(n)
    if (0<x<8)==False:
        n = input(CORRECT_INPUT)
        acceptCommand(n)
    return x


def moveUp():
    """ Moving to the level up. """
    chdir('..')


def moveDown(path):
    """ Moving to the level down. """
    file = input(NAME)
    if exists(path + '/' + file):
        chdir(file)
    else:
        print(NO_FILE, file)


def CountFiles():
    """ The number of files in the directory. """
    summ = 0
    for _, _, files in walk(getcwd()):
        count = len(files)
        summ += count
    return summ


def CountBytes():
    """ The total number of bytes. """
    bytes = 0
    a = []
    j = 0
    for k in list(walk(getcwd())):
        a.append(k[0])
    for _, _, files in walk(getcwd()):
        size = 0
        for file in files:
            path = (a[j] + '/' + file)
            if exists(path):
                if isfile(path):
                    size = getsize(path)
        j += 1
        bytes += size
    return bytes


def findFiles(target, path):
    """ Forming a list of ways to files. """
    a = []
    j = 0
    for k in list(walk(getcwd())):
        a.append(k[0])
    for _, _, files in walk(path):
        for file in files:
            new = a[j] + '/' + file
            if isfile(new):
                if file.find(target[0]) != -1:
                    target.append(normpath(new))
        j += 1
    if len(target) != 1:
        target.pop(0)
        return target
    else:
        return NOT_FOUND


def runCommand(word):
    """ Defining the function by the number of the command. """
    while word != 7:
        if word == 1:
            for name in listdir(getcwd()):
                print(name)
        elif word == 2:
            moveUp()
        elif word == 3:
            moveDown(getcwd())
        elif word == 4:
            print(CountFiles())
        elif word == 5:
            print(CountBytes(), BYTE)
        elif word == 6:
            a = input(FILE_NAME)
            target = []
            target.append(a)
            print(findFiles(target, getcwd()))
        main()
    if word == 7:
        print(END_OF_THE_PROGRAM)
        sys.exit()


def main():
    """ The main function. """
    a = getcwd()
    print(a)
    print(MENU)
    runCommand(acceptCommand(input()))


if __name__ == "__main__":
    main()
