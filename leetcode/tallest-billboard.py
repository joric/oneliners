from lc import *

# https://leetcode.com/problems/tallest-billboard/discuss/2604071/Python.-LRU-cache.-2-liner...

class Solution:
    def tallestBillboard(self, x: List[int]) -> int:
        f=lru_cache(None)(lambda i,s: (0 if s==0 else -inf) if i==len(x)  else max(f(i+1,s),f(i+1,s-x[i]),f(i+1,s+x[i])+x[i]))
        return f(0,0)

class Solution:
    def tallestBillboard(self, r: List[int]) -> int:
        f=cache(lambda i,s:i<len(r)and max(f(i+1,s),f(i+1,s-r[i]),f(i+1,s+r[i])+r[i])or(s and-inf or 0));return f(0,0)

class Solution:
    def tallestBillboard(self, r: List[int]) -> int:
        f=cache(lambda i,s:i<len(r)and max((t:=r[i])+f(i+1,s+t),f(i+1,s-t),f(i+1,s))or(s and-inf or 0));return f(0,0)

class Solution:
    def tallestBillboard(self, r):
        f=cache(lambda i,s:r[i:]and max(f(i+1,s),f(i+1,s-r[i]),f(i+1,s+r[i])+r[i])or-9**9*(s!=0));return f(0,0)


test('''
956. Tallest Billboard
Hard

897

29

Add to List

Share
You are installing a billboard and want it to have the largest height. The billboard will have two steel supports, one on each side. Each steel support must be an equal height.

You are given a collection of rods that can be welded together. For example, if you have rods of lengths 1, 2, and 3, you can weld them together to make a support of length 6.

Return the largest possible height of your billboard installation. If you cannot support the billboard, return 0.

 

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
 

Constraints:

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000
''')


