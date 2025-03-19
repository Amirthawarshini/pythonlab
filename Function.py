<<<<<<< HEAD
def outer_function():
    def inner_function():
        return f"This is inner function"   
    return inner_function
        
msg_function = outer_function()
=======
def outer_function():
    def inner_function():
        return f"This is inner function"   
    return inner_function
        
msg_function = outer_function()
>>>>>>> 710fa2ce603dfcf118d3cbdb3d98c3973e0c732e
print(msg_function())