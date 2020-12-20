def f(n,data) :
	max_value = 0
	res = 0
	for i in range(n) :
		if max_value < data[i] : 
			max_value = data[i]
			res = i
	return res


n = int(input())
data = list(map(int, input().split()))

print(f(n,data)+1)