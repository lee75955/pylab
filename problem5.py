import math
r = int(input("반지름을 입력하시오: "))

def circle(a):
    s,v=0,0
    s=4*math.pi*r*r
    v=4/3*math.pi*r*r*r
    print("구의 겉면적: %d " % s)
    print("구의 부피: %d " % v)
circle(r)