import sys
sys.setrecursionlimit(1000000)

def sol(k, n) :
	res = 0
	if k == 0 :
		res += n
	else :
		while n > 0 :
			res += sol(k-1,n)
			n -= 1
	#print(k, n, res)
	return res

try :
	while 1 :
		res = 0
		k, n = map(int, sys.stdin.readline().rstrip().split())
		while n > 0 :
			res += sol(k-1,n)
			n -=1
		print(res)
except :
	exit()	