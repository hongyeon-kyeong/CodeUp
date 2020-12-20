a, b = map(int, input().split())
'''
def gen(a,b) :
	res=0
	for i in range(a,b+1) :
		flag = True
		for j in range(i//2,i) :
			sum = 0
			k = str(j)
			for t in k :
				sum += int(t)
			sum += j
			if sum == i :
				flag = False
				break
		if flag :
			res += i
	return res
'''

def gen(a,b) :
	data = list()
	res = 0
	for i in range(1,b) :
		sum = 0
		k = str(i)
		for t in k :
			sum += int(t)
		sum += i
		data.append(sum)
	for i in range(a, b+1) :
		if i not in data :
			res += i
	return res

		
print(gen(a,b))