'''def passes(s,t):
    if len(t)==1:
        return 1
    c=0
    for i in s:
        if i=='A':
            c=c+1
        elif i=='B':
            c=c-1
    return c
        
        
s=input()
t=set(s)
print(passes(s,t))'''
def passes(s):
    n=len(s)-1
    i=0
    c=0
    while(i<=n):
        if (i==n):
            return c
        elif s[i]=='A':
            i=i+2
            c +=1
        else:
            i=i-1
            c +=1
    return -1
s=input()
print(passes(s))
    
