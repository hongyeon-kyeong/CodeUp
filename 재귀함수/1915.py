import sys
n = int(sys.stdin.readline().rstrip())
count =  0
res = list()
def sol(count) :
	if count < n :
		if count == 0 or count == 1:
			res.append(1)
		else :
			res.append(res[count-2] + res[count-1])
		count += 1
		sol(count)
	elif count == n :
		print(res[n-1])

sol(0)
