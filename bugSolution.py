def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(5)) # This works fine
print(factorial(0)) # This also works fine
try:
    print(factorial(-1)) # This will now raise a ValueError
except ValueError as e:
    print(f"Error: {e}") 