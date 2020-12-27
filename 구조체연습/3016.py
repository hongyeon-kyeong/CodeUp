import collections
n = int(input())
subA = list()
subB = list()
subC = list()

Student = collections.namedtuple('Student', ['name','fst','scd','trd']) 
for _ in range(n) :
	nm, f, s, t = input().split()
	subA.append(Student(nm, int(f), int(s), int(t)))
	subB.append(Student(nm, int(f), int(s), int(t)))
	subC.append(Student(nm, int(f), int(s), int(t)))

def bubble_sort(data, att) :
	for i in range(n) :
		for j in range(n-i-1) :
			if data[j][att] < data[j+1][att] :
				temp = data[j]
				data[j] = data[j+1]
				data[j+1] = temp

bubble_sort(subA, 1)
bubble_sort(subB, 2)
bubble_sort(subC, 3)

res = [0,0,0]
res[0] = subA[0].name
for i in range(n) :
	if subA[0].scd == subB[i].scd :
		res[1] = i
		break

for i in range(n) :
	if subA[0].trd == subC[i].trd :
		res[2] = i
		break

print(res[0], res[1]+1, res[2]+1)
