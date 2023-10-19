# Pascal triangle
from math import factorial

n = int(input())
for i in range(0, n + 1):
    # Pascal triangle using combinations
    # For nth row, pascal triangle elements are, nc0, nc1, nc2, ..., ncn
    print(int(factorial(n)/(factorial(i) * factorial(n - i))), end = " ")
    
