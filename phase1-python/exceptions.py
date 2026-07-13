# Without exception handling - this crashes the whole program
def divide_unsafe(a, b):
    return a / b

# With exception handling - this fails gracefully
def divide_safe(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Error: cannot divide by zero"
    except TypeError:
        return "Error: inputs must be numbers"
    finally:
        print("Division attempt completed")

print(divide_safe(10, 2))
print(divide_safe(10, 0))
print(divide_safe(10, "a"))
