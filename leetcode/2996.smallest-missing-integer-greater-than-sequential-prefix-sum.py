from lc import *

#  https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/solutions/5940988/easy-one-by-deepash780-lyko/?envType=daily-question&envId=2026-08-11

class Solution:
    def missingInteger(self, a: List[int]) -> int:
        b=a[0]
        for i in range(1,len(a)):
            if a[i]-a[i-1]==1:
                b+=a[i]
            else:
                break
        while b in a:
            b+=1
        return b

# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/solutions/8324853/python-one-line-by-l1ne-3deh/?envType=daily-question&envId=2026-08-11

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        diffs = starmap(sub, pairwise(nums))
        streak = takewhile((-1).__eq__, diffs)
        size = 1 - sum(streak)
        best = sum(nums[:size])
        set_of_nums = set(nums)
        return next(filterfalse(set_of_nums.__contains__, count(best)))

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        return next(filterfalse(set(nums).__contains__, count(sum(nums[:1-sum(takewhile((-1).__eq__, starmap(sub, pairwise(nums))))]))))

class Solution:
    def missingInteger(self, a: List[int]) -> int:
        return next(filterfalse({*a}.__contains__,count(sum(a[:1-sum(takewhile((-1).__eq__,starmap(sub,pairwise(a))))]))))

class Solution:
    def missingInteger(self,a:List[int])->int:
        return next(x for x in count(sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]))if x not in a)

class Solution:
    def missingInteger(self,a:List[int])->int:
        return next(x for x in count(sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]))if{x}-{*a})

class Solution:
    def missingInteger(self,a:List[int])->int:
        return next(filterfalse(a.count,count(sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]))))

class Solution:
    def missingInteger(self,a:List[int])->int:
        return next(x for x in count(sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]))if{x}-{*a})

class Solution:
    def missingInteger(self,a:List[int])->int:
        return reduce(lambda s,_:s+(s in a),a,sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]))

class Solution:
    def missingInteger(self, a: List[int]) -> int:
        s=sum(a[:sum(takewhile(int,map(eq,a,count(a[0]))))]);[s:=s+(s in a)for _ in a];return s



test('''
2996. Smallest Missing Integer Greater Than Sequential Prefix Sum
Solved
Easy
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of integers nums.

A prefix nums[0..i] is sequential if, for all 1 <= j <= i, nums[j] = nums[j - 1] + 1. In particular, the prefix consisting only of nums[0] is sequential.

Return the smallest integer x missing from nums such that x is greater than or equal to the sum of the longest sequential prefix.

 

Example 1:

Input: nums = [1,2,3,2,5]
Output: 6
Explanation: The longest sequential prefix of nums is [1,2,3] with a sum of 6. 6 is not in the array, therefore 6 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
Example 2:

Input: nums = [3,4,5,1,12,14,13]
Output: 15
Explanation: The longest sequential prefix of nums is [3,4,5] with a sum of 12. 12, 13, and 14 belong to the array while 15 does not. Therefore 15 is the smallest missing integer greater than or equal to the sum of the longest sequential prefix.
 

Constraints:

1 <= nums.length <= 50
1 <= nums[i] <= 50
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
54,328/151.4K
Acceptance Rate
35.9%
Topics
Mid Level
Array
Hash Table
Sorting
Biweekly Contest 121
icon
Companies
Hint 1
To find the longest sequential prefix, iterate from left to right. For a fixed i, if nums[i] != nums[i - 1] + 1 then the longest sequential prefix ends at i - 1.
Similar Questions
Longest Common Prefix
Easy
First Missing Positive
Hard
Next Greater Element I
Easy
''')
