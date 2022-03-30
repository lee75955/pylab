n=int(input("자연수를 입력하시오: "))

def factorial(a):
    sum=1
    for i in range(1,n+1,1):
        sum *= i
    print(sum)
factorial(n)