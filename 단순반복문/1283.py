a = int(input())
b = int(input())
data = list(map(int, input().split()))

sum = a
for d in data :
	sum = (1+d/100)*sum

print('%0.0f' % (sum-a))
if a > sum :
	print('bad')
elif a == sum :
	print('same')
else :
	print('good')
