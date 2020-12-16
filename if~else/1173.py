'''
IDEA 
- 30분 이상 : -30
- 30분 미만 : 60-(30-분) --> 30+분 / 시간 -1
-- 0시 일때 생각못함
'''
h, m = map(int, input().split())
if m >= 30 :
	print(h, m-30)
elif h == 0 :
	print(23,30+m)
else :
	print(h-1,30+m)