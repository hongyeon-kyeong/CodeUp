import sys
a, b, c = map(int, sys.stdin.readline().rstrip().split())
i = a
j = b
k = c

while i%j != 0 :
	i, j = j, i%j

while a%b != 0 :
	a, b = b, a%b

if j == b :
	print(j)
else :
	while j%b != 0 :
		j, b = b, j%b
	print(b)