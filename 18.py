a = int(input())
b = int(input())
m = 0
if a>b:
	k = a
else:
	k = b
for i in range(1,k):
	m += 1
	k = k * m
	if ( k % a == 0 and k % b == 0):
		print(k)
		break