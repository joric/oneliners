from lc import *

# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/

class Solution:
    def canBeEqual(self, a: List[int], b: List[int]) -> bool:
        return sorted(a)==sorted(b)

# https://leetcode.com/problems/make-two-arrays-equal-by-reversing-subarrays/discuss/1517473/99-72-faster-java-solution/

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        xorArr = 0
        xorTarget = 0
        prodTarget = 1
        addTarget = 0
        subTarget = 0
        addArr = 0
        subArr = 0
        prodArr = 1
        for i in range(len(arr)):
            xorTarget ^= target[i]
            prodTarget *= target[i]
            addTarget += target[i]
            subTarget -= target[i]
            xorArr ^= arr[i]
            addArr += arr[i]
            subArr -= arr[i]
            prodArr *= arr[i]
        return xorArr == xorTarget and prodTarget == prodArr and addArr == addTarget and subArr == subTarget;


test('''
1460. Make Two Arrays Equal by Reversing Subarrays
Easy

1040

143

Add to List

Share
You are given two integer arrays of equal length target and arr. In one step, you can select any non-empty subarray of arr and reverse it. You are allowed to make any number of steps.

Return true if you can make arr equal to target or false otherwise.

 

Example 1:

Input: target = [1,2,3,4], arr = [2,4,1,3]
Output: true
Explanation: You can follow the next steps to convert arr to target:
1- Reverse subarray [2,4,1], arr becomes [1,4,2,3]
2- Reverse subarray [4,2], arr becomes [1,2,4,3]
3- Reverse subarray [4,3], arr becomes [1,2,3,4]
There are multiple ways to convert arr to target, this is not the only way to do so.
Example 2:

Input: target = [7], arr = [7]
Output: true
Explanation: arr is equal to target without any reverses.
Example 3:

Input: target = [3,7,9], arr = [3,7,11]
Output: false
Explanation: arr does not have value 9 and it can never be converted to target.

Other Examples

Input: target = [1, 12, 3, 4], arr = [2, 4, 1, 13]
Output: false

These arrays cannot be made equal through reversals, but they will pass all the checks in this method:

XOR: 1 ^ 12 ^ 3 ^ 4 = 2 ^ 4 ^ 1 ^ 13
Product: 1 12 3 4 = 2 4 1 13 = 144
Sum: 1 + 12 + 3 + 4 = 2 + 4 + 1 + 13 = 20
Subtraction: -(1 + 12 + 3 + 4) = -(2 + 4 + 1 + 13) = -20
The method will incorrectly return true for these arrays.

Input: target = [1, 6, 3, 10], arr = [2, 5, 3, 10]
Output: false

Input: target = [2, 3, 5, 6], arr = [1, 4, 5, 6]
Output: false

Input: target = [1, 2, 3, 18], arr = [3, 4, 5, 12]
Output: false

Constraints:

target.length == arr.length
1 <= target.length <= 1000
1 <= target[i] <= 1000
1 <= arr[i] <= 1000
Accepted
131,364
Submissions
182,226
''')