#k = input()
#for i in range(1,16) :
#	print('%s*%s=%s' % (k,format(i,'X'),format(int('0x'+k,16)*i,'X')))
#print(format(int('0x'+k,16)*15,'X'))
#print(int('0x'+k,16))
'''
k = int(input(),16)
for i in range(1,16) :
	print('%X*%X=%X' % (k, i, (k*i)))
'''
#n = float(input())
#print('%d' % n)

#a = hex(11)
#print(a)

b = format(11,'x')
c = format(11,'X')
print(b)
print(c)