import sys
from collections import Counter


class Task1a:
    def __init__(self):
        self.x = 0

    def find_last_words_count(self):
        a = (1, [1, 2])
        addedValue = self.x
        print(a)
        a[1].append(addedValue)
        print(a)


if __name__ == '__main__':
    my_task = Task1a()
    print("This is task 1a:")
    print("Enter the word combination:")
    my_task.x = int(input())
    my_task.find_last_words_count()
    input()
    sys.exit(1)

