def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
    
#Example usage
n = int(input("Enter the number of fibonacci terms:"))
fibonacci(n)
    