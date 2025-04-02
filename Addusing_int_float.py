def add(a:int, b:int) -> int:
    result = int(a) + int(b)# Explicit conversion
    return result 
# --------------------------------------------
result = add(5.5, 4.5) # Able to get the integer result
print(result)