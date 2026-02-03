from lc import *

# https://leetcode.com/problems/trionic-array-i/solutions/7046283/ruby-one-liner-by-dnnx-v5h2/

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return[*map(itemgetter(0),groupby(map(lambda p:(gt(*p))-(lt(*p)),zip(a,a[1:]))))]==[-1,1,-1]

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return[k for k,_ in groupby((x>y)-(x<y)for x,y in zip(a,a[1:]))]==[-1,1,-1]

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return[k for k,_ in groupby((x>y)-(x<y)for x,y in pairwise(a))]==[-1,1,-1]

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return(-1,1,-1)==next(zip(*groupby(pairwise(a),lambda p:gt(*p)-lt(*p))))

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return(-1,1,-1)==next(zip(*groupby((x>y)-(x<y)for x,y in pairwise(a))))

# https://leetcode.com/problems/trionic-array-i/solutions/7546990/one-line-solution-by-mikposp-6u7o/

class Solution:
    def isTrionic(self, a: List[int]) -> bool:
        return(1,-1,1)==next(zip(*groupby((x<y)-(x>y)for x,y in pairwise(a))))

test('''
3637. Trionic Array I
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums of length n.

An array is trionic if there exist indices 0 < p < q < n − 1 such that:

nums[0...p] is strictly increasing,
nums[p...q] is strictly decreasing,
nums[q...n − 1] is strictly increasing.
Return true if nums is trionic, otherwise return false.

 

Example 1:

Input: nums = [1,3,5,4,2,6]

Output: true

Explanation:

Pick p = 2, q = 4:

nums[0...2] = [1, 3, 5] is strictly increasing (1 < 3 < 5).
nums[2...4] = [5, 4, 2] is strictly decreasing (5 > 4 > 2).
nums[4...5] = [2, 6] is strictly increasing (2 < 6).
Example 2:

Input: nums = [2,1,3]

Output: false

Explanation:

There is no way to pick p and q to form the required three segments.

Other examples:

Input: nums = [2,4,3,3]
Output: false

Input: nums = [1,6,6,3,7]
Output: false

Constraints:

3 <= n <= 100
-1000 <= nums[i] <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
64,130/134.1K
Acceptance Rate
47.8%
Topics
Array
Weekly Contest 461
icon
Companies
Hint 1
Use brute force
''')
