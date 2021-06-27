
l=int(input())
y=input()

y=y+'Z'
d=0
p=0
m=0
n=0

for i in range(l + 1):
    if(y[i]=='-'):
        d = d + 1
        
    elif(y[i]=='A' and p ==0):
        m+=d + 1
        p ='A'
        d = 0
        
    elif(y[i]=='B' and p ==0):
        n+=1
        p ='B'
        d = 0
        
    elif(y[i]=='A' and p =='A'):
        m+=d + 1
        p ='A'
        d = 0
        
    elif(y[i]=='B' and p =='B'):
        n+= d + 1
        p ='B'
        d = 0
        
    elif(y[i]=='A' and p =='B'):
        m+=1+(d//2)
        n+=(d//2)
        p ='A'
        d = 0
        
    elif(y[i]=='B' and p =='A'):
        n+=1
        p ='B'
        d = 0
        
    elif(y[i]=='Z' and p =='B'):
        n = n + d
if(m>n):
    print('A')
    
elif(m<n):
    print('B')
    
else:
    print("Coalition government")