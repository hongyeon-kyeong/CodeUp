def f(n,data) :
	min_value = 100000000000000
	for i in range(n) :
		if min_value > data[i] : 
			min_value = data[i]
	return min_value


n = int(input())
data = list(map(int, input().split()))

print(f(n,data))