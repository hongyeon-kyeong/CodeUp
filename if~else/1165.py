'''
IDEA 
While 시간 < 90
현재 시간 + 5
count

우리 득점 + count + 1

-- 왜 if else일까.. 다른 풀이를 찾아보자!
'''
N, M = map(int, input().split())
count = 0
while N < 90 :
	N += 5
	count += 1
print(count+M)

