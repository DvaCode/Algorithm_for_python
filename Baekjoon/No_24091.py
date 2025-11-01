import sys
sys.setrecursionlimit(10**9)
def quick_sort(lst, p, r):
    if p < r:
        q = partition(lst, p, r)
        quick_sort(lst, p, q - 1)
        quick_sort(lst, q+1, r)

def swap(lst, i, j):
    global swap_count, K
    lst[i], lst[j] = lst[j], lst[i]
    swap_count += 1
    if swap_count == K:
        print(' '.join(map(str,lst)))
        sys.exit(0)        

def partition(lst, p, r):
    x = lst[r]
    i = p - 1
    for j in range(p, r):
        if lst[j] <= x:
            i += 1
            swap(lst, i, j)
    if i + 1 != r:
        swap(lst, i + 1, r)
    return i + 1

# if __name__ == "__main__":
#     N, K = map(int, input().split())
#     lst = list(map(int, input().split()))
#     swap_count = 0
    
#     quick_sort(lst, 0, N - 1)
#     print(-1)