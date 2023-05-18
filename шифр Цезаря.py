q=[]
s = input('work - ').lower()
n=int(input('key - '))
for i in range(len(s)):
    if s[i] in ',."!':
        q.append(s[i])
        continue
    a = ord(s[i])+n 
    if 97<=a<=122:
        q.append((chr(a)))
        continue
    if a>122:
        q.append((chr(96 + (a-122))))
        continue
        
print(*q)


