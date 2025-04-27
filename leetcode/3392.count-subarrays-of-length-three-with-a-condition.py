from lc import *

# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/solutions/6251410/1-line/?envType=daily-question&envId=2025-04-27

class Solution:
    def countSubarrays(self, a: List[int]) -> int:
        return sum((a[i]+a[i+2])*2==a[i+1]for i in range(len(a)-2))

class Solution:
    def countSubarrays(self, a: List[int]) -> int:
        return sum(a[i+1]/2==a[i]+a[i+2]for i in range(len(a)-2))

# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/solutions/6171755/python3-3-lines-zip-and-count-t-s-92-93/?envType=daily-question&envId=2025-04-27

class Solution:
    def countSubarrays(self, a: List[int]) -> int:
        return sum(x+x+z+z==y for x,y,z in zip(a,a[1:],a[2:]))

# https://leetcode.com/problems/count-subarrays-of-length-three-with-a-condition/solutions/6676966/one-line-solution/?envType=daily-question&envId=2025-04-27

class Solution:
    def countSubarrays(self, a: List[int]) -> int:
        return sum(l+r==m/2 for l,m,r in zip(a,a[1:],a[2:]))

test('''
3392. Count Subarrays of Length Three With a Condition
Solved
Easy
Topics
Companies
Hint
Given an integer array nums, return the number of subarrays of length 3 such that the sum of the first and third numbers equals exactly half of the second number.

 

Example 1:

Input: nums = [1,2,1,4,1]

Output: 1

Explanation:

Only the subarray [1,4,1] contains exactly 3 elements where the sum of the first and third numbers equals half the middle number.

Example 2:

Input: nums = [1,1,1]

Output: 0

Explanation:

[1,1,1] is the only subarray of length 3. However, its first and third numbers do not add to half the middle number.

 

Constraints:

3 <= nums.length <= 100
-100 <= nums[i] <= 100
Seen this question in a real interview before?
1/5
Yes
No
Accepted
35.4K
Submissions
65.7K
Acceptance Rate
53.8%
Topics
Array
Companies
Hint 1
The constraints are small. Consider checking every subarray.
''')
