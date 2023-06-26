LOCAL_TEST = True


def insertionSort(a):
    for i in range(1, len(a)):
        tmp = a[i]
        j = i
        while(j > 0 and a[j-1] > tmp):
            a[j] = a[j-1]
            j -= 1
        a[j] = tmp
    return a


if __name__ == "__main__":
    if LOCAL_TEST:
        arr = [1, 4, 8, 2, 6, 3, 67, 34, 5, 3, 6, 4, 9]
    else:
        try:
            arr = list(map(int, input()))
        except Exception:
            print("Input is not in the expected format")
            arr = []
    output = insertionSort(arr)
    print(output)
