if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    store = list(set(arr))
    store.sort()
    print(store[-2])
    