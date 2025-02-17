#One time
#program to show constant time complexity

def printnumber(n):

    iteration = 0

    print("The number entered by the user is ", n)

    iteration += 1
    print("Total iterations done in the code is ", iteration,"\n")


printnumber(10)
printnumber(20)

print("\n With any 'n'  the time taken by our code won't change")



#Program to show linear complexity O(n) by entering any n

def OnTime(n):
    iteration = 0
    for i in range(1, n+1):
        iteration += 1
    print("When n is ",n,"Iterations = ", iteration) 

OnTime(10) 
OnTime(20) 
OnTime(42) 

print("\nWith every 'n' the time taken and iterations will increase")




#Program to show time complexity O(n^2) by entering any n

def onsquaretime(n):
    itera = 0
    for i in range(0, n):
        for j in range(0, n):
            print("*", end = " ")
            itera += 1
        print("")
    print("\n When n is ",n," Iterations = ", itera,"\n")

onsquaretime(5)
onsquaretime(4)
onsquaretime(3)

print("\nWith every 'n' the time taken equals n^2")
print("O(n^2)")