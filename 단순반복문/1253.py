a, b = map(int, input().split())
if a > b :
	big = a
	small = b
else :
	big = b
	small = a

while small <= big :
	print(small, end=' ')
	small += 1

