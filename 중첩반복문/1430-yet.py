'''
천만 * 십만---> 시간초과 ?, 

메모리 초과 발생

'''
'''
N = int(input())
data = list(map(int, input().split()))
M = int(input())
ques = list(map(int, input().split()))

for q in ques :
	if q in data :
		print('1', end=' ')
	else :
		print('0', end=' ')

N = int(input())
S = input()
data = list()
for i in range(len(S)) :
	if S[i] != ' ' :
		if S[i+1] == ' ' :
			data.append(S[i])
		else : 

M = int(input())
S = input()
ques = list()
for s in S :
	if s != ' ' :
		ques.append(int(s))

for q in ques :
	if q in data :
		print('1', end=' ')
	else :
		print('0', end=' ')
'''
import sys
N = int(input())
S = input()
M = int(input())
Q = input()
res = ''
res2 = ''
data = list()
ques = list()
for i in range(len(S)) :
	if S[i] != ' ' :
		if res == '' :
			res = S[i]
		if i < len(S) - 1 :
			if S[i+1] == ' ' :
				data.append(res)
				res = ''
			else :
				res += S[i+1]
		else :
			data.append(res)
#print(data)

for i in range(len(Q)) :
	if Q[i] != ' ' :
		if res2 == '' :
			res2 = Q[i]
		if i < len(Q) - 1 :
			if Q[i+1] == ' ' :
				ques.append(res2)
				res2 = ''
			else :
				res2 += Q[i+1]
		else :
			ques.append(res2) 
#print(ques)

for q in ques :
	if q in data :
		print('1', end=' ')
	else :
		print('0', end=' ') 
