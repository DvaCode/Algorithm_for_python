import sys

input = sys.stdin.readline
def sol():
    N = int(input())
    num_set = set()
    for i in range(N):
        cmd_lst = input().split()
        if len(cmd_lst) > 1:
            cmt = cmd_lst[0]
            num = int(cmd_lst[1])
        else:
            cmt = cmd_lst[0]
        
        
        if cmt == "add":
            num_set.add(num)
        elif cmt == "remove":
            num_set.discard(num)
        elif cmt == "check":
            print(1) if num in num_set else print(0)
        elif cmt == "toggle":
            if num in num_set:
                num_set.discard(num)
            else:
                num_set.add(num)
        elif cmt == "all":
            num_set = set(i for i in range(1,21))
        else: # cmt = empty
            num_set.clear()

sol()