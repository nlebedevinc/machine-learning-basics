n = int(input())
p = dict(input().split() for j in range(n))
k = input()
for key, value in p.items():
    if k == value:
        print(key)
    if k == key:
        print(value)