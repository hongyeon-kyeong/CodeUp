N = int(input())
data = list(map(int, input().split()))

res = data.copy()
'''
def sort(i) :
	#print('i :', i)
	#print('res[i]', res[i])
	#print('res[i+1', res[i+1])
	if res[i] > res[i+1] :
		temp = res[i]
		res[i] = res[i+1]
		res[i+1] = temp
		if i+2 < N :
			sort(i+1)

i = N-2
while i >= 0 :
	sort(i)
	i -= 1
'''
res.sort()
def srch(low,high,k) :
	idx = (low+high) // 2
	#print('idx : ', idx)
	if res[idx] == k :
		print(idx, end=' ')
		return
	elif res[idx] < k :
		srch(idx+1,high,k)
	else :
		srch(low,idx-1,k)

for i in range(N) :
	srch(0,N-1,data[i])

#print(res)
	