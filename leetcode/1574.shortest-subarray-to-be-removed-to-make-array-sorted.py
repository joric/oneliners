from lc import *

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted

class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left = 0
        while left<n-1 and arr[left] <= arr[left+1]: left +=1
        if left == n-1: return 0
        right = n-1
        while right > left and arr[right-1] <= arr[right]: right-=1
        if right == 0: return n-1
        res = min(n - left - 1, right)
        i = 0
        j = right
        while i <= left and j < n:
            if arr[j] >= arr[i]:
                res = min(res, j - i - 1)
                i+=1
            else:
                j+=1
        return res

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/831006/ororor-Python-3-ororor-Thoughts

class Solution:
    def findLengthOfShortestSubarray(self, a: List[int]) -> int:
        n,j = len(a),0
        for j in reversed(range(n)):
            if a[j-1]>a[j]:
                break
        if j == 0:
            return 0
        r = j
        for i in range(n):
            if i>0 and a[i-1]>a[i]:
                break
            while j<n and a[i]>a[j]:
                j += 1
            r = min(r, j - i - 1)
        return r

# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/discuss/6046121/Python

class Solution:
    def findLengthOfShortestSubarray(self, a: List[int]) -> int:
        l = 1
        while l<len(a)and a[l]>=a[l-1]:
            l += 1

        r = len(a)-1
        while r>=0 and a[r]>=a[r-1]:
            r -= 1

        t = a[r:]
        return max(0,min(r,min(~i+r+bisect_left(t,a[i])for i in range(l))))

class Solution:
    def findLengthOfShortestSubarray(self, a: List[int]) -> int:
        l = next((i for i in range(1,len(a))if a[i]<a[i-1]),1)
        r = next((i for i in range(len(a)-1,-1,-1)if a[i]<a[i-1]),-1)
        t = a[r:]
        return max(0,min(r,min(r-i-1+bisect_left(t,a[i])for i in range(l))))

class Solution:
    def findLengthOfShortestSubarray(self, a: List[int]) -> int:
        l,r=next((i for i in range(1,len(a))if a[i]<a[i-1]),1),next((i for i in range(len(a)-1,-1,-1)if a[i]<a[i-1]),-1);t=a[r:];return max(0,min(r,min(~i+r+bisect_left(t,a[i])for i in range(l))))

test('''
1574. Shortest Subarray to be Removed to Make Array Sorted
Medium

1831

81

Add to List

Share
Given an integer array arr, remove a subarray (can be empty) from arr such that the remaining elements in arr are non-decreasing.

Return the length of the shortest subarray to remove.

A subarray is a contiguous subsequence of the array.

 

Example 1:

Input: arr = [1,2,3,10,4,2,3,5]
Output: 3
Explanation: The shortest subarray we can remove is [10,4,2] of length 3. The remaining elements after that will be [1,2,3,3,5] which are sorted.
Another correct solution is to remove the subarray [3,10,4].
Example 2:

Input: arr = [5,4,3,2,1]
Output: 4
Explanation: Since the array is strictly decreasing, we can only keep a single element. Therefore we need to remove a subarray of length 4, either [5,4,3,2] or [4,3,2,1].
Example 3:

Input: arr = [1,2,3]
Output: 0
Explanation: The array is already non-decreasing. We do not need to remove any elements.
 

Other examples:

Input: arr = [1,1,1]
Output: 0

Constraints:

1 <= arr.length <= 105
0 <= arr[i] <= 109
Accepted
48,597
Submissions
113,035
''')
