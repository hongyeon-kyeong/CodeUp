import sys
n, k = map(int, sys.stdin.readline().rstrip().split())

#1) 중복조합을 이용한 풀이
def factorial(n) :
	if n <= 1 :
		return 1
	else :
		return n * factorial(n-1)

blank = n - k

res = factorial(blank+1)//(factorial(k)*factorial(blank+1-k))
print(res)


#2) 재귀함수를 이용한 풀이
