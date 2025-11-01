import sys

def sol():
    input_str = sys.stdin.readline().strip()
    cnt = 1
    sum = 0

    weight_starNum = 0
    check_num = int(input_str[-1]) # 체크기호
    input_str = input_str[:-1]

    for str in input_str:
        if str != '*':
            sum += int(str) * cnt
        else:
            weight_starNum = cnt

        if cnt == 1:
            cnt = 3
        else:
            cnt = 1
    for i in range(10):
        if (sum + check_num + i * weight_starNum) % 10 == 0:
            print(i)
            break

if __name__ == '__main__':
    sol()