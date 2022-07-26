# =========================Loops


# ==========================For Loop
for var in range(30, 51):
    print(var)


animals_name=['cat', 'dog', 'bird', 'fish', 'lion', 'tiger']
print("animals_name:", animals_name)

for i in animals_name:
    print(i)

completeString='A quick brown fox jumps over the lazy dog'

print("completeString:", completeString)
for i in completeString:
    print(i)
# print(completeString[0])
# print(completeString[1])
# print(completeString[2])
# print(completeString[3])
# print(completeString[4])
# print(completeString[5])


# ==================================While Loop
number=500
small_number=100

while small_number>number:
    print(small_number)
    print("small number added")
    small_number=small_number+1