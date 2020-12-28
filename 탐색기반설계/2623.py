import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

# 1)
i = min(a, b)
while i > 1 :
	if a%i == 0 and b%i == 0 :
		break
	else : 
		i -= 1
print(i)

# 2)
while a%b != 0 :
	a, b = b, a%b

print(b)