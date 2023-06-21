from lc import *

# https://leetcode.com/problems/minimum-cost-to-make-array-equal/discuss/3597733/7-line-code-with-97.83-in-Speed

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        a = sorted(zip(nums, cost))
        m = sum(cost)/2
        c = 0
        for t,x in a:
            c += x
            if c >= m:
                return sum(abs(t-n)*c for n,c in a)

class Solution:
    def minCost(self, v: List[int], p: List[int]) -> int:
        a,m,c=sorted(zip(v,p)),sum(p)/2,0;return next(sum(abs(t-n)*c for n,c in a)for t,x in a if(c:=c+x)>=m)

class Solution:
    def minCost(self, v, p):
        a,c=sorted(zip(v,p)),-sum(p);return next(sum(abs(t-n)*c for n,c in a)for t,x in a if(c:=c+2*x)>0)

test('''
2448. Minimum Cost to Make Array Equal
Hard

647

11

Add to List

Share
You are given two 0-indexed arrays nums and cost consisting each of n positive integers.

You can do the following operation any number of times:

Increase or decrease any element of the array nums by 1.
The cost of doing one operation on the ith element is cost[i].

Return the minimum total cost such that all the elements of the array nums become equal.

 

Example 1:

Input: nums = [1,3,5,2], cost = [2,3,1,14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8.
It can be shown that we cannot make the array equal with a smaller cost.
Example 2:

Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
Output: 0
Explanation: All the elements are already equal, so no operations are needed.
 

Constraints:

n == nums.length == cost.length
1 <= n <= 10^5
1 <= nums[i], cost[i] <= 10^6
Accepted
13,321
Submissions
37,553
Seen this question in a real interview before?

Yes

No
Changing the elements into one of the numbers already existing in the array nums is optimal.
Try finding the cost of changing the array into each element, and return the minimum value.
''')
