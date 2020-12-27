import sys
import collections

Student = collections.namedtuple('Student',['cid','sid','score'])
Studs = []

n = int(sys.stdin.readline().rstrip())
for _ in range(n) :
	c, s, sc = map(int,sys.stdin.readline().rstrip().split())
	Studs.append(Student(c,s,sc))

for i in range(n) :
	for j in range(n-1-i) :
		if Studs[j].score < Studs[j+1].score :
			temp = Studs[j]
			Studs[j] = Studs[j+1]
			Studs[j+1] = temp

#print(Studs)
for i in range(3) :
	if i==2 and Studs[0].cid == Studs[1].cid :
		print(Studs[3].cid, Studs[3].sid)
	else : 
		print(Studs[i].cid, Studs[i].sid)
