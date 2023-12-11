from lc import *

# editorial (log n)

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        n = len(arr)
        candidates = [arr[n // 4], arr[n // 2], arr[3 * n // 4]]
        target = n / 4
        for candidate in candidates:
            left = bisect_left(arr, candidate)
            right = bisect_right(arr, candidate) - 1
            if right - left + 1 > target:
                return candidate
        return -1

# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/930267/One-line-solution

class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        return Counter(a).most_common()[0][0]

test('''
1287. Element Appearing More Than 25% In Sorted Array
Easy

1048

52

Add to List

Share
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
''')

