res = [[0 for _ in range(25)] for _ in range(25)]
life = [[0 for i in range(25)] for j in range(25)]

def chk_life(life, res, i, j) :
	for a in range(i-1,i+2) : 
		for b in range(j-1,j+2) :
			#print('a : ', 'b : ', a, b)
			if a < 0 or b < 0 or a > 24 or b > 24 :
				continue
			if a == i and b == j :
				continue
			else :
				#print('res[a][b]', res[a][b])
				if res[a][b] == 1 :
					life[i][j] += 1
					#print('life[a][b] : ', life[a][b])


for i in range(25) :
	res[i] = list(map(int, input().split()))

for i in range(25) :
	for j in range(25) :
		#print(i, j)
		k = chk_life(life, res, i, j)
'''
for i in range(25) :
	for j in range(25) :
		print(life[i][j], end=' ')
	print()

'''

for i in range(25) :
	for j in range(25) :
		if life[i][j] == 3 :
			print(1, end=' ')
		elif life[i][j] >=4 or life[i][j] <=1 :
			print(0, end=' ')
		elif life[i][j] == 2 and res[i][j] == 1:
			print(1, end=' ')
		else :
			print(0, end=' ')
	print()
