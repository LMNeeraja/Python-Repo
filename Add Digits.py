def dig_sum(n):
    s=0
    while(n!=0):
        r=n%10
        s+=r
        n=n//10
    return s
n=int(input())
while(n//10>=1):
    n=dig_sum(n)
print(n)
