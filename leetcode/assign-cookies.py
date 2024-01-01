from lc import *

# https://leetcode.com/problems/assign-cookies/discuss/93995/Python-fast-one-liner

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort();return len([s.pop()for x in sorted(g)[::-1]if s and s[-1]>=x])

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        s.sort();return sum(0<s.pop()for x in sorted(g)[::-1]if s and s[-1]>=x)

test('''
455. Assign Cookies
Easy

2789

257

Add to List

Share
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

 

Example 1:

Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you could only make the child whose greed factor is 1 content.
You need to output 1.
Example 2:

Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are big enough to gratify all of the children, 
You need to output 2.


Example 3:

Input: g = [1,2,3], s = []
Output: 0

Example 4:

Input: g= [10,9,8,7], s = [5,6,7,8]
Output: 2

Constraints:

1 <= g.length <= 3 * 10^4
0 <= s.length <= 3 * 10^4
1 <= g[i], s[j] <= 2^31 - 1
Accepted
268,260
Submissions
539,707
''')

