def myfunction(n):
    if (n <= 0):
        return
    for i in range (0, n+1):
        print("Codingal")

    myfunction(n // 2)
    myfunction(n // 3)   

myfunction(5)


def say_hello(n):
    if n <= 0:
        return
    for i in range(n):
        print("Hello")
    say_hello(n - 2)

say_hello(5)    
