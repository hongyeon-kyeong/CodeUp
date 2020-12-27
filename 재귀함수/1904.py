import sys
a, b = map(int, sys.stdin.readline().rstrip().split())

def sol(i) :
	if i <= b :
		if i%2 == 1 :
			print(i, end = ' ') 
		sol(i+1)
sol(a)