n, m , k = map(int, input().split())

ary = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k) :
	x1, y1, x2, y2, u = map(int, input().split())
	
	ary[x1][y1] = ary[x1][y1] + u
	if x2+1 < n and y2+1 < m : 
		ary[x2+1][y2+1] = ary[x2+1][y2+1] + u

	if y2+1 < m :
		ary[x1][y2+1] = ary[x1][y2+1] - u

	if x2+1 < n :
		ary[x2+1][y1] = ary[x2+1][y1] - u

for i in range(n) :
	sum = 0
	for j in range(m) :
		sum += ary[i][j]
		print(ary[i][j], end=' ')
		ary[i][j] = sum
	print()
print()
for i in range(n) :
	for j in range(m) :
		if i > 0 :
			ary[i][j] += ary[i-1][j]
			print(ary[i][j], end=' ')
		else :
			print(ary[i][j], end=' ')
	print()
