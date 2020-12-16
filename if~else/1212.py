a, b, c = map(int,input().split())
sum = 0 
if a > b :
	num = a 
	sum += b
else :
	num = b
	sum += a
if num > c :
	max = num
	sum += c
else :
	max = c
	sum += num
if max < sum :
	print('yes')
else :
	print('no')


