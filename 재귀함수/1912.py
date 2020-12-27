import sys

n = int(sys.stdin.readline().rstrip())
res = 1
def sol(i, res) :
	if i > 0 :
		res *=i
		i -= 1
		sol(i, res)
	else :
		print(res)

sol(n,res)