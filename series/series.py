def fibonacci(n):
     # base case
     if n in {0, 1}:
          return n
     return fibonacci(n - 1) + fibonacci(n - 2) # Recursive case