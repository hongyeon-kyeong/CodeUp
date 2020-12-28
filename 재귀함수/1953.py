import sys
n = int(sys.stdin.readline().rstrip())

def sol(i) :
	if i <= n :
		print('*'*i)
		i += 1
		sol(i)
sol(1)