#Testing the different loops to see which one works best
def myfunction(n):
    print("\nTime complexity breakdown: ")
    for i in range(0, n+1):
        print("First loop")
    print("\nFirst loop is O(n)\n")


    j = 1
    while(j <= n+1):
        print("Second loop ", j)
        j = j*2
    print("\nSecond loop is O(log n)\n")


    for i in range(0, 100):
        print("Third loop")
    print("\nThird loop is O(n)")

print("Total time complexity is O(n)") 

myfunction(5)

