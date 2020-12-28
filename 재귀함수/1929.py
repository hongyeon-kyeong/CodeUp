import sys
n = int(sys.stdin.readline().rstrip())
res = list()
def sol(n) :
	if n != 1 :
		res.append(n)
		if n%2 == 0 :
			n = n//2
		else :
			n = 3*n +1
		sol(n)
	elif n == 1 :
		res.append(1)
		prt(res, len(res)-1)

def prt(res, i) :
	if i >= 0 :
		print(res[i])
		i -= 1
		prt(res, i)
sol(n)


