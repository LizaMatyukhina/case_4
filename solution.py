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


def CountFiles(path):
    count = 0
    if not exists(path):
        return
    files = listdir(path)
    print(files)
    for file in files:
        file_path = join(path, file)
        if isfile(file_path):
            count += 1
        else:
            CountFiles(file_path)


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
            print(CountFiles(a))
            print(sum(len(fs) for _, _, fs in walk(getcwd())))

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