from lc import *

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if x <= arr[0]: return arr[:k]
        elif arr[n-1] <= x: return arr[n-k:n]
        else:
            index = bisect.bisect_left(arr, x)
            if index < 0: index = -index - 1
                
            low = max(0, index - k - 1)
            high = min(n - 1, index + k - 1)

            while high - low > k - 1:
                if low < 0 or x - arr[low] <= arr[high] - x: high -= 1
                elif (high > n - 1 or x - arr[low]) > (arr[high] - x): low+=1

            return arr[low:high + 1]

# https://leetcode.com/problems/find-k-closest-elements/discuss/782319/Python:-Easy-Heap/1651775

class Solution:
    def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
        return sorted(nsmallest(k, a, key=lambda n:(abs(n-x),n)))

class Solution:
    def findClosestElements(self, a: List[int], k: int, x: int) -> List[int]:
        return sorted(sorted(a,key=lambda e:abs(x-e))[:k])

test('''
658. Find K Closest Elements

Medium

Given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.

An integer a is closer to x than an integer b if:

|a - x| < |b - x|, or
|a - x| == |b - x| and a < b

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]

Constraints:

1 <= k <= arr.length
1 <= arr.length <= 10**4
arr is sorted in ascending order.
-104 <= arr[i], x <= 10**4
''')