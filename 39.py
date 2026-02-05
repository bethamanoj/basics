n = list(map(int,input().split()))
k = len (n)
s = 0
for i in n:
    s = s+i
    avg = s//k
print(avg)