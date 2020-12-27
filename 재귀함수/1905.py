import sys
sys.setrecursionlimit(1000000)
n = int(sys.stdin.readline().rstrip())
sum = 0
def sol(i, sum) :
	if i <= n :
		sum += i
		i += 1
		sol(i, sum)
	else :
		print(sum)
sol(1, sum)
