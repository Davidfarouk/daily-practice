def search(arr, x):
    for i, v in enumerate(arr):
        if v == x:
            return i
    return -1
