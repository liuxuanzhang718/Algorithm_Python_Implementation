# Find the minimum subarray in an array using divide and conquer algorithm.

# O(nlogn)
def find_cross_min(arr, left, mid, right):
    left_sum = float('inf')
    current_sum = 0
    for i in range(mid, left - 1, -1):
        current_sum += arr[i]
        if current_sum < left_sum:
            left_sum = current_sum
            left_min = i
    
    right_sum = float('inf')
    current_sum = 0
    for i in range(mid + 1, right + 1):
        current_sum += arr[i]
        if current_sum < right_sum:
            right_sum = current_sum
            right_min = i

    return (left_sum + right_sum, left_min, right_min)


def find_min_subarry_divide_and_conquer_nlogn(arr, left, right):
    # Base case: If there is only one element, return it as the minimum subarray.
    if left == right:
        return (arr[left], left, right)

    # Calculate the middle element
    mid = (left + right) // 2

    # Calculate the minimum subarray on the left and right sides of the middle element.
    (left_min, left_low, left_high) = find_min_subarry_divide_and_conquer_nlogn(arr, left, mid)
    (right_min, right_low, right_high) = find_min_subarry_divide_and_conquer_nlogn(arr, mid + 1, right)


    # Calculate the minimum subarray that crosses the middle element.
    (cross_min, cross_low, cross_high) = find_cross_min(arr, left, mid, right)

    # Return the minimum of the three values.
    if left_min <= right_min and left_min <= cross_min:
        return (left_min, left_low, left_high)
    elif right_min <= left_min and right_min <= cross_min:
        return (right_min, right_low, right_high)
    else:
        return (cross_min, cross_low, cross_high)

# O(n)
class Result:
    def __init__(self, total, prefixSum, prefixL, prefixR, suffixSum, suffixL, suffixR, bestMin, bestMinL, bestMinR):
        self.total = total
        self.prefixSum = prefixSum
        self.prefixL = prefixL
        self.prefixR = prefixR
        self.suffixSum = suffixSum
        self.suffixL = suffixL
        self.suffixR = suffixR
        self.bestMin = bestMin
        self.bestMinL = bestMinL
        self.bestMinR = bestMinR

def find_min_subarray_divide_and_conquer_n(arr, low, high):
    if low == high:
        return Result(arr[low], arr[low], low, low, arr[low], low, low, arr[low], low, low)
    
    mid = (low + high) // 2
    left = find_min_subarray_divide_and_conquer_n(arr, low, mid)
    right = find_min_subarray_divide_and_conquer_n(arr, mid + 1, high)

    total = left.total + right.total
    if left.prefixSum <= left.total + right.prefixSum:
        prefixSum = left.prefixSum
        prefixL = left.prefixL
        prefixR = left.prefixR
    else:
        prefixSum = left.total + right.prefixSum
        prefixL = left.prefixL
        prefixR = right.prefixR

    if right.suffixSum <= right.total + left.suffixSum:
        suffixSum = right.suffixSum
        suffixL = right.suffixL
        suffixR = right.suffixR
    else:
        suffixSum = right.total + left.suffixSum
        suffixL = left.suffixL
        suffixR = right.suffixR

    cross_sum = left.suffixSum + right.prefixSum

    if left.bestMin <= right.bestMin and left.bestMin <= cross_sum:
        bestMin = left.bestMin
        bestMinL = left.bestMinL
        bestMinR = left.bestMinR
    elif right.bestMin <= left.bestMin and right.bestMin <= cross_sum:
        bestMin = right.bestMin
        bestMinL = right.bestMinL
        bestMinR = right.bestMinR
    else:
        bestMin = cross_sum
        bestMinL = left.suffixL
        bestMinR = right.prefixR
    
    return Result(total, prefixSum, prefixL, prefixR, suffixSum, suffixL, suffixR, bestMin, bestMinL, bestMinR)

# DP
# dp[i]: minimum sum of subarray ending at i
# ending at i means include i in the subarray
# dp[i]: min(dp[i - 1] + arr[i], arr[i])
# Base case: dp[0] = arr[0]
def find_min_subarray_dp(arr):
    n = len(arr)
    dp = [0] * n
    dp[0] = arr[0]

    for i in range(1, n):
        dp[i] = min(dp[i - 1] + arr[i], arr[i])
    
    return min(dp)


if __name__ == '__main__':
    # Example array values
    A = [5, -2, 3, -6, 4, -1, 2, -8, 3]
    # Call the function to find the minimum subarray using divide and conquer
    min_value, min_left, min_right = find_min_subarry_divide_and_conquer_nlogn(A, 0, len(A) - 1)
    # Call the function to find the minimum subarray using dynamic programming
    min_value_dp = find_min_subarray_dp(A)
    # Call the function to find the minimum subarray using divide and conquer with Result class
    result = find_min_subarray_divide_and_conquer_n(A, 0, len(A) - 1)
    print(f"The starting position of the minimum subarray is {result.bestMinL}, the ending position is {result.bestMinR}, and the minimum value is {result.bestMin}")
    print(f"The starting position of the minimum subarray is {min_left}, the ending position is {min_right}, and the minimum value is {min_value}")
    print(f"The minimum value is {min_value_dp}")




    