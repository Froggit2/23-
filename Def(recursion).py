import math                         #в интернете нашел я сам не знал как сделать
def test(a = 1, b = 'два', c = True,n = 0):
    print(a,b,c)
    if n == 0:
        return 0
    else:
        n = math.factorial(n)       #в интернете нашел я сам не знал как сделать
    print(n)
test(n = 5)