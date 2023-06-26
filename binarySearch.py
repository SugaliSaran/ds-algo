LOCAL_TEST = True


def binarySearch(a, k):
    l = 0
    r = len(a) - 1
    while(l <= r):
        mid = (l+r)//2
        if k == a[mid]:
            return mid
        elif k < a[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


if __name__ == "__main__":
    if LOCAL_TEST:
        arr = [1, 4, 8, 12, 19, 24, 54, 108, 234]
        num = 20
    else:
        try:
            arr = list(map(int, input()))
            num = int(input())
        except Exception:
            print("Input is not in the expected format")
            arr = []
            num = 0
    output = binarySearch(arr, num)
    print(output)
