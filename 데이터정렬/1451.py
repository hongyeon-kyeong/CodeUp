n = int(input())
data=list()
for _ in range(n) :
	data.append(int(input()))

data.sort()
for d in data :
	print(d)