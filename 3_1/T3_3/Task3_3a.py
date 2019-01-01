tokens = input().split()

result = {}
for tkn in tokens:
  cnt = tokens.count(tkn)
  result[tkn] = cnt

print(result)