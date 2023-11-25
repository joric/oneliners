from lc import *

class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        sub = 0
        sum = 0
        res = []
        for i in range(n-1, -1,-1):
            sum += nums[i]
        for i in range(n):
            sum -= nums[i]
            res.append(sub+ (i * nums[i])- ((n - i - 1)* nums[i])+ sum)
            sum -= nums[i]
        return res

# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/discuss/2135231/Python3-2-Lines

class Solution:
    def getSumAbsoluteDifferences(self, n: List[int]) -> List[int]:
        a=[0,*accumulate(n)];return[a[-1]-2*a[i]-x*len(n)+2*x*i for i,x in enumerate(n)]

# https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/discuss/1240128/Python-3-one-line-blazing-fast

class Solution:
    def getSumAbsoluteDifferences(self, n: List[int]) -> List[int]:
        r = sum(n)
        for i,d in enumerate(map(sub,n,chain([0],n))):
            r += d * (2*i-len(n))
            yield r

class Solution:
    def getSumAbsoluteDifferences(self, n: List[int]) -> List[int]:
        return islice(accumulate(map(mul,map(sub,n,chain([0],n)),count(-len(n),2)),initial=sum(n)),1,None)

class Solution:
    def getSumAbsoluteDifferences(self, n: List[int]) -> List[int]:
        r=sum(n);return[r:=r+d*(2*i-len(n))for i,d in enumerate(map(sub,n,[0]+n))]

test('''
1685. Sum of Absolute Differences in a Sorted Array
Medium

1361

40

Add to List

Share
You are given an integer array nums sorted in non-decreasing order.

Build and return an integer array result with the same length as nums such that result[i] is equal to the summation of absolute differences between nums[i] and all the other elements in the array.

In other words, result[i] is equal to sum(|nums[i]-nums[j]|) where 0 <= j < nums.length and j != i (0-indexed).

 

Example 1:

Input: nums = [2,3,5]
Output: [4,3,5]
Explanation: Assuming the arrays are 0-indexed, then
result[0] = |2-2| + |2-3| + |2-5| = 0 + 1 + 3 = 4,
result[1] = |3-2| + |3-3| + |3-5| = 1 + 0 + 2 = 3,
result[2] = |5-2| + |5-3| + |5-5| = 3 + 2 + 0 = 5.
Example 2:

Input: nums = [1,4,6,8,10]
Output: [24,15,13,15,21]
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= nums[i + 1] <= 10^4
Accepted
47,520
Submissions
71,700
Seen this question in a real interview before?

Yes

No
Absolute difference is the same as max(a, b) - min(a, b). How can you use this fact with the fact that the array is sorted?
For nums[i], the answer is (nums[i] - nums[0]) + (nums[i] - nums[1]) + ... + (nums[i] - nums[i-1]) + (nums[i+1] - nums[i]) + (nums[i+2] - nums[i]) + ... + (nums[n-1] - nums[i]).
It can be simplified to (nums[i] * i - (nums[0] + nums[1] + ... + nums[i-1])) + ((nums[i+1] + nums[i+2] + ... + nums[n-1]) - nums[i] * (n-i-1)). One can build prefix and suffix sums to compute this quickly.
''')

