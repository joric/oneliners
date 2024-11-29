from lc import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i for i,_ in Counter(nums).most_common(k)]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [*zip(*Counter(nums).most_common(k))][0]

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return next(zip(*Counter(nums).most_common(k)))

class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        return dict(Counter(n).most_common(k)) # stopped working since Aug 2023

class Solution:
    def topKFrequent(self, n: List[int], k: int) -> List[int]:
        return sorted({*n},key=n.count)[-k:]

test('''
347. Top K Frequent Elements
Medium

13663

497

Add to List

Share
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
''', sort=True)
