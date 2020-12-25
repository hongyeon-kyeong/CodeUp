'''
n = int(input())
math = list()
comp = list()
idx = list()

for i in range(n) :
	m, c = map(int, input().split())
	math.append(m)
	comp.append(c)
	idx.append(i+1)

def chg_idx(j) :
	temp = math[j]
	math[j] = math[j+1]
	math[j+1] = temp
	tempi = idx[j]
	idx[j] = idx[j+1]
	idx[j+1] = tempi
	tempp = comp[j]
	comp[j] = comp[j+1]
	comp[j+1] = tempp

for i in range(1,n) :
	for j in range(n-i) :
		if math[j] < math[j+1] :
			chg_idx(j)
		elif math[j] == math[j+1] :
			if comp[j] < comp[j+1] :
				chg_idx(j)

for i in range(n) :
	print(idx[i], math[i], comp[i])

'''
import collections
Student = collections.namedtuple('Student', ['id', 'math', 'comp'])
Students = list()

n = int(input())
for i in range(n) :
	m , c = map(int, input().split())
	Students.append(Student(i,m,c))

def chg_idx(j) :
	temp = Students[j]
	Students[j] = Students[j+1]
	Students[j+1] = temp

for i in range(1,n) :
	for j in range(n-i) :
		if Students[j].math < Students[j+1].math :
			chg_idx(j)
		elif Students[j].math == Students[j+1].math :
			if Students[j].comp < Students[j+1].comp :
				chg_idx(j)

for i in range(n) :
	print((Students[i].id)+1, Students[i].math, Students[i].comp)

'''
import struct
n = int(input())
stus = list()
for i in range(n) :
	m, c = map(int, input().split())
	stus.append(struct.pack('iii',i+1,m,c))

def chg_idx(j) :
	temp = stus[j]
	stus[j] = stus[j+1]
	stus[j+1] = temp

for i in range(1,n) :
	for j in range(n-i) :
		stuj = struct.unpack('iii',stus[j])
		stujj = struct.unpack('iii',stus[j+1])

		if stuj[1] < stujj[1] :
			chg_idx(j)
		elif stuj[1] == stujj[1] :
			if stuj[2] < stujj[2] :
				chg_idx(j)

for s in stus :
	res = struct.unpack('iii', s)
	print(res[0], res[1], res[2])
'''