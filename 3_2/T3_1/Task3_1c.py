def capitalize(string):
    words = string.split()

    for i in range(len(words)):
        words[i] = words[i].replace(words[i][0], chr(ord(words[i][0]) - 32))

    return ' '.join(words)


a = 'hello, my name is vlad'
print(capitalize(a))