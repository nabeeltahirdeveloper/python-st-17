# listVar=[1,2,3,4,5]

# print(listVar[4])


# dictVar={'name':"nabeel", 'age':25, 'city':'karachi', "food":["pizza", "burger", "chicken", ["pasta", "rice"]]}

# print(dictVar['food'][3][0])


dictVar={'name':"nabeel", 'age':25, 'city':'karachi', "food":{'chicken':"rice", "fastfood":["pizza", "burger", "chicken"]}}

print(dictVar["food"]['fastfood'][2])
    # pep8 rule

if True:
    print("if working")

# if <condition> 


if 55==55:
    print('your math is wrong')
elif 45==45:
    print("here you win")
else:
    print("you are right")