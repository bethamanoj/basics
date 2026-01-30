n = int(input())
temp=n 
k = 0 
while temp > 0:
	r = temp % 10 
	k = (k*10) + r
	temp //= 10
if (k == n):
	print('Palindrome')
else:
	print('Not a Palindrome')