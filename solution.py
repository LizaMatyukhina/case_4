from os import *
from os.path import *
import sys

# Просмотр каталога
a = getcwd()
names = listdir(a)
files = []

def acceptCommand(x):
    try:
        x = int(x)
    except:
        n = input('Введите правильную команду: \n', )
        acceptCommand(n)
    if (0<x<8)==False:
        n = input('Введите правильную команду: \n',)
        acceptCommand(n)
    return (x)


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


def findFiles(target, path):
    inside = listdir(path)
    for name in inside:
        new = getcwd() + '/' + name
        if isfile(new):
            if name.find(target[0])!= -1:
                target.append(new)
        else:
            try:
                findFiles(target, new)
            except:
                pass
    if len(target)!=1:
        target.pop(0)
        return target
    else:
        return ('Ничего не было найдено')



def runCommand(word):
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
            print(CountBytes(), 'байт')
        elif word == 6:
            a = input('Введите название файла: ')
            target = []
            target.append(a)
            print(findFiles(target, getcwd()))
        main()
    if word == 7:
        print('Программа была закрыта, спасибо за работу!')
        sys.exit()


def main():
    a = getcwd()
    print(a)
    print('''Введите 1, чтобы просмотреть каталог
Введите 2, чтобы переместиться на уровень вверх
Введите 3, чтобы преместиться на уровень вниз
Введите 4, чтобы узнать количество файлов и каталогов
Введите 5, чтобы получить размер текущего каталога
Введите 6, чтобы найти файл
Введите 7, чтобы закрыть программу''')
    runCommand(acceptCommand(input()))



if __name__ == "__main__":
    main()