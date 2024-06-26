# this function is used to read the txt file and count the frequency of each word

def wordFrequency(filename):
    with open(filename,'r',encoding='utf-8') as file:
        fullfile = file.read()
        words = fullfile.split()

        for word in words:
            print('{0:10} {1:3}'.format(word,words.count(word)))        



def letterFrequency(fileName):
    with open(fileName,'r',encoding='utf-8') as file:
        fullfile = file.read()

        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        
        for letter in letters:
            print('{0:3} {1:2}'.format(letter,fullfile.count(letter)))




filename = 'test.txt'
with open(filename,'w',encoding='utf-8') as file2:
    file2.write('My name is is zaid amjad')

wordFrequency(filename)
letterFrequency(filename)

    