

def factorial(m):
    fact = 1
    for i in range (1,m+1):
        fact = fact*i
    print("Factorial of", m, "is", fact)
n=int(input("Enter a number: "))
factorial(n)

