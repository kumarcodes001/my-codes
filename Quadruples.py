n=int(input())
l=[int(i) for i in input(). split()]
c=0
for i in range(n-3):
 if l[i]+l[i+1]==l[i+2]+l[i+3]:
  c+=1
print(c)

