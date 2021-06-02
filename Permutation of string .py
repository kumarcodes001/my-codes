from itertools import permutations
s=input()
sum=0
for p in permutations(s):
    perm=[' '.join(p)]
    sum=sum+1
print(sum)
