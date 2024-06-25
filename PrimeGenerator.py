#this function generates prime number upto given limit

def primeGenerator(limit):
    for num in range(1,(limit+1)):
        count = 0
        for i in range(1,(num+1)):
            if num%i==0:
                count+=1
        if count==2:
            print(num,end=' ')

    print('')


primeGenerator(50)