n = int(input())
data = list(map(int, input().split()))

res = data.copy()
for i in range(n) :
	for j in range(n-1-i) :
		if res[j] < res[j+1] :
			temp = res[j]
			res[j] = res[j+1]
			res[j+1] = temp

for d in data :
	for i in range(n) :
		if d == res[i] :
			print(d, i+1)
			break