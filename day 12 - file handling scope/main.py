# import os
# import shutil
# if os.path.isdir("2"):
#     pass
# else:
#     os.mkdir("2")



# shutil.move("1/1.txt", "2/1.txt")

# file=open("2/1.txt", 'a')

# file.write("hello")
# file.close()






# def sumNum(numberOne, numberTwo):
#     global resultNumber
#     resultNumber=numberOne+numberTwo




# sumNum(5,20)
# print(resultNumber)

import json

file=open("newData.json", 'r')
data=file.read()
file.close()

print("this is data:", data)
newData=json.loads(data)
print("description:", newData["description"])
