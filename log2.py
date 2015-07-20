#-*-coding: cp1251 -*-

#              Скрипт для обработки логов загрузки файлов ре
#   "Папки D:\log\in" и "D:\log\out" должны быть созданы.
#   Выходной файл предполагается обрабатывать в Excel (импорт данных из текста с разделителями запятые).

import os
import re
from datetime import datetime, date, time

x = os.listdir("D:\\log\\in")            #спипсок файлов в каталоге
y1 = "D:\\log\\in\\"                     #путь к логам
y2 = "D:\\log\\out\\out "                #обработанные логи
i = 0
mas = []
time = datetime.now()
t = time.strftime("%d-%m-%Y %H-%M-%S")   #для вставки даты и времени в название
#t = time.isoformat()

p = re.compile(r"Реквизит\n? \n?\d\d\n?[0-9А-ЯЁ\s,.\n\W]*нет\n? \n?в\n? \n?словаре\n? \n?\d\d\d", re.DOTALL)  #поисковый шаблон. некорректно задан (несколько раз одно и то же прописано), но работает!

out = y2 + t + ".txt"
k = open(out, "w+", encoding="cp1251")
print('Обрабатываю:\n')

while i<len(x):
    z = y1 + x[i]
    print(x[i])
    f = open(z,"r", encoding="cp1251")
    f1 = f.read()
    m = p.findall(f1)
    mas = mas + m                         #в файл запишем вне цикла, чтобы разом удалить дубликаты
    #k.write(m)
    f.close()
    
    i += 1

s = str(set(mas))                         #удаление дубликатов

p2 = re.compile(r"(Реквизит \d\d )|(\\n)|({)|(})|(')")  #подчищаем ненужные символы
s2 = p2.sub("",s)
p3 = re.compile(r", ")
s = p3.sub("\n",s2)
p4 = re.compile(r" нет в словаре ")
s2 = p4.sub(",",s)

if mas == []:
    k.write('Отсутствующих словарных значений в логах не найдено.')
else:
    shapka = 'Значение,Словарь\n'
    k.write(shapka)
    k.write(s2)
k.close()

print("\nГотово! Нажмите enter.")
input()
