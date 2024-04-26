import math
def test(a = 1, b = 'два', c = True):
    print(a,b,c)
    if a == 0:
        return 0
    else:
        a = math.factorial(a)
    test(a)
test(a = 3)