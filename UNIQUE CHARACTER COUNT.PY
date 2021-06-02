def unique(string):
    seen = {}
    max_len = 0
    start = 0
    for end in range(len(string)):
        if string[end] in seen:
            start = max(start, seen[string[end]] + 1)
        seen[string[end]] = end
        max_len = max(max_len, end-start + 1)
    return max_len
string =str(input())
string=string.replace(' ','')

l = unique(string)
print(l)
