a, m , d, n = map(int, input().split())
res = a
for i in range(n-1) :
	res *= m
	res += d

print(res)