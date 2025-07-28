from lc import *

# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/discuss/1525309/JavaC%2B%2BPython-DP-solution

class Solution:
    def countMaxOrSubsets(self, n: List[int]) -> int:
        c = Counter([0])
        for a in n:
            for k,v in deepcopy(c).items():
                c[k|a] += v
        return c[max(c)]

class Solution:
    def countMaxOrSubsets(self, n: List[int]) -> int:
        c=Counter([0]);[c.update({k|a:v})for a in n for k,v in deepcopy(c).items()];return c[max(c)]

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        c=Counter([0]);[c.update({k|x:v})for x in a for k,v in[*c.items()]];return c[max(c)]

# https://leetcode.com/problems/count-number-of-maximum-bitwise-or-subsets/solutions/5930848/One-Line-Solution/

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        return sum(reduce(or_,(v for i,v in enumerate(a) if 1<<i&m))==reduce(or_,a) for m in range(1,1<<len(a)))

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        return sum(reduce(or_,q)==reduce(or_,a)for k in range(len(a)) for q in combinations(a,k+1))

# updated 2024-10-18 (POTD)

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        return(f:=lambda i,o,x=reduce(or_,a):a[i:]and f(i+1,o)+f(i+1,o|a[i])or o==x)(0,0)

# updated 2025-07-28 (POTD)

class Solution:
    def countMaxOrSubsets(self, a: List[int]) -> int:
        return(f:=lambda i,o:a[i:]and f(i+1,o)+f(i+1,o|a[i])or o==reduce(or_,a))(0,0)

test('''
2044. Count Number of Maximum Bitwise-OR Subsets
Medium

637

22

Add to List

Share
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the number of different non-empty subsets with the maximum bitwise OR.

An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b. Two subsets are considered different if the indices of the elements chosen are different.

The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

 

Example 1:

Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]
Example 2:

Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.
Example 3:

Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
 

Constraints:

1 <= nums.length <= 16
1 <= nums[i] <= 105
Accepted
31,444
Submissions
40,150
''')
