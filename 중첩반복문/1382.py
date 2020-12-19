for i in range(1,10) :
	for j in range(2,6) :
		if j < 5 :
			print(j, 'x', i, '=', '%2d' % (i*j), end='\t')
		else :
			print(j, 'x', i, '=', '%2d' % (i*j), end='')
	print()