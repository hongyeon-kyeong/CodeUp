import sys
import math
res = 1
n, k = map(int, sys.stdin.readline().rstrip().split())
i = 0
while i < k :
	res *= n
	n-=1
	i+= 1
res //= math.factorial(k)

print(res)