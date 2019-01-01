import sys
from collections import Counter


class Task2d:
    def __init__(self):
        self.n = 0
        self.x = set()
        self.line = set()

    def fill_x_list(self):
        for i in range(self.n-1):
            self.x.add(str(i+1))

    def set_included_values(self):
        buf1 = set()
        # (self.x & self.line)
        buf1.update(self.x & self.line)
        self.x.clear()
        self.x.update(buf1)
        print(sorted(list(self.x)))

    def set_excluded_values(self):
        buf1 = set()
        # print(self.x - self.line)
        buf1.update(self.x - self.line)
        self.x.clear()
        self.x.update(buf1)
        print(sorted(list(self.x)))


if __name__ == '__main__':
    my_task = Task2d()
    print("This is task 2d:")
    print("Enter range")
    my_task.n = int(input())
    my_task.fill_x_list()

    print("Enter numbers")
    buf = input()
    while(buf.lower()!="end"):
        my_task.line = set(buf.split())
        # print("Size of splited items")
        # print(len(my_task.line))
        print("Enter The Answer")
        buf_ans = input()
        if buf_ans.lower() == "yes":
            my_task.set_included_values()
        elif buf_ans.lower() == "no":
            my_task.set_excluded_values()
        print("Enter numbers")
        buf = input()
    print(sorted(list(my_task.x)))
    input()
    sys.exit(1)

