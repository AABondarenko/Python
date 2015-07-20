#-*-coding: cp1251 -*-

import os
import re

x = os.listdir("D:\\Cronos\\temp")
y = "D:\\Cronos\\temp\\"
i = 0
g = re.compile(r";")

print("Обрабатываю:                           |   Завершение:\n                                       |")
while i<len(x):
    z = y + x[i]
    pr = (i/len(x))*100
    print(z, "        |  ", round(pr, 1), "%")
    with open(z, "r+", encoding="cp1251") as f:
        f1 = f.read()
        p = re.sub(g,'',f1)
        f.close()
    with open(z, "w", encoding="cp1251") as f:
        f.write(p)
        f.close()
    i += 1

print("                                       |   100 %\nГотово!")
input()
