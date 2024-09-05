from lc import *

# Q1/Q3. https://leetcode.com/contest/biweekly-contest-124/problems/maximum-number-of-operations-with-the-same-score-ii/
# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-ii/

# RedHeadphone
class Solution:
    def maxOperations(self, a: List[int]) -> int:
        @cache
        def f(i,j,k=None):
            if i>=j:
                return 0
            return max([
                1+f(i+2,j,t) if (t:=a[i]+a[i+1])==k or not k else 0, # first two
                1+f(i,j-2,t) if (t:=a[j]+a[j-1])==k or not k else 0, # last two (Q3)
                1+f(i+1,j-1,t) if (t:=a[i]+a[j])==k or not k else 0, # first and last (Q3)
            ])
        return f(0,len(a)-1)

class Solution:
    def maxOperations(self, a: List[int]) -> int:
        return(f:=cache(lambda i,j,k:i<j and max((1+f(i+q,j+p,t)if(t:=a[u]+a[v])==k or not k else 0)for u,v,q,p in((i,i+1,2,0),(j,j-1,0,-2),(i,j,1,-1)))or 0))(0,len(a)-1,None)

test('''
3040. Maximum Number of Operations With the Same Score II
User Accepted:5833
User Tried:9986
Total Accepted:6156
Total Submissions:26305
Difficulty:Medium
Given an array of integers called nums, you can perform any of the following operation while nums contains at least 2 elements:

Choose the first two elements of nums and delete them.
Choose the last two elements of nums and delete them.
Choose the first and the last elements of nums and delete them.
The score of the operation is the sum of the deleted elements.

Your task is to find the maximum number of operations that can be performed, such that all operations have the same score.

Return the maximum number of operations possible that satisfy the condition mentioned above.

 

Example 1:

Input: nums = [3,2,1,2,3,4]
Output: 3
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [1,2,3,4].
- Delete the first and the last elements, with score 1 + 4 = 5, nums = [2,3].
- Delete the first and the last elements, with score 2 + 3 = 5, nums = [].
We are unable to perform any more operations as nums is empty.
Example 2:

Input: nums = [3,2,6,1,4]
Output: 2
Explanation: We perform the following operations:
- Delete the first two elements, with score 3 + 2 = 5, nums = [6,1,4].
- Delete the last two elements, with score 1 + 4 = 5, nums = [6].
It can be proven that we can perform at most 2 operations.
 

Example 3:

Input: nums = [1,9,7,3,2,7,4,12,2,6]
Output: 2

Constraints:

2 <= nums.length <= 2000
1 <= nums[i] <= 1000
''')

