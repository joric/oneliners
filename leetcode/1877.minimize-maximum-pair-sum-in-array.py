from lc import *

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/discuss/2452681/Python-or-Full-explanation-and-2-solutions-with-a-linear-and-O(nlogn)-time-complexities

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        m = max(nums)
        a = [0]*(m+1)
        for i in nums:
            a[i] += 1
        r,i,j = 0, 0, m
        while i <= j:
            if a[i]==0:
                i += 1
            elif a[j]==0:
                j -= 1
            else:
                r = max(i+j, r)
                a[i] -= 1
                a[j] -= 1
        return r

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/discuss/4296645/Python-one-line

class Solution:
    def minPairSum(self, a: List[int]) -> int:
        a.sort();return max(a[i]+a[~i]for i in range(len(a)//2))

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/discuss/1238655/JavaC%2B%2BPython-min-%2B-max

class Solution:
    def minPairSum(self, a: List[int]) -> int:
        return max(x+y for x,y in zip(sorted(a),sorted(a)[::-1]))

class Solution:
    def minPairSum(self, a: List[int]) -> int:
        return max(map(sum,zip(t:=sorted(a),t[::-1])))

class Solution:
    def minPairSum(self, a: List[int]) -> int:
        a.sort();return max(map(sum,zip(a,a[::-1])))

# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/solutions/4298396/one-line-solution-by-mikposp-uq2g/

class Solution:
    def minPairSum(self, a: List[int]) -> int:
        a.sort();return max(map(add,a,a[::-1]))

test('''
1877. Minimize Maximum Pair Sum in Array
Medium

1517

339

Add to List

Share
The pair sum of a pair (a,b) is equal to a + b. The maximum pair sum is the largest pair sum in a list of pairs.

For example, if we have pairs (1,5), (2,3), and (4,4), the maximum pair sum would be max(1+5, 2+3, 4+4) = max(6, 5, 8) = 8.
Given an array nums of even length n, pair up the elements of nums into n / 2 pairs such that:

Each element of nums is in exactly one pair, and
The maximum pair sum is minimized.
Return the minimized maximum pair sum after optimally pairing up the elements.

 

Example 1:

Input: nums = [3,5,2,3]
Output: 7
Explanation: The elements can be paired up into pairs (3,3) and (5,2).
The maximum pair sum is max(3+3, 5+2) = max(6, 7) = 7.
Example 2:

Input: nums = [3,5,4,2,4,6]
Output: 8
Explanation: The elements can be paired up into pairs (3,5), (4,4), and (6,2).
The maximum pair sum is max(3+5, 4+4, 6+2) = max(8, 8, 8) = 8.
 

Constraints:

n == nums.length
2 <= n <= 10^5
n is even.
1 <= nums[i] <= 10^5
Accepted
112,678
Submissions
138,851
''')
