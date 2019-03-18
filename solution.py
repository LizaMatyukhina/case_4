from os import *
from os.path import *

# Просмотр каталога
a = getcwd()
names = listdir(a)
files = []


def moveUp():
    chdir('..')

def moveDown(path):
    file = input('Введите название каталога: ')
    if exists(path + '/' + file):
        chdir(file)
    else:
        print('Не удается найти указанный файл: ', file)


def CountFiles(path, count):
    if exists(path) == False:
        return
    files = listdir(path)
    for file in files:
        if isfile(file):
            count += 1
        else:
            CountFiles(file, count)
    return count


def main():
    a = getcwd()
    print(a)
    print('Введите 1, чтобы просмотреть каталог')
    print('Введите 2, чтобы переместиться на уровень вверх')
    print('Введите 3, чтобы преместиться на уровень вниз')
    print('Введите 4, чтобы узнать количество файлов и каталогов')
    print('Введите 7, чтобы закрыть программу')
    word = int(input())
    while word != 7:
        if word == 1:
            for name in names:
                print(name)
        elif word == 2:
            moveUp()
        elif word == 3:
            moveDown(a)
        elif word == 4:
            count = 0
            print(CountFiles(a, count))

        a = getcwd()
        print(a)

        print('Введите 1, чтобы просмотреть каталог')
        print('Введите 2, чтобы переместиться на уровень вверх')
        print('Введите 3, чтобы преместиться на уровень вниз')
        print('Введите 4, чтобы узнать количество файлов и каталогов')
        print('Введите 7, чтобы закрыть программу')

        word = int(input())

    if word == 7:
        print('Программа была закрыта, спасибо за работу!')


if __name__ == "__main__":
    main()