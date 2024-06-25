#this function is used to read .json file and parse its data into python's data type

import json

def jsonDataType(filename):

    # if you don't have file then run this code 
    # with open(filename,'w',encoding='utf-8') as writeFile:
    #     x = {'zaid':32,'saad':43,'abdullah':77}
    #     json.dump(x,writeFile)

    with open(filename,'r',encoding='utf-8') as readFile:
        x = json.load(readFile)
        return type(x)
    


filename = str(input("Please Enter a filename to parse data: "))
dataStructure = jsonDataType(filename).__name__
print(dataStructure)