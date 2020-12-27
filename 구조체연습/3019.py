import collections
n = int(input())
Schedule = list()
Sche = collections.namedtuple('Sche',['name','year','month','day'])
for _ in range(n) :
	nm, y, m, d = input().split()
	Schedule.append(Sche(nm, int(y), int(m), int(d)))

def chg_idx(i, min) :
	temp = Schedule[i]
	Schedule[i] = Schedule[min]
	Schedule[min] = temp

for i in range(n-1) :
	min = i
	for j in range(i+1,n) :
		if Schedule[min].year > Schedule[j].year :
			min = j
		elif Schedule[min].year == Schedule[j].year :
			if Schedule[min].month > Schedule[j].month :
				min = j
			elif Schedule[min].month == Schedule[j].month :
				if Schedule[min].day > Schedule[j].day :
					min = j
				elif Schedule[min].day == Schedule[j].day :
					name1 = Schedule[min].name
					name2 = Schedule[j].name
					len1 = len(name1)
					len2 = len(name2)
					k = 0
					while True :
						if k > len1-1 :
							break 
						elif k > len2-1 :
							min = j
							break
						elif ord(name1[k]) < ord(name2[k]) :
							break
						elif ord(name1[k]) > ord(name2[k]) :
							min = j
							break
						else :
							k += 1
	chg_idx(i,min) 

for i in range(n) :
	print(Schedule[i].name)