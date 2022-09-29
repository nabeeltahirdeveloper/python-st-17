# file=open("main.txt", 'w')
# file.write("hello world")
# file.close()


# file=open("main.txt", 'r')
# print(file.readlines())
# file.close()


import os
import shutil
# os.remove('D:\Projects\python-st-17\day 11 - file handling\main.txt')

# shutil.copyfile("main.txt", "test/new.txt")
shutil.copytree(r"test", "new1")



