import sys
n = int(sys.stdin.readline().rstrip())
def sol(n) :
	if n != 1 :
		print(n)
		if n%2 == 0 :
			n = n//2
		else :
			n = 3*n +1
		sol(n)
	elif n == 1 :
		print(1)

sol(n)


