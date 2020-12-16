S = input()
for s in S :
	if s == ' ' :
		print(' ', end='')
	elif s == 'a' :
		print('x',end='')
	elif s == 'b' :
		print('y',end='') 
	elif s == 'c' :
		print('z',end='')
	else :
		print(chr(ord(s) - 3), end='')