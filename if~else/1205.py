'''
-- 혹시 더 좋은 풀이가 있는지 궁금하다!
'''

a, b = map(int, input().split())
sum = a + b
if a > b :
	dif = a - b
else :
	dif = b - a

if sum > dif :
	res = sum 
else :
	res = dif

mul = a * b
if res < mul :
	res = mul

if a > b :
	div = a / b
else :
	div = b /a

if res < div :
	res = div

a2 = a**b

if res < a2 :
	res = a2

b2 =  b**a

if res < b2 :
	res = b2

print('%0.6f' % res)