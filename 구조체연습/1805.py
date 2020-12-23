n = int(input())
idx = list()
data = list()
for i in range(n) :
	id, d = map(int, input().split())
	idx.append(id)
	data.append(d) 

def sort(i) :
	if idx[i] > idx[i+1] :
		temp = idx[i]
		tempd = data[i]

		idx[i] = idx[i+1]
		data[i] = data[i+1]

		idx[i+1] = temp
		data[i+1] = tempd
		
		if i+2 < n :
			sort(i+1)

i = n-2
while i >= 0 :
	sort(i)
	i -= 1

for i in range(n) :
	print(idx[i], data[i])