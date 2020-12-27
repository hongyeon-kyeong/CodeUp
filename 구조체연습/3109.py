import collections
import sys
n = int(sys.stdin.readline().rstrip())
Studs = []
no_lst =[]
Students = collections.namedtuple('Students', ['type','no','name'])

for _ in range(n) :
	t, o, nm = sys.stdin.readline().rstrip().split()
	if t == 'I' :
		if o in no_lst :
			Studs.insert(0,Students(t, int(o), nm))
		else :
			Studs.append(Students(t, int(o), nm))
		no_lst.append(o)
	else :
		for stu in Studs :
			if stu.no == int(o) :
				Studs.remove(stu)
				no_lst.remove(o)
				break

a, b, c, d, e = map(int, sys.stdin.readline().rstrip().split())

Studs.sort()

print(Studs[a-1].no, Studs[a-1].name)
print(Studs[b-1].no, Studs[b-1].name)
print(Studs[c-1].no, Studs[c-1].name)
print(Studs[d-1].no, Studs[d-1].name)
print(Studs[e-1].no, Studs[e-1].name)
