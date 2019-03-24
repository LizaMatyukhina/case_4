from os import *
from os.path import *
from sys import *

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


def CountFiles():
    summ = 0
    for _, _, files in walk(getcwd()):
        count = len(files)
        summ += count
    return summ


def CountBytes():
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



def main():
    a = getcwd()
    print(a)
    print('Введите 1, чтобы просмотреть каталог')
    print('Введите 2, чтобы переместиться на уровень вверх')
    print('Введите 3, чтобы преместиться на уровень вниз')
    print('Введите 4, чтобы узнать количество файлов и каталогов')
    print('Введите 5, чтобы получить размер текущего каталога')
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
            print(CountFiles())
        elif word == 5:
            print(CountBytes())

        a = getcwd()
        print(a)

        print('Введите 1, чтобы просмотреть каталог')
        print('Введите 2, чтобы переместиться на уровень вверх')
        print('Введите 3, чтобы преместиться на уровень вниз')
        print('Введите 4, чтобы узнать количество файлов и каталогов')
        print('Введите 5, чтобы получить размер текущего каталога')
        print('Введите 7, чтобы закрыть программу')

        word = int(input())

    if word == 7:
        print('Программа была закрыта, спасибо за работу!')


if __name__ == "__main__":
    main()