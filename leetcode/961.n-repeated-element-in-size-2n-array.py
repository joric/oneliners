from lc import *

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/327929/2-line-python-40ms-beat-96-by-a_star-z9w9/?envType=daily-question&envId=2026-01-02

class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        return next(a[i]for i in range(len(a))if a[i]in a[i+1:])

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/970751/python3-one-line-by-smellhead-riwo/?envType=daily-question&envId=2026-01-02

class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        return[i for i,j in Counter(a).items()if j==len(a)/2][0]

class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        c=Counter(a);return[k for k in c if c[k]==len(a)/2][0]

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/1562650/python3-one-line-solution-by-sirenescx-6kru/?envType=daily-question&envId=2026-01-02

class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        return(sum(a)-sum({*a}))//(len(a)//2-1)

# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/solutions/2821341/simple-one-line-python3-by-jlonerawesome-oh1q/?envType=daily-question&envId=2026-01-02

class Solution:
    def repeatedNTimes(self, a: List[int]) -> int:
        return Counter(a).most_common(1)[0][0]

test('''
961. N-Repeated Element in Size 2N Array
Solved
Easy
Topics
premium lock icon
Companies
You are given an integer array nums with the following properties:

nums.length == 2 * n.
nums contains n + 1 unique elements.
Exactly one element of nums is repeated n times.
Return the element that is repeated n times.

 

Example 1:

Input: nums = [1,2,3,3]
Output: 3
Example 2:

Input: nums = [2,1,2,5,3,2]
Output: 2
Example 3:

Input: nums = [5,1,5,2,5,3,5,4]
Output: 5
 

Constraints:

2 <= n <= 5000
nums.length == 2 * n
0 <= nums[i] <= 104
nums contains n + 1 unique elements and one of them is repeated exactly n times.
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
278,242/357.4K
Acceptance Rate
77.9%
Topics
Array
Hash Table
Weekly Contest 116
''')
