from lc import *

# https://leetcode.com/problems/jump-game-vi/discuss/982147/6-short-lines-with-initialization-trick-Python

class Solution:
    def maxResult(self, a: List[int], k: int) -> int:
        q = [(0,-k)]
        for i,x in enumerate(a):
            while i-q[0][1]>k:
                heappop(q)
            x -= q[0][0]
            heappush(q,(-x,i))
        return x

class Solution:
    def maxResult(self, a: List[int], k: int) -> int:
        q=[(0,-k)]
        for i,x in enumerate(a):
            while q[0][1]<i-k:
                heappop(q)
            heappush(q,((r:=q[0][0]-x),i))
        return -r

class Solution:
    def maxResult(self, a: List[int], k: int) -> int:
        q=[(0,-k)];[(next(heappop(q)for _ in count()if q[0][1]>=i-k),heappush(q,((r:=q[0][0]-x),i)))for i,x in enumerate(a)];return -r

test('''
1696. Jump Game VI
Medium

3345

109

Add to List

Share
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.

 

Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0
 

Constraints:

1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4
Accepted
104,398
Submissions
228,258
''')
