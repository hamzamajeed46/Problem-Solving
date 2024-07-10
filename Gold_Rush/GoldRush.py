def gold_rush(n,m):
    if n==m:
        return 'YES'
    if n % 3 != 0 or m > n:
        return 'NO'
 
    a = [n//3,(n//3)*2]
    i,l = 0,2
    while i < l:
        if a[i]==m:
            return 'YES'
 
        if a[i] % 3 == 0:
            x = a[i]//3
            a.append(x)
            a.append(x*2)
        l = len(a)
        i += 1
    return 'NO'
 
 
 
 
 
 
t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    print(gold_rush(n, m))