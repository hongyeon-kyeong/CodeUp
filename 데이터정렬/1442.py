'''
선택 정렬
'''
import sys
n = int(sys.stdin.readline().rstrip())
data = list()

for _ in range(n) :
	data.append(int(sys.stdin.readline().rstrip()))

for i in range(n) :
	min = i
	for j in range(i+1, n) :
		if data[min] > data[j] :
			min = j
	temp = data[i]
	data[i] = data[min]
	data[min] = temp

for d in data :
	print(d)


'''
파이썬 시간초과 이슈로 아래와 같이 제출
import sys
n = int(sys.stdin.readline().rstrip())
data = list()
for _ in range(n) :
	data.append(int(sys.stdin.readline().rstrip()))
data.sort()

for d in data :
	print(d)

'''