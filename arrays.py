def rotate_array(arr, k):
    """Rotate array to the right by k steps"""
    if not arr:
        return arr
    k = k % len(arr)
    return arr[-k:] + arr[:-k]

def remove_duplicates(arr):
    """Remove duplicates from sorted array"""
    if not arr:
        return 0
    i = 0
    for j in range(1, len(arr)):
        if arr[j] != arr[i]:
            i += 1
            arr[i] = arr[j]
    return i + 1

def find_missing_number(arr, n):
    """Find missing number in array from 1 to n"""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

def max_subarray_sum(arr):
    """Find maximum sum of contiguous subarray (Kadane's algorithm)"""
    if not arr:
        return 0
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
