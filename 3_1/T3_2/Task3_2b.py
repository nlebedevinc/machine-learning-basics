import sys

print("This is task 2b:")
a = list(map(int, input().split()))
newset = set()
for i in a:
    print('YES') if i in newset else print('NO')
    newset.add(i)
sys.exit(1)

