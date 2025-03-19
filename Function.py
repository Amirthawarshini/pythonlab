def outer_function():
    def inner_function():
        return f"This is inner function"   
    return inner_function
        
msg_function = outer_function()
print(msg_function())