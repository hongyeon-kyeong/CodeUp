res = [[0 for _ in range(25)] for _ in range(25)]

def chk_life(res, i, j) :
	

for i in range(25) :
	res[i] = list(map(int, input().split()))

for i in range(25) :
	for j in range(25) :
		chk_life(res, i, j)
print(res)