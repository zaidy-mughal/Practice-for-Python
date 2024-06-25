#this function prints the fibuonacci sequence upto given element/limit

def fibounacci(num):
    a,b = 0,1
    for i in range(num):
        print(a,end=' ')
        a,b = b,a+b
    print()

fibounacci(15)
