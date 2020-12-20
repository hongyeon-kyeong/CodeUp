n = int(input())
data = list(map(int, input().split()))
a, b = map(int, input().split())

def maxi(a,b) :
	max_value = -2147483649
	res = 0
	for i in range(a, b+1) :
		if max_value < data[i-1] :
			max_value = data[i-1]
			res = i
	return res
print(maxi(a,b))