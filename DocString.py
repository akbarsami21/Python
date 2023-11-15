
def square(n):
    """this method will return the square of n"""
    return n**2

print(square(5))
print(square.__doc__)

def square(n):
    print("doc string will not show")
    """this method will return the square of n"""
    return n**2

print(square(25))
print(square.__doc__)