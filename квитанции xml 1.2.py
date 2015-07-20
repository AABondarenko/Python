#-*-coding: cp1251 -*-

import os
import re

x = os.listdir("D:\\xml\\in")      #список файлов в каталоге
y1 = "D:\\xml\\in\\"               #путь к xmlкам
y2 = "D:\\xml\\out\\kvit_"         #путь к квитанциям
i = 0   	                	 #этот цикл только с нуля!!!
#ras = ".xml"                            #расширение файла квитанции

p = re.compile(r"<ИмяФайла>.*Записей>", re.S)   #шаблон РВ для поиска нужного куска
print("Формирую файлы: ")

while i<len(x):
    z = y1 + x[i]        #путь к нужному в этой итерации файлу
    kvit = y2 + x[i]
    print(kvit)
    f = open(z,"r", encoding="UTF-8")
    f1 = f.read()
    m = p.findall(f1)
    #print(m)
    k = open(kvit, "w", encoding="UTF-8")  #файл квитанции в режиме записи
    k.write("""<?xml version="1.0" encoding="UTF-8" ?><КвитанцияОтвет xmlns="КвитанцияОтвет">""")
    tekst = re.sub(r'ДатаИВремяВыгрузки','ДатаФормирования',m[0]) #замена

    try:
        k.write(tekst)           #пишем найденный кусок в файл квитанции
    except:
        print("list index error")

    #re.sub("ДатаИВремяВыгрузки","ДатаФормирования")
    k.write("<Результат>Успешно</Результат><КоличествоОшибок>0</КоличествоОшибок><Комментарий>тест</Комментарий>")
    k.write("</КвитанцияОтвет>")
    f.close()
    k.close()
    i += 1

print("Готово!")
print("Нажмите Enter для продолжения.")
input()
