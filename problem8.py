a = input("파일을 입력하시오: ")

if a == 'text.py':
    f = open('text.py', 'r')
    i = 0
    while True:
        line = f.readline()
        i += 1
        if line == '':
            break
        print(i, ":", line)
    f.close()
else:
    print("종료하겠습니다")