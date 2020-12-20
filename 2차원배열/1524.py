maps = [[0 for _ in range(9)] for _ in range(9)]

for i in range(9) :
	maps[i] = list(map(int, input().split()))

r, c = map(int, input().split())

count = 0

if maps[r-1][c-1] == 1 :
	print(-1)
else :
	for a in range(r-2, r+1) :
		for b in range(c-2, c+1) :
			if a < 0 or b < 0 or a > 8 or b > 8 :
				continue
			elif a == r-1 and b == c-1 :
				continue
			else :
				#print('a : ', a, 'b : ', b, 'maps[a][b] :', maps[a][b])
				if maps[a][b] == 1:
					count +=1
	print(count)

