#-*-coding: cp1251 -*-

# Программа вычисляет в днях среднюю задержку
# для каждой даты
# в формировании файлов после регистрации

# Средняя задержка - это среднее арифметическое
# разниц даты, указанной в названии файла и дат регистрации из входящего реквизита

import os
import re
from datetime import datetime, date, time

def reg_list(d):
    global q
    q = 0
    for line in f:
        if line[0] == '7' and line[1] == '5':
            d[q] = line
        else:
            q -= 1
        q += 1

x = os.listdir("D:\\reg\\in")                          #список регов
x_temp = os.listdir("D:\\reg\\in2")                    #что осталось в in2 с прошлого раза
y = "D:\\reg\\in\\"                                    #папка с регами
y2 = "D:\\reg\\in2\\"                                  #собранные по датам реги
v = "D:\\reg\\out\\"                                   #папка с итоговыми файлами

i = 0
ii = 0
iii = 0
name = [0] * 1000000

time = datetime.now()
t = time.strftime("%d-%m-%Y %H-%M-%S")

out =  v + 'задержка регистрации ' + t + ".txt"
k = open(out, "w+", encoding="cp1251")

while iii<len(x_temp):                                  #очищаем in2
    flfl = y2 + x_temp[iii]
    os.remove(flfl)
    iii += 1

print('Собираю файлы по датам:')

while ii<len(x):
    print(x[ii])
    z = y + x[ii]
    name[ii] = x[ii][5] + x[ii][6]+ x[ii][7]+ x[ii][8]+ x[ii][9] + x[ii][10]
    out2 = y2 + name[ii]
    k2 = open(out2, "a", encoding="cp1251")
    f = open(z, "r", encoding="cp1251")
    f1 = f.read()
    k2.write(f1)
    ii += 1

k2.close
f.close

x2 = os.listdir("D:\\areg\\in2")                        #список собранных регов

while i<len(x2):
    print('Обрабатываю: ',x2[i])

    j = 0
    summ = 0
    s = str(x2[i])
    s = '20' + s                                        #преобразование даты в названии рег в человеческий вид
    s = datetime.strptime(s,'%Y%m%d')
    date_reg = [0] * 1000000
    z = y2 + x2[i]
    f = open(z, "r", encoding="cp1251")

    reg_list(date_reg)
    d2 = date_reg[:q:1]

    while j<len(d2):
        d2[j] = date_reg[j][3] + date_reg[j][4] + date_reg[j][5] + date_reg[j][6] + date_reg[j][7] + date_reg[j][8] + date_reg[j][9] + date_reg[j][10] #берем из реквизита только дату
        a = s - datetime.strptime(d2[j],'%d%m%Y')       #разница дат

        if str(a)[1] == ':':
            d2[j] = 0
        else:
            d2[j] = str(a)[0] + str(a)[1]               #берем только количество дней
        j += 1

    maximum = 0
    minimum = 9999
    mes = 0
    #5y = 3y = 1y = 9m = 80d = 4d = 0

    for sch in range(len(d2)):
        if int(d2[sch]) > maximum:
            maximum = int(d2[sch])
        elif int(d2[sch]) < minimum:
            minimum = int(d2[sch])
        elif int(d2[sch])>30:
            mes += 1
        #elif int(d2[sch])>30:
            
    
    for u in range(len(d2)):                            #подсчет среднего арифметического
        summ = summ + int(d2[u])
    av = summ / len(d2)
    av = str(int(av))
    protsent = (mes / len(d2)) * 100

    ostatok = '        максимальная ' + str(maximum) + '\n        минимальная ' + str(minimum) + '\n        задержка более 30 дней '  + str(int(protsent)) + '% (' + str(mes) + ' анкет из ' + str(len(d2)) + ')\n______________________________________________________________________\n\n'
    data = x2[i][4] + x2[i][5] + '.' + x2[i][2] + x2[i][3] + '.' + '20' + x2[i][0] + x2[i][1]

    if (10<int(av)<20):
        itog = data + ':\n        в среднем задержка ' + av + ' дней\n' + ostatok
    elif av[-1] == '1':
        itog = data + ':\n        в среднем задержка ' + av + ' день\n' + ostatok
    elif av[-1] == '2':
        itog = data + ':\n        в среднем задержка ' + av + ' дня\n' + ostatok 
    elif av[-1] == '3':
        itog = data + ':\n        в среднем задержка ' + av + ' дня\n' + ostatok
    elif av[-1] == '4':
        itog = data + ':\n        в среднем задержка ' + av + ' дня\n' + ostatok
    else:
        itog = data + ':\n        в среднем задержка ' + av + ' дней\n' + ostatok

    k.write(itog)
    f.close

    i += 1

k.close()
print("\nГотово! Нажмите enter.")
input()
