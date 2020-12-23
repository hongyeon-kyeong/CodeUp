n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
for d in data :
	print(d, end=' ')