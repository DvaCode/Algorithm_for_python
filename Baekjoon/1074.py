import sys

input = sys.stdin.readline

def sol():
    # input part
    N, row, col = map(int, input().split())
    ans = 0

    def z_matrix(N_, r, c):
        # 2 x 2 행렬 Z 동선으로 움직임
        # 4등분 하고 쪼개서 분할
        # offset 값 계산해서 return
        if N_ == 0:
            return 0
        half = 2 ** (N_ - 1)
        offset = 0
        if r < half and c >= half:
            # 제 2사분면
            offset = 4 ** (N_ - 1)
            c -= half
        elif r >= half and c < half:
            # 제 3사분면
            offset = (4 ** (N_ - 1)) * 2
            r -= half
        elif r >= half and c >= half:
            # 제 4사분면
            offset = (4 ** (N_ - 1)) * 3
            r -= half
            c -= half

        return offset + z_matrix(N_ - 1, r, c)

    ans = z_matrix(N, row, col)

    print(ans)

sol()
