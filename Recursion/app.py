def factorial(self, n):
    if n == 1:
        return 1
    n * factorial(n -1)
    

print(factorial(5))