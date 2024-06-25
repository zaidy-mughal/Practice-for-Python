#this function prints fizz if a number is multiple of 3 and buzz if a number is multiple of 5 and if a number is multiple of both it will print fizzbuzz

def fizzbuzz():
    for i in range(100):
        num = i+1
        if num%3==0 and num%5==0:
            print('FizzBuzz')
        elif num%3==0:
            print('Fizz')
        elif num%5==0:
            print('Buzz')
        else:
            print(num)


fizzbuzz()
        