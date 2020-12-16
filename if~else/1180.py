'''
문자열을 어떻게 쪼개는지.. 다른 풀이 살펴보기!
'''

n = input()
n_list = list()
for i in n :
	n_list.append(i)

temp = n_list[0]
n_list[0] = n_list[1]
n_list[1] = temp

data = int(n_list[0] + n_list[1]) * 2
if data > 100 :
	data %= 100
print(data)
if data <= 50 :
	print('GOOD')
else :
	print('OH MY GOD')
