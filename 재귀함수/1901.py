import sys

n = int(sys.stdin.readline().rstrip())
def sol(i) :
	if i <= n :
		print(i)
		sol(i+1)
sol(1)