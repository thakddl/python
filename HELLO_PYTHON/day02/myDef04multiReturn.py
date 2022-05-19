def addMinMulDiv(a, b):
    return a+b, a-b, a*b, a/b

a,b,c,d = addMinMulDiv(4, 5)
e = addMinMulDiv(4, 5)
print(a,b,c,d)
print(e)
print(e[0])
# ()는 튜플이라고 읽는다.작은 배열이라고 생각하면 된다.