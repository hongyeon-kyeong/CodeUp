m, n, x, y = map(int, input().split())
maps = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n) :
	maps[i] = list(map(int, input().split()))

def getSum(i, j) :
	sum = 0
	for a in range(x) :
		for b in range(y) :
			if i+a >= n or j+b >= m :
				return 0
			else :
				sum += maps[i+a][j+b]
				#print('sum', sum)
	return sum

def getSuml(i, j) :
	sum = 0
	for a in range(y) :
		for b in range(x) :
			if i+a >= n or j+b >= m :
				return 0
			else :
				sum += maps[i+a][j+b]
				#print('sum', sum)
	return sum

max_value = 0
for i in range(n) :
	for j in range(m) :
		max_value = max(max_value, getSum(i, j))
		max_value = max(max_value, getSuml(i, j))
		#print(max_value)

print(max_value)