s="abd"
ans=0
for i in range(len(s)-1):
    a=ord(s[i])
    b=ord(s[i+1])
    temp=abs(a-b)
    ans=temp+ans
print(ans)