import collections
n = int(input())
Studs = list()
no_list = list()
Students = collections.namedtuple('Students', ['type','no','name'])

for _ in range(n) :
	t, o, nm = input().split()
	if t == 'I' :
		if o not in no_list :
			Studs.append(Students(t, int(o), nm))
			no_list.append(o)
	else :
		for stu in Studs :
			if stu.no == int(o) :
				Studs.remove(stu)
				no_list.remove(o)

res = list()
res = list(map(int, input().split()))
m = len(Studs)

for i in range(m) :
	key = Studs[i]
	for j in range(i-1,-2,-1) :
		if j > -1 and Studs[j].no > key.no :
			Studs[j+1] = Studs[j]
		else :
			break
	Studs[j+1] = key

for r in res :
	print(Studs[r-1].no, Studs[r-1].name)