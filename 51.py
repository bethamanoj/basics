def palindrome(n):
	temp = n 
	k = 0
	while temp >0:
	    r = temp % 10
	    k = k * 10 + r
	    temp = temp // 10 
	return k
n = int(input())
m =palindrome(n)
if (n == m):
    print('Palindrome')
else:
    print('not')