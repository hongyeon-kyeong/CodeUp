a, b = map(int, input().split())
x, y, z = map(int, input().split())

res = [[0 for _ in range(b)] for _ in range(a)]
life = [[0 for _ in range(b)] for _ in range(a)]

def chk_life(life, res, i, j) :
	for c in range(i-1,i+2) : 
		for d in range(j-1,j+2) :
			#print('a : ', 'b : ', a, b)
			if c < 0 or d < 0 or c > a-1 or d > b-1 :
				continue
			if c == i and d == j :
				continue
			else :
				#print('res[a][b]', res[a][b])
				if res[c][d] == 1 :
					life[i][j] += 1
					#print('life[a][b] : ', life[a][b])


for i in range(a) :
	res[i] = list(map(int, input().split()))
k = int(input())

for t in range(k) :
	for i in range(a) :
		for j in range(b) :
			 chk_life(life, res, i, j)
	for i in range(a) :
		for j in range(b) :
			if life[i][j] == x :
				res[i][j] = 1
			elif life[i][j] >=z or life[i][j] <=y :
				res[i][j] = 0

for i in range(a) :
	for j in range(b) :
		print(res[i][j], end= ' ')
	print()
