a, b, c = map(int, input().split())

if c >= a+b :
	print('삼각형아님')
elif a == b and b == c :
	print('정삼각형')
elif a == b or b ==c or c == a :
	print('이등변삼각형')
elif a**2 + b**2 == c**2 :
	print('직각삼각형')
else : 
	print('삼각형')