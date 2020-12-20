'''
n = int(input())
i = 1
while i <= n :
	if i%3 == 0 :
		print('X', end=' ')
	else :
		print(i, end=' ')
	i += 1
'''
from collections import Counter
n = int(input())
for i in range(1,n+1) :
  counter = Counter(str(i))
  if (counter['3'] > 0 or counter['6'] > 0 or counter['9']) :
    print('X' * (counter['3'] + counter['6'] + counter['9']), end=' ')
  else :
    print(i, end=' ')