#this function checks whether the given string is palindrome or not

def isPalindrom(string):
    length = int(len(string)/2)

    # for i in range(length):
    if string[i] != string[-(i+1)]:
        return False
    return True
        
    

string = 'zaiaz'
print(isPalindrom(string))