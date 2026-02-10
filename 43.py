n = list(map(int,input().split()))
largest = 0 
second = 0
for i in n:
	if i>largest:
		second = largest
		largest = i
	elif largest>i>second:
		second = i
print(second)