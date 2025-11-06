def two_sum(nums, target):
    """Find two numbers that add up to target"""
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []

def is_valid_parentheses(s):
    """Check if string has valid parentheses"""
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            top = stack.pop() if stack else '#'
            if mapping[char] != top:
                return False
        else:
            stack.append(char)

    return not stack

def merge_sorted_arrays(arr1, arr2):
    """Merge two sorted arrays"""
    result = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result
