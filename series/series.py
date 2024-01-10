def fibonacci(n):
     """
     Return the nth value of the Fibonacci series
     
     Parameters:
     n(int): 1 integer which indicates the index of the number in the series
     
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
     n(int): 1 integer which indicates the index of the number in the series
     
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

def sum_series(n, first_num=0, second_num=1):
     """
     produce numbers from the fibonacci series or lucas series depending on which params are included. if params do not match those series, then add up the numbers of the last two numbers in the series
     
     Parameters:
     n(int): required, integer which indicates the index of the number in the series
     first_num(int): optional with default value of 0; first number in the series
     second_num(int): optional with default value of 1; second number in the series
     
     Returns:
     1 integer
     if first_num=0 and second_num=1 (or optional params left blank), return nth value of the Fibonacci series
     if first_num=2 and second_num=1, return nth value of the Lucas series
     else return the sum of the last two numbers in the series with a starting point of n
     """
     # base case
     if n == 0:
          return first_num
     if n == 1:
          return second_num
     # recursive case
     else:
          return sum_series(n - 1, first_num, second_num) + sum_series(n - 2, first_num, second_num) # recursive case
     
     
print(sum_series(3, 10, 10))
print(sum_series(5, 4, 7))
# 10, 10, 20, 30, 50
# 4, 7, 11, 18, 29 => 47
# L: 2, 1, ....
# Fib: 0, 1, ...
# F(0): 10
# F(1): 10
# F(2): 20
