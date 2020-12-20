'''
다른 좋은 방법이 있을까...
'''

n = input()

def abs(n) :
	if '.' in n :
		n = float(n)
	else :
		n = int(n)
	if n < 0 :
		return -n
	else :
		return n
print(abs(n))