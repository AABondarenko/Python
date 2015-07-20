import shutil

path = 'D:\\photo\\'
i = 0
j = 0
copy_count = 1000
source_count = 9

while j < source_count:
    for i in range(copy_count):
        path0 = path + str(j) + '.jpg'
        path1 = path + 'copies\\' + str(j) + ' ' + str(i) + '.jpg'
        shutil.copyfile(path0, path1)
        print(path1)
    j += 1
    
print('\n\n     ! DONE !')
input()
