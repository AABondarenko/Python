import shutil

path = 'D:\\тэмп3\\2'
i = 0
count = 300

while i < count:
    path1 = path + str(i) + '.jpg'
    shutil.copyfile(r'D:\\тэмп3\\2.jpg', path1)
    i += 1
    
