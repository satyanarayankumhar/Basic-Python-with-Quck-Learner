def fizzBuzz(n):
    # Write your code here
    for n in range(1,n+1):
        if(n%3==0 and n%5==0):
            print("FizzBuzz")
        elif(n%3==0):
            print("Fizz")
        elif(n%5==0):
            print("Buzz")
        elif(n%3!=0 and n%5!=0 and n==n):
            print(n)


if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)
