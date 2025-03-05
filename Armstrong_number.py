def is_armstrong(num):
    # Convert the number to string to find its length
    num_str = str(num)
    num_len = len(num_str)
    
    # Calculate the sum of each digits raised to the power of the number's length
    sum = 0
    for digit in num_str:
        sum += int(digit) ** num_len

    # Check if the sum is equal to the original number
    return sum == num

num = int(input("Enter a number: "))
if is_armstrong(num):
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")