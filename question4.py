for _ in range(int(input())):
    n=int(input())
    s=list(map(str,input().split()))
    f=0
    if s[n-1]=="cookie":
        print("NO")
        f=1
    else:
        for i in range(n-1):
            if s[i]=="cookie" and s[i+1]!="milk":
                f=1
                print("NO")
                break
    if f==0:
        print("YES")