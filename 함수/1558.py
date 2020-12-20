n = input()

def f(n) :
	data = list()
	for i in n :
		data.append(i)
	
	data.reverse()
	return data
print(''.join(f(n)))