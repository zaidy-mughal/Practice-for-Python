# this function is used to read the txt file and count the frequency of each word

def fileReader(filename):
    with open(filename,'r',encoding='utf-8') as file:
        return file.read()


filename = 'test.txt'
with open(filename,'w',encoding='utf-8') as file2:
    file2.write('My name is zaid amjad')

content = fileReader(filename)
print(content)
    