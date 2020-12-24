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
			