n, g = map(int, input().split())
k = list(map(int, input().split()))
for i in range(0,n,g) :
	min_value = 1000
	for j in range(g) :
		if j+i >= n : break
		min_value = min(min_value, k[j+i])
	print(min_value, end=' ')