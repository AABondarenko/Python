#-*-coding: cp1251 -*-

import os
import re

x = os.listdir("D:\\xml\\in")      #������ ������ � ��������
y1 = "D:\\xml\\in\\"               #���� � xml���
y2 = "D:\\xml\\out\\kvit_"         #���� � ����������
i = 0   	                	 #���� ���� ������ � ����!!!
#ras = ".xml"                            #���������� ����� ���������

p = re.compile(r"<��������>.*�������>", re.S)   #������ �� ��� ������ ������� �����
print("�������� �����: ")

while i<len(x):
    z = y1 + x[i]        #���� � ������� � ���� �������� �����
    kvit = y2 + x[i]
    print(kvit)
    f = open(z,"r", encoding="UTF-8")
    f1 = f.read()
    m = p.findall(f1)
    #print(m)
    k = open(kvit, "w", encoding="UTF-8")  #���� ��������� � ������ ������
    k.write("""<?xml version="1.0" encoding="UTF-8" ?><�������������� xmlns="��������������">""")
    tekst = re.sub(r'������������������','����������������',m[0]) #������

    try:
        k.write(tekst)           #����� ��������� ����� � ���� ���������
    except:
        print("list index error")

    #re.sub("������������������","����������������")
    k.write("<���������>�������</���������><����������������>0</����������������><�����������>����</�����������>")
    k.write("</��������������>")
    f.close()
    k.close()
    i += 1

print("������!")
print("������� Enter ��� �����������.")
input()
