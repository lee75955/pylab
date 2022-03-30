import random

count,o,x=0,0,0
while True:
    a = random.randint(1, 9)
    b = random.randint(1, 9)
    result = a * b
    ans = int(input("%d * %d 의 답은?" % (a,b)))
    if result == ans:
            print("정답입니다")
            o+=1
            count += 1
    elif result != ans:
            print("오답입니다")
            x+=1
            count += 1
    c = input("계속하시겠습니까?")
    if c.upper() == 'Y':
        continue
    elif c.upper() == 'N':
        d = o/count
        print("정답률은",d,"%입니다")
        break


