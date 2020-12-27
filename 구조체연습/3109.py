import collections
n = int(input())
Studs = list()
no_list = list()
Students = collections.namedtuple('Students', ['type','no','name'])

for _ in range(n) :
	t, o, nm = input().split()
	if t == 'I' :
		if o in no_list :
			Studs.insert(0,Students(t, int(o), nm))
		else :
			Studs.append(Students(t, int(o), nm))
		no_list.append(o)
	else :
		for stu in Studs :
			if stu.no == int(o) :
				Studs.remove(stu)
				no_list.remove(o)
				break

res = list()
res = list(map(int, input().split()))
m = len(Studs)

Studs.sort()

for r in res :
	print(Studs[r-1].no, Studs[r-1].name)