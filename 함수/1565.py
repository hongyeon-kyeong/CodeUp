a, b = map(int,input().split())

'''
def lcm(a,b) :
	if a <= b:
		fin = a
	else :
		fin = b
	res = 1 
	for i in range(1,fin+1) :
		if a%i == 0 and b%i == 0 :
			res = i
	return a//res * b//res * res
	-- 시간초과 후 유클리드 호제법 사용
	https://ko.wikipedia.org/wiki/%EC%9C%A0%ED%81%B4%EB%A6%AC%EB%93%9C_%ED%98%B8%EC%A0%9C%EB%B2%95
'''

def lcm(a,b) :
	if a >= b :
		m = a
		n = b
	else :
		m = b
		n = a
	while True :
		res = m%n
		#print('m', m, 'n', n, 'res', res)
		if res == 0 :
			break
		m = n
		n = res
	return n*(a//n)*(b//n)
	
print(lcm(a,b))