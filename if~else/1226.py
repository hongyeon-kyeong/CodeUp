rotto = list(map(int, input().split()))
juhee = list(map(int, input().split()))
count = 0
bonus = 'N'
for j in juhee :
	if j == rotto[6] :
		bonus = 'Y'
	for r in range(len(rotto)-1) :
		if j == rotto[r] :
			count += 1
			break

if count >= 6 :
	print('1')
elif count ==5 and bonus == 'Y' :
	print('2')
elif count == 5 :
	print('3')
elif count == 4 :
	print('4')
elif count == 3 :
	print('5')
else :
	print('0')