def bubbleSort(arr):
    boolean = True
    n = len(arr)
    while boolean:
        boolean = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                boolean = True
        n -= 1


A = [2, 8, 5, 3, 9, 4, 1]
bubbleSort(A)
print(A)
