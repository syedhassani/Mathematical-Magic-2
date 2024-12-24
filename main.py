# from math import sqrt
# number=int(input("Enter your number \n"))
# if number>1:
#     for i in range(2,int(sqrt(number))+1):
#         if(number%i==0):
#             print(number, "is not a prime number")
#             break
#         else:
#             print(number, "is a prime number")
# else:
#     print(number, "is not a prime number")
# actvtiy 2
def primeSeive(n):
    prime = [True for i in range(n + 1)]
    currentNumber = 2
    while (currentNumber * currentNumber <= n):
        if (prime[currentNumber] == True):
            for i in range(currentNumber ** 2, n + 1, currentNumber):
                prime[i] = False
        currentNumber += 1
    prime[0]= False
    prime[1]= False
    for p in range(n + 1):
        if prime[p]:
            print(p)


n = int(input("Enter number to find all prime numbers less than the number : "))
primeSeive(n)
print ("Following are the prime numbers smaller.")
print ("than or equal to")
