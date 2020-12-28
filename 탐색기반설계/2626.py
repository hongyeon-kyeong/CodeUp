import sys
n=int(sys.stdin.readline().rstrip())
cnt=0

for k in range(n//3,n//2+1) :
    for i in range(1,n//3+1) :
        j=n-i-k
        if i<=j and j<=k and i+j>k :
            cnt+=1

print(cnt)
