'''
삽입 정렬
'''

import sys
n = int(sys.stdin.readline().rstrip())
data = list()
for _ in range(n) :
	data.append(int(sys.stdin.readline().rstrip()))

'''
for i in range(1, n) :
	key = data[i]
	for j in range(i-1,-1,-1) :
		if data[j] > key :
			data[j+1] = data[j]
		else :
			data[j+1] = key
			break
'''
data.sort()

for d in data :
	print(d)
