import sys
n = int(sys.stdin.readline().rstrip())

def sol(i) :
	if i > 0 :
		print(i)
		sol(i-1)
sol(n)