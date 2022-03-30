a = int(input("Enter a temperature: "))
b = input("Choose: ")
sum = 0
if b.upper() == 'F':
    sum = (9/5)*a+32
    print("%d C = %d F" %(a,sum))
elif b.upper() == 'C':
    sum = (5/9)*(a-32)
    print("%d F = %d C" %(a,sum))