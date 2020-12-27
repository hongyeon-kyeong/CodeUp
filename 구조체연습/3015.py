
'''
import struct
n, m = map(int, input().split())
studs = list()

for i in range(n) :
	nm, sc = input().split()
	studs.append(struct.pack('10si', bytes(nm, encoding=
	"euc-kr"), int(sc)))

for i in range(1,n) :
	key = struct.unpack('10si', studs[i])
	isEnd = False
	for j in range(i-1,-1,-1) :
		print(j)
		res = struct.unpack('10si', studs[j])
		if key[1] > res[1] :
			studs[j+1] = studs[j]
		else :
			isEnd = True
	if isEnd : studs[j+1] = key
	else : studs[0] = key

for i in range(m) :
	res = struct.unpack('10si', studs[i])
	print(res[0])
'''
import collections
n, m = map(int, input().split())
studs = list()
Student = collections.namedtuple('Student',['name','score'])

for i in range(n) :
	nm, sc = input().split()
	studs.append(Student(nm, int(sc)))


for i in range(1,n) :
	key = studs[i]
	#isend = False
	for j in range(i-1,-2,-1) :
		if j > -1 and key.score > studs[j].score :
			studs[j+1] = studs[j]
		else :
			break
	studs[j+1] = key
	print(studs)
'''

for size in range(1, n) :
	val = studs[size]
	i = size
	while i > 0 and studs[i-1].score < val.score :
		studs[i] = studs[i-1]
		i -= 1
	studs[i] = val
	print(studs)
'''
for i in range(m) :
	print(studs[i].name)

