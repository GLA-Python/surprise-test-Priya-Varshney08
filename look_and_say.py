def look_and_say(num):
    l=[]
    i = 0
    while i < len(num):
        count = 1
        while i+1 < len(num) and num[i]==num[i+1]:
            i += 1 
            count += 1 
        l.append(str(count)+num[i])
        i += 1 
    return ''.join(l)
z=1
n=int(input())
for i in range(n):
    print(z)
    z=look_and_say(str(z))
