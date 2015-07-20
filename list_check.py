#-*-coding: cp1251 -*-

from datetime import datetime, date, time
global workdir          # директория с проверяемыми файлами
workdir = 'D:\\2015\\проверка май\\'

# ф-ция загрузки списков
def opener(path):
    with open(workdir + path) as f:
        x = f.readlines()
    return x

# ф-ция поэлементной сверки двух списков
def checker(x , y , f_name, temp = ''):
    time = datetime.now()
    t = time.strftime(" (%d %m %Y - %H %M %S)")  # дата-время к имени файла
    for i in x:
        for j in y:
            if i.lower() == j.lower():      # для сравнения все строки приводятся к нижнему регистру
                temp = temp + i
    if len(temp) > 0:                       # записываю, если найдены совпадения
        with open(workdir + f_name + t + '.csv', 'w') as f:
            f.write(temp)


# открываю списки
print('Загружаю csv...')
UK  = opener('входные данные\\В не ранее 01012010.csv')
FR  = opener('входные данные\\Ф не ранее 01012010.csv')
US  = opener('входные данные\\С не ранее 01012010 часть1.csv')
US2 = opener('входные данные\\С не ранее 01012010 часть2.csv')
US3 = opener('входные данные\\С не ранее 01012010 часть3.csv')
US  = US + US2 + US3
AL  = opener('входные данные\\результат А.csv')
ER  = opener('входные данные\\результат Е.csv')
TE  = opener('входные данные\\Т.csv')
F   = opener('входные данные\\Ф.csv')

# проверяю поочередно
print('Проверяю...\n')
checker(UK, AL, 'UK_AL')
checker(UK, ER, 'UK_ER')
checker(UK, TE, 'UK_TE')
checker(UK, F,  'UK_F' )
print('А  проверены')

checker(FR, AL, 'FR_AL')
checker(FR, ER, 'FR_ER')
checker(FR, TE, 'FR_TE')
checker(FR, F,  'FR_F' )
print('Ф   проверены')

checker(US, AL, 'US_AL')
checker(US, ER, 'US_ER')
checker(US, TE, 'US_TE')
checker(US, F,  'US_F')
print('У проверены')

print('\nГотово!')
input()


# TODO
# если дата 00.00.nnnn, то сверять с замененной строкой с проставленными в ней нулями
