def Candies(n):
    if n%2==0:  return -1
    a = []
    for i in range(40):
        if n==1:    break
        a.append((n%2)+1)
        n = n//2
    if n!=1:    return -1
    return (a)
 
 
def main():
    t = int(input())
    for ts in range(t):
        n = int(input())
        a = Candies(n)
        if a==-1: print(-1)
        else:
            print(len(a))
            print(a[0],end = ' ')
            for i in range(len(a)-1,0,-1):
                print(a[i],end = ' ')
            print()
main()