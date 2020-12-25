nan = list()
for _ in range(7) :
	nan.append(int(input()))

for i in range(7) :
	max = i
	for j in range(i+1,7) :
		if nan[max] < nan[j] :
			max = j
	temp = nan[max]
	nan[max] = nan[i]
	nan[i] = temp	

print(nan[0])
print(nan[1])