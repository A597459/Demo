# Recursion in python:
def my_function(k):
    if k > 0:
        result = k + my_function(k - 1)
        print(result)
    else:
        result = 0
        return result

    print("\n\nrecursion Example Results")


my_function(10)
