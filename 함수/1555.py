n = int(input())

def f(n) :
	sum = 0
	i = 1
	while i <= n :
		sum += i
		i+=1
	return sum

print(f(n))