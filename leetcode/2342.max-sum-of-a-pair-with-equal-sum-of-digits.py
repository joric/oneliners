from lc import *

# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solutions/2321429/scala-one-line-solution-faster-than-100-00-less-than-100-00/?envType=daily-question&envId=2025-02-12

'''
  def maximumSum(nums: Array[Int]): Int =
    scala.util.Try(nums.map(i => i.toString.map(n => n - '0').sum).zip(nums)
      .groupBy(_._1).mapValues(_.toSeq).values.filter(_.size >= 2)
      .map(n => n.map(_._2).sortBy(-_).take(2).sum).max).getOrElse(-1)
'''

class Solution:
    def maximumSum(self, a: List[int]) -> int:
        d=defaultdict(list);[d[sum(map(int,str(x)))].append(x)for x in a];return max((-1,sum(sorted(g)[-2:]))[len(g)>1]for g in d.values())

# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/solutions/6410166/simple-solution-6-lines-o-n/?envType=daily-question&envId=2025-02-12

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        ans, dic = -1, defaultdict(lambda : -inf)
        for num in nums:
            sum_digit = sum(map(int, str(num)))
            ans = max(dic[sum_digit] + num, ans)
            dic[sum_digit] = max(num, dic[sum_digit])
        return ans

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        return (d:=defaultdict(lambda:-inf)) or reduce(lambda a,n:(max(a,d[s:=sum(map(int,str(n)))]+n),setitem(d,s,max(n,d[s])))[0],nums,-1)

class Solution:
    def maximumSum(self, a: List[int]) -> int:
        d={};return max(setitem(d,s:=sum(map(int,str(x))),max(x,t:=d.get(s,-inf)))or max(-1,x+t)for x in a)

class Solution:
    def maximumSum(self, a: List[int]) -> int:
        d={};return max(setitem(d,s:=sum(map(int,str(x))),max(x,t:=d.get(s,0)))or(-1,x+t)[t>0]for x in a)

test('''
2342. Max Sum of a Pair With Equal Sum of Digits
Medium
Topics
Companies
Hint
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions.

 

Example 1:

Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.
Example 2:

Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
88.1K
Submissions
144.4K
Acceptance Rate
61.0%
Topics
Array
Hash Table
Sorting
Heap (Priority Queue)
Companies
Hint 1
What is the largest possible sum of digits a number can have?
Hint 2
Group the array elements by the sum of their digits, and find the largest two elements of each group.
''')
