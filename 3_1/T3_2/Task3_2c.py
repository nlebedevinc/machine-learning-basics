import sys
from collections import Counter


class Task2c:
    def __init__(self):
        self.n = 0
        self.m = 0
        self.nSet = set()
        self.mSet = set()

    def solve(self):
        print("In both Sets:")
        print(sorted(list(self.nSet & self.mSet)))
        print("Only in N Set:")
        print(sorted(list(self.nSet - self.mSet)))
        print("Only in M Set:")
        print(sorted(list(self.mSet - self.nSet)))



if __name__ == '__main__':
    my_task = Task2c()
    print("This is task 2c:")
    print("Enter N")
    my_task.n = int(input())
    print("Enter M")
    my_task.m = int(input())

    print("Enter N numbers")
    for i in range(my_task.n):
        my_task.nSet.add(input())

    print("Enter M numbers")
    for i in range(my_task.m):
        my_task.mSet.add(input())

    my_task.solve()

    print("Enter numbers")
    buf = input()

    input()
    sys.exit(1)

