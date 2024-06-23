from lc import *

# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/1659537/Python-two-liner-%3A)

class Solution:
    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        c=Counter(accumulate(i%2 for i in a));return sum(y*(c[x-k]+(x-k==0))for x,y in c.items())

# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/625894/Python-2-lines.

class Solution:
    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        c=Counter([0,*accumulate(x%2 for x in a)]);return sum(c[t]*c[t-k]for t in c)

# https://leetcode.com/problems/count-number-of-nice-subarrays/discuss/5351230/one-line-solution

class Solution:
    def numberOfSubarrays(self, a: List[int], k: int) -> int:
        c=Counter([q:=0]);return sum(c.update([q:=q+v%2])or c[q-k]for v in a)

test('''
1248. Count Number of Nice Subarrays
Medium

4032

88

Add to List

Share
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

Return the number of nice sub-arrays.

 

Example 1:

Input: nums = [1,1,2,1,1], k = 3
Output: 2
Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
Example 2:

Input: nums = [2,4,6], k = 1
Output: 0
Explanation: There are no odd numbers in the array.
Example 3:

Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
Output: 16
 

Constraints:

1 <= nums.length <= 50000
1 <= nums[i] <= 10^5
1 <= k <= nums.length
Accepted
163,877
Submissions
241,643
''')
