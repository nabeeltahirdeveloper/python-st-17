# import json

# data={
#     "name":'Ali', 'age': 19, "fvrtColor": "blue", "male": True
# }


# file = open("newJson.json", 'w')
# file.write(json.dumps(data))

# file.close()




# print(data)
# print(type(data))
# print(json.dumps(data))
# print(type(json.dumps(data)))


# print(r"hello \2  w\torld")


newDict ={
    "1":{
        "name": "nabeel",
        "gender": "male"
    },
    "2":{
        "name":"naveed",
        "gender":"male"
    }
}

print(newDict["1"]["name"])

newDict["1"]["name"] = "Ali"
print(newDict["1"])
