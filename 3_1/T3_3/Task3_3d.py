d = {}
for i in range(int(input())):
    for word in input().split():
        d[word] = d.get(word, 0) + 1  # в словарь добавляется последнее значение суммы

for i in sorted(d.items(), key=lambda x: (-x[1], x[0])):
    print(i[0])