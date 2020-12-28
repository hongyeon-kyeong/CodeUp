import sys
n = int(sys.stdin.readline().rstrip())
count = 0
res = list()
resres = list()
a = n//2 - 1
z = n - a

for i in range(a,0,-1) :
	for j in range(1, z) :
		k = n - i - j
		res = [i, j, k]
		res.sort()
		if res not in resres :
			if res[0] + res[1] > res[2] :
				count += 1
				resres.append(res)
print(count)
		
'''
n=int(input())
cnt=0

for k in range(n//3,n//2+1) :
    for i in range(1,n//3+1) :
        j=n-i-k
        if i<=j and j<=k and i+j>k :
            cnt+=1

print(cnt)
'''