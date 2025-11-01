import sys
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    str = [input().rstrip('\n') for _ in range(T)]
    print(str)
    for i in range(T):
        str[i][0] = str[i][0].upper()
        print(str[i])