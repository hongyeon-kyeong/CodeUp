n = int(input())
data = list(map(int, input().split()))
count = 0
def stop() :
	for k in range(n-1) :
		if data[k] > data[k+1] :
			return False
	return True

for i in range(1,n) :
	if stop() : break
	for j in range(n-i) :
		if data[j] > data[j+1] :
			temp = data[j]
			data[j] = data[j+1]
			data[j+1] = temp
	count +=1
	
print(count)
#for d in data :
#	print(d, end =' ')