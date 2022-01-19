l = eval(input())
n = []

for i in range(len(l)-1):
    n.append(abs(l[i+1]-l[i]))

c = []
for i,j in zip(n,n[1:]):
    if j > i:
        c.append(True)
    else:
        c.append(False)

print(all(c))
