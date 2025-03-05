def factorial_iterative(n):
    if n == 0:
        return 1
    else:
        return n * factorial_iterative(n-1)
    
num = int(input("Enter a number: "))
print("factorial of" , num, "is", factorial_iterative(num))