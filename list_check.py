#-*-coding: cp1251 -*-

from datetime import datetime, date, time
global workdir          # ���������� � ������������ �������
workdir = 'D:\\2015\\�������� ���\\'

# �-��� �������� �������
def opener(path):
    with open(workdir + path) as f:
        x = f.readlines()
    return x

# �-��� ������������ ������ ���� �������
def checker(x , y , f_name, temp = ''):
    time = datetime.now()
    t = time.strftime(" (%d %m %Y - %H %M %S)")  # ����-����� � ����� �����
    for i in x:
        for j in y:
            if i.lower() == j.lower():      # ��� ��������� ��� ������ ���������� � ������� ��������
                temp = temp + i
    if len(temp) > 0:                       # ���������, ���� ������� ����������
        with open(workdir + f_name + t + '.csv', 'w') as f:
            f.write(temp)


# �������� ������
print('�������� csv...')
UK  = opener('������� ������\\� �� ����� 01012010.csv')
FR  = opener('������� ������\\� �� ����� 01012010.csv')
US  = opener('������� ������\\� �� ����� 01012010 �����1.csv')
US2 = opener('������� ������\\� �� ����� 01012010 �����2.csv')
US3 = opener('������� ������\\� �� ����� 01012010 �����3.csv')
US  = US + US2 + US3
AL  = opener('������� ������\\��������� �.csv')
ER  = opener('������� ������\\��������� �.csv')
TE  = opener('������� ������\\�.csv')
F   = opener('������� ������\\�.csv')

# �������� ����������
print('��������...\n')
checker(UK, AL, 'UK_AL')
checker(UK, ER, 'UK_ER')
checker(UK, TE, 'UK_TE')
checker(UK, F,  'UK_F' )
print('�  ���������')

checker(FR, AL, 'FR_AL')
checker(FR, ER, 'FR_ER')
checker(FR, TE, 'FR_TE')
checker(FR, F,  'FR_F' )
print('�   ���������')

checker(US, AL, 'US_AL')
checker(US, ER, 'US_ER')
checker(US, TE, 'US_TE')
checker(US, F,  'US_F')
print('� ���������')

print('\n������!')
input()


# TODO
# ���� ���� 00.00.nnnn, �� ������� � ���������� ������� � �������������� � ��� ������
