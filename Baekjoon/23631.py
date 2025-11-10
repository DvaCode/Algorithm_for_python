import sys
input = sys.stdin.readline
from math import sqrt

def sol(N, K):
    n = int((-1 + sqrt(1+8*(N-1)/K))/2)
    if n % 2 != 0: # n is odd
        distance = K*(n+1)**2//2 - (N - 1)
        direction = 'L'
    else: # n is even
        distance = -1*K*n*(n+2)//2 + (N - 1)
        direction = 'R'
    print(str(distance)+' '+direction+' | n='+str(n))
    
def sol_main(N,K):
    pos = 1
    out_lines = []
    total_run = N - 1
    if total_run == 0:
        out_lines.append("0 R")
        sys.stdout.write("\n".join(out_lines))
        print()
        return
        
        # 문제의 뛰기 패턴: 첫 번째 뛰기는 K, 두 번째는 2K, 세 번째는 3K, … 
        # t번 뛰면 누적 거리는 S(t) = K * t*(t+1)//2 입니다.
        # t의 최대값 t_max를, S(t) <= total_run 를 만족하는 최대 정수 t로 구해야 한다.
        # S(t) <= total_run  ⇔  K*t*(t+1)//2 <= total_run  
        # (정수 나눗셈의 특성을 피하기 위해 양변에 2를 곱하면)
        # ⇔ K * t * (t+1) <= 2*total_run + δ   (여기서 δ는 0 또는 1; 정확하게는 floor 조건)
        # 보다 확실하게는, floor(K*t*(t+1)/2) <= total_run ⇔ K*t*(t+1) < 2*(total_run+1)
        # 를 만족하는 최대 t를 이분탐색으로 구합니다.
        
    lo = 0
    hi = total_run + 1  # t는 total_run 이하임 (실제 t는 훨씬 작지만 upper bound로 충분)
    # 이분탐색: 조건: K * mid * (mid+1) < 2*(total_run+1)
    while lo < hi:
        mid = (lo + hi) // 2
        if K * mid * (mid + 1) < 2 * (total_run + 1):
            lo = mid + 1
        else:
            hi = mid
    t = lo - 1  # 완주한 뛰기 횟수
    
    # 완주한 t번 뛰었을 때의 누적 거리
    S = K * t * (t + 1) // 2  
    # 남은 거리 (다음 뛰기에서 불완전하게 뛸 거리)
    R = total_run - S
    
    # t번 뛰고 난 후 제로x의 위치(pos_complete)는 뛰기의 방향에 따라 결정됨.
    # 뛰기 순서: 1번째(오른쪽), 2번째(왼쪽), 3번째(오른쪽), 4번째(왼쪽), …  
    # 따라서 t가 홀수면 마지막 뛰기는 오른쪽, 짝수면 왼쪽.
    if t % 2 == 1:
        pos_complete = K * ((t + 1) // 2)   # 예: t=3 → 오른쪽으로 (1번째와 3번째): K + 3K = 4K, 즉 (3+1)//2 = 2번 K
    else:
        pos_complete = -K * (t // 2)          # 예: t=2 → 오른쪽: K, 왼쪽: 2K → net = -K
    
    # 이제 R가 0이면, 전환점(뛰기를 끝낸 지점)에 도달한 것이므로, 방향을 바꾼 후 멈춤.
    # R > 0이면, (t+1)번째 뛰기 진행 중에 멈추게 됨.
    if R == 0:
        final_pos = pos_complete
        # 전환점에 도달한 경우, 바로 방향을 바꾼다.
        final_dir = "L" if (t % 2 == 1) else "R"
    else:
        # (t+1)번째 뛰기의 방향: (t+1)이 홀수면 오른쪽, 짝수면 왼쪽.
        if (t + 1) % 2 == 1:
            final_pos = pos_complete + R
            final_dir = "R"
        else:
            final_pos = pos_complete - R
            final_dir = "L"
    
    out_lines.append(f"{final_pos} {final_dir}")
    
    sys.stdout.write("\n".join(out_lines))
    print()

# if __name__ == "__main__":
#     # T = int(input())
#     # for _ in range(T):
#     #     N, K = map(int, input().split())
#     #     sol(N, K)
#     sol(15,3)
#     sol(7,2)
#     sol(20,7)
#     sol(3,2)
#     sol(8,2)
#     sol(5,1)