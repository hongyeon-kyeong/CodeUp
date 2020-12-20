n = int(input())
data = list(map(int, input().split()))
k = int(input())

def lower_bound(k) :
	for i in range(n) :
		if data[i] >= k :
			return i+1
	return n+1
print(lower_bound(k))