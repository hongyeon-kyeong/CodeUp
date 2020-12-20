'''
파이썬 다른 풀이도 있는지 찾아보기
'''

a, b = map(int, input().split())
def myswap() :
	global a, b
	if a > b :
		tmp = a
		a = b
		b = tmp

myswap()
print(a, b)