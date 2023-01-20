from lc import *

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        s = {()}
        for x in nums:
            s |= {a + (x,) for a in s if not a or a[-1]<=x}
        return [a for a in s if len(a)>=2]


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        return (s:={()},[s:=s|({a+(x,) for a in s if not a or a[-1]<=x}) for x in nums],[a for a in s if len(a)>1])[-1]

test('''

491. Non-decreasing Subsequences
Medium

1820

162

Add to List

Share
Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with at least two elements. You may return the answer in any order.

 

Example 1:

Input: nums = [4,6,7,7]
Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
Example 2:

Input: nums = [4,4,3,2,1]
Output: [[4,4]]
 

Constraints:

1 <= nums.length <= 15
-100 <= nums[i] <= 100
''',check=lambda res,exp,nums:sorted(map(list,res))==sorted(exp))
