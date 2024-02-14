k= []
for j in range(99999):
    n=0
    i=j
    a=len(str(j))
    while i!=0:
        n = n + (i%10)**a
        i=i//10
    if n==j:
        k.append(j)
print(k)