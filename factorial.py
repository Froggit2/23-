def test(*params):
    print(params)
def factorial(a):
    if a == 0:
        return 1
    else:
        return(a * factorial(a-1))
print(test(1,2,3,4,5,6))
print(factorial(5))
