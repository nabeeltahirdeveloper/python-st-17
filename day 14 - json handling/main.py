import json     #importing json library

file=open("appVersion.json", "r")   #open required file in read mode

data=file.read()    #storinng file content into data

file.close()    #closing file for saving resources

newData=json.loads(data)    #loads convert string to dict

print(newData['properties']["age"]["minimum"])      #printing age

oldAge=newData['properties']["age"]["minimum"]      #storing current age into oldAge variable

newAge=oldAge+1     #Adding one in current age

newData['properties']["age"]["minimum"]=newAge      # replacing old age with new age

print(newData['properties']["age"]["minimum"])      #printing new age

file=open("appVersion.json", "w")   #open required file in write mode

file.write(json.dumps(newData))     #writing file by converting dict to string using dumps method

file.close()    #closing file for saving resourses


