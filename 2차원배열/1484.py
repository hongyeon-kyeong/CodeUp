import sys
n, m = map(int, sys.stdin.readline().rstrip().split())
d = 1

res = [[0 for _ in range(m)] for _ in range(n)]

j = 0
while True :
	for i in range(j, m-1-j, 1) :
		res[j][i] = d
		d+=1
	if d > n*m : break
	for i in range(j, n-1-j, 1) :
		res[i][m-1-j] = d
		d+=1
	if d > n*m : break
	for i in range(m-1-j,j,-1) :
		res[n-1-j][i] =d
		d+=1
	if d > n*m : break
	for i in range(n-1-j,j,-1) :
		res[i][j] =d
		d+=1
	if d > n*m : break
	j +=1

for i in range(n) :	
	for j in range(m) :
		print(res[i][j], end =' ')
	print()

'''
for i in range(0,m-1,1) :
	res[0][i] = d
	d += 1
for i in range(0,n-1,1) :
	res[i][m-1] = d
	d += 1
for i in range(m-1,0,-1) :
	res[n-1][i] = d
	d+=1
for i in range(n-1,0,-1) :
	res[i][0] = d
	d+=1

for i in range(1,m-2,1) :
	res[1][i] = d
	d+=1
for i in range(1,n-2,1) :
	res[i][m-2] = d
	d += 1
for i in range(m-2,0,-1) :
	res[3-1-1][i] = d
	d+=1
'''