def fibonacci(n):
     """
     Return the nth value of the Fibonacci series
     
     Parameters:
     n (int): 1 integer
     
     Returns:
     1 integer
     int: For n = 0, return 0
     int: For n = 1, return 1
     int: For n > 1, call F(n-1) and F(n-2) and add them together
     """
     # base case
     if n in {0, 1}:
          return n
     return fibonacci(n - 1) + fibonacci(n - 2) # Recursive case

def lucas(n):
     """
     Return the nth value of the Lucas series
     
     Parameters:
     n(int): 1 integer
     
     Returns:
     1 integer
     int: For n = 0, return 2
     int: For n = 1, return 1
     int: For n > 1, call L(n-1) and L(n-2) and add them together
     """
     # base case
     if n == 0:
          return 2
     if n == 1:
          return 1
     return lucas(n - 1) + lucas(n - 2)
     
     