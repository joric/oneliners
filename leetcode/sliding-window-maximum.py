from lc import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        r, d = [], deque()
        for i, n in enumerate(nums):
            while d and n>=nums[d[-1]]:
                d.pop()
            d.append(i)
            if d[0] == i-k:
                d.popleft()
            r.append(nums[d[0]])
        return r[k-1:]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return (d:=deque()) or reduce(lambda r,p:(next(_ for _ in count() if not(d and p[1]>=nums[d[-1]] and d.pop())),
            d.append(p[0]),d[0]==p[0]-k and d.popleft(),r.append(nums[d[0]])) and r,enumerate(nums),[])[k-1:]

test('''


239. Sliding Window Maximum
Hard

12792

414

Add to List

Share
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
1 <= k <= nums.length


''')
