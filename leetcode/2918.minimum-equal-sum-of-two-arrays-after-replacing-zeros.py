from lc import *

# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/solutions/4223178/python-easy-and-simple-one-liner/?envType=daily-question&envId=2025-05-10

class Solution:
    def minSum(self, a: List[int], b: List[int]) -> int:
        return -1 if (((sum(a)+a.count(0)>sum(b)+b.count(0))and not b.count(0))or((sum(a)+a.count(0)<sum(b)+b.count(0))and not a.count(0))) else max(sum(a)+a.count(0),sum(b)+b.count(0))

# https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/solutions/4220828/java-c-python-easy-and-concise/?envType=daily-question&envId=2025-05-10

class Solution:
    def minSum(self, A: List[int], B: List[int]) -> int:
        sa = sum(max(a, 1) for a in A)
        sb = sum(max(b, 1) for b in B)
        if sa < sb and A.count(0) == 0: return -1
        if sa > sb and B.count(0) == 0: return -1
        return max(sa, sb)

class Solution:
    def minSum(self, a: List[int], b: List[int]) -> int:
        p,q=(sum(x or 1 for x in t)for t in(a,b));return(max(p,q),-1)[p<q and a.count(0)==0 or p>q and b.count(0)==0]

class Solution:
    def minSum(self, a: List[int], b: List[int]) -> int:
        p,q=(sum(x or 1 for x in t)for t in(a,b));return(max(p,q),-1)[(p<q)*all(a)+(p>q)*all(b)]

test('''
2918. Minimum Equal Sum of Two Arrays After Replacing Zeros
Medium
Topics
Companies
Hint
You are given two arrays nums1 and nums2 consisting of positive integers.

You have to replace all the 0's in both arrays with strictly positive integers such that the sum of elements of both arrays becomes equal.

Return the minimum equal sum you can obtain, or -1 if it is impossible.

 

Example 1:

Input: nums1 = [3,2,0,1,0], nums2 = [6,5,0]
Output: 12
Explanation: We can replace 0's in the following way:
- Replace the two 0's in nums1 with the values 2 and 4. The resulting array is nums1 = [3,2,2,1,4].
- Replace the 0 in nums2 with the value 1. The resulting array is nums2 = [6,5,1].
Both arrays have an equal sum of 12. It can be shown that it is the minimum sum we can obtain.
Example 2:

Input: nums1 = [2,0,2,0], nums2 = [1,4]
Output: -1
Explanation: It is impossible to make the sum of both arrays equal.
 

Constraints:

1 <= nums1.length, nums2.length <= 105
0 <= nums1[i], nums2[i] <= 106
Seen this question in a real interview before?
1/5
Yes
No
Accepted
32.9K
Submissions
90.2K
Acceptance Rate
36.4%
Topics
Array
Greedy
Companies
Hint 1
Consider we replace all the 0’s with 1’s on both arrays, the answer will be -1 if there was no 0 in the array with the smaller sum of elements.
Hint 2
Otherwise, how can you update the value of exactly one of these 1’s to make the sum of the two arrays equal?
''')
