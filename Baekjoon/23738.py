import sys

input = sys.stdin.readline

str = input()
ans_str = []
for ch in str:
    if ch is "B":
        ans_str += "v"
    elif ch is "E":
        ans_str += "ye"
    elif ch is "H":
        ans_str += "n"
    elif ch is "P":
        ans_str += "r"
    elif ch is "C":
        ans_str += "s"
    elif ch is "y":
        ans_str += "u"
    elif ch is "X":
        ans_str += "h"
    elif ch is " ":
        ans_str += " "
    else:
        ans_str += ch.lower()

print(''.join(ans_str))