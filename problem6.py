a = []
b = []
def listProd(a,b):

    a.append(int(input("1번째값을 입력하시오: ")))
    a.append(int(input("2번째값을 입력하시오: ")))
    a.append(int(input("3번째값을 입력하시오: ")))
    b.append(int(input("1번째값을 입력하시오: ")))
    b.append(int(input("2번째값을 입력하시오: ")))
    b.append(int(input("3번째값을 입력하시오: ")))

    c = a[0]*b[0]+a[1]*b[1]+a[2]*b[2]
    print(a)
    print(b)
    print(c)
listProd(a,b)