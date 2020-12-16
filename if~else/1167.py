'''
IDEA
- 배열의 오름차순을 직접 구현해보자.
- 지금 인덱스랑 다음인덱스랑 비교해서 다음 인덱스가 더 작으면 자리를 바꾼다. 그리고 다시 재귀를 돌린다.

- 배열을 줄여나간다고 생각한다.
'''
def sortD(data, i) :
	for j in range(i) :
		if data[j] > data[j+1] :
			temp = data[j]
			data[j] = data[j+1]
			data[j+1] = temp
			sortD(data, j) 



data = list(map(int, input().split()))
sortD(data, len(data)-1)
print(data[1])