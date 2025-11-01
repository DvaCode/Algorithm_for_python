def sol(arr, target):
    size_n = len(arr)
    hashtable = [-1] * (size_n + 1)
    for i in arr:
        hashtable[i % (size_n + 1)] = i
    if hashtable[target % (size_n + 1)] == target:
        return True
    return False

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 8]
    target = 3
    print(sol(arr, target))  # Output: True

    target = 6
    print(sol(arr, target))  # Output: False

    arr = [2, 3, 5, 9]
    target = 10
    print(sol(arr, target))  # Output: True

    target = 25
    print(sol(arr, target))  # Output: False
