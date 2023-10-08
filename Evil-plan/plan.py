
def binary_search(arr, target):
    """
    Perform binary search on a sorted array to find the target value.
    Returns the index of the target value if found, else returns -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example usage:
arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
if result != -1:
    print(f"Found {target} at index {result}")
else:
    print(f"{target} not found in array")
