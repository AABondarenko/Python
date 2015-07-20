#-*-coding: cp1251 -*-

import os
start_path = 'D:\\! 2014\\ФОТО\\222'
output = 'D:\\! 2014\\ФОТО\\sizes.txt'
output2 = 'D:\\! 2014\\ФОТО\\big_small.txt'
k = open(output, "w+", encoding="cp1251")
k2 = open(output2, "w+", encoding="cp1251")
big = small = 0
porog = 4000
for dirpath, dirnames, filenames in os.walk(start_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.getsize(fp) > porog:
            big += 1
        else:
            small += 1
        k.write(str(os.path.getsize(fp)) + '\n')
k2.write('big: ' + str(big) + '\nsmall: ' + str(small))
k.close()
k2.close()
print('done')
input()
