n = int(input())
count = 0
data = list()
i = 1
while i <= n :
	if n % i == 0 :
		count += 1
		data.append(i)
	i += 1

if count == 4 :
	if data[1]**3 == data[3] :
		print('wrong number')
	else : print(data[1],data[2])
else :
	print('wrong number')
