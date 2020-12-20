maps = [[0 for _ in range(10)] for _ in range(10)]
res = [[0 for _ in range(10)] for _ in range(10)]
for i in range(10) :
	maps[i] = list(map(int, input().split()))

def waterball(maps, i,j,k) :
	for a in range(k+1) :
		if j+a >= 0 and j+a < 10 :
			if maps[i][j+a] != -1 :
				res[i][j+a] = -2
			else :
				break
	for a in range(k+1) :
		if i+a >= 0 and i+a < 10 :
			if maps[i+a][j] != -1 :
				res[i+a][j] = -2
			else :
				break
	for a in range(0,-k-1,-1) :
		if j+a >= 0 and j+a < 10 :
			if maps[i][j+a] != -1 :
				res[i][j+a] = -2
			else :
				break
	for a in range(0,-k-1,-1) :
		if i+a >= 0 and i+a < 10 :
			if maps[i+a][j] != -1 :
				res[i+a][j] = -2
			else :
				break

for i in range(10) :
	for j in range(10) :
		if maps[i][j] > 0 :
			waterball(maps, i,j,maps[i][j])
		if maps[i][j] == -1 :
			res[i][j] = maps[i][j]

n = int(input())
players = list()
for i in range(n) :
	x, y = map(int, input().split())
	if res[x-1][y-1] <= -1 :
		players.append('dead')
	else :
		players.append('survive')
		res[x-1][y-1] = i+1

for i in range(10) :
	for j in range(10) :
		print(res[i][j], end=' ')
	print()

print('Character Information')
for i in range(n) :
	print('player', i+1, players[i])