from lc import *

# https://leetcode.com/problems/target-sum/discuss/97439/JavaPython-Easily-Understood

class Solution:
    def findTargetSumWays(self, a: List[int], s: int) -> int:
        c=Counter({0:1})
        for x in a:
            t=Counter()
            for y in c:
                t[y+x] += c[y]
                t[y-x] += c[y]
            c = t
        return c[s]

# https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, a: List[int], s: int) -> int:
        return+(f:=cache(lambda i,x:f(i+1,x+a[i])+f(i+1,x-a[i])if a[i:]else x==s))(0,0)

test('''
494. Target Sum
Medium

11160

374

Add to List

Share
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.

 

Example 1:

Input: nums = [1,1,1,1,1], target = 3
Output: 5
Explanation: There are 5 ways to assign symbols to make the sum of nums be target 3.
-1 + 1 + 1 + 1 + 1 = 3
+1 - 1 + 1 + 1 + 1 = 3
+1 + 1 - 1 + 1 + 1 = 3
+1 + 1 + 1 - 1 + 1 = 3
+1 + 1 + 1 + 1 - 1 = 3
Example 2:

Input: nums = [1], target = 1
Output: 1
 

Constraints:

1 <= nums.length <= 20
0 <= nums[i] <= 1000
0 <= sum(nums[i]) <= 1000
-1000 <= target <= 1000
Accepted
705,478
Submissions
1,469,378
''')
