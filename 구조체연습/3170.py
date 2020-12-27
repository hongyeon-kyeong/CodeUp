import collections
n, m = map(int, input().split())
Rst = collections.namedtuple('Rst', ['idx','name','num'])
RstSet = [Rst(-1,'0',0) for _ in range(250)]
#print(RstSet)
for i in range(n) :
	name, num = input().split()
	idx = 0
	for nm in name :
		idx += ord(nm) - 97
	if RstSet[idx].name == name :
		#print(RstSet[idx])
		newNum = RstSet[idx].num + int(num)
		RstSet[idx] = Rst(idx, name, newNum)
	else :
		RstSet[idx] = Rst(idx, name, int(num))

for i in range(m) :
	ques = input()
	idx = 0
	for q in ques :
		idx += ord(q) - 97
	if RstSet[idx].name == ques :
		print(RstSet[idx].num)
	else :
		print(0)
