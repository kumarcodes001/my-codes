def area(a,b,c):
    s=(a+b+c)/2
    a=s*(s-a)*(s-b)*(s-c)
    return a
a=int(input())
b=int(input())
c=int(input())
print(int(area(a,b,c)))
