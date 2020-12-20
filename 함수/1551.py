n = int(input())
data = list(map(int, input().split()))
k = int(input())

def f(n, data, k) :
	for i in range(n) :
		if data[i] == k :
			return i+1
	return -1
print(f(n, data, k))