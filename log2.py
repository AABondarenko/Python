#-*-coding: cp1251 -*-

#              ������ ��� ��������� ����� �������� ������ ��
#   "����� D:\log\in" � "D:\log\out" ������ ���� �������.
#   �������� ���� �������������� ������������ � Excel (������ ������ �� ������ � ������������� �������).

import os
import re
from datetime import datetime, date, time

x = os.listdir("D:\\log\\in")            #������� ������ � ��������
y1 = "D:\\log\\in\\"                     #���� � �����
y2 = "D:\\log\\out\\out "                #������������ ����
i = 0
mas = []
time = datetime.now()
t = time.strftime("%d-%m-%Y %H-%M-%S")   #��� ������� ���� � ������� � ��������
#t = time.isoformat()

p = re.compile(r"��������\n? \n?\d\d\n?[0-9�-ߨ\s,.\n\W]*���\n? \n?�\n? \n?�������\n? \n?\d\d\d", re.DOTALL)  #��������� ������. ����������� ����� (��������� ��� ���� � �� �� ���������), �� ��������!

out = y2 + t + ".txt"
k = open(out, "w+", encoding="cp1251")
print('�����������:\n')

while i<len(x):
    z = y1 + x[i]
    print(x[i])
    f = open(z,"r", encoding="cp1251")
    f1 = f.read()
    m = p.findall(f1)
    mas = mas + m                         #� ���� ������� ��� �����, ����� ����� ������� ���������
    #k.write(m)
    f.close()
    
    i += 1

s = str(set(mas))                         #�������� ����������

p2 = re.compile(r"(�������� \d\d )|(\\n)|({)|(})|(')")  #��������� �������� �������
s2 = p2.sub("",s)
p3 = re.compile(r", ")
s = p3.sub("\n",s2)
p4 = re.compile(r" ��� � ������� ")
s2 = p4.sub(",",s)

if mas == []:
    k.write('������������� ��������� �������� � ����� �� �������.')
else:
    shapka = '��������,�������\n'
    k.write(shapka)
    k.write(s2)
k.close()

print("\n������! ������� enter.")
input()
