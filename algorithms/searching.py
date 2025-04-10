# dsa_visualizer/algorithms/searching.py
import time

def linear_search(arr, target, update_callback):
    for i, num in enumerate(arr):
        update_callback(arr, [i], [])
        time.sleep(0.3)
        if num == target:
            update_callback(arr, [i], [i])
            return i, "O(n)", "O(1)"
    update_callback(arr, [], [])
    return -1, "O(n)", "O(1)"

def binary_search(arr, target, update_callback):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        update_callback(arr, [mid], [])
        time.sleep(0.3)
        if arr[mid] == target:
            update_callback(arr, [mid], [mid])
            return mid, "O(log n)", "O(1)"
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    update_callback(arr, [], [])
    return -1, "O(log n)", "O(1)"

def jump_search(arr, target, update_callback):
    n = len(arr)
    step = int(n**0.5)
    left, right = 0, 0
    while left < n and arr[left] <= target:
        right = min(n - 1, left + step)
        update_callback(arr, range(left, right + 1), [])
        time.sleep(0.3)
        if arr[left] <= target <= arr[right]:
            break
        left += step
    if left >= n or arr[left] > target:
        return -1, "O(√n)", "O(1)"
    while left <= right:
        update_callback(arr, [left], [])
        time.sleep(0.3)
        if arr[left] == target:
            update_callback(arr, [left], [left])
            return left, "O(√n)", "O(1)"
        left += 1
    update_callback(arr, [], [])
    return -1, "O(√n)", "O(1)"