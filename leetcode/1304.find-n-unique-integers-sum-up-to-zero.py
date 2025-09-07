from lc import *

# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/solutions/464344/trivial-python-ruby-java-c/?envType=daily-question&envId=2025-09-07

class Solution:
    def sumZero(self, n: int) -> List[int]:
        a=range(1,n);return[*a,-sum(a)]

test('''
1304. Find N Unique Integers Sum up to Zero
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an integer n, return any array containing n unique integers such that they add up to 0.

 

Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
 

Constraints:

1 <= n <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
258,779/338.6K
Acceptance Rate
76.4%
Topics
Array
Math
Weekly Contest 169
icon
Companies
Hint 1
Return an array where the values are symmetric. (+x , -x).
Hint 2
If n is odd, append value 0 in your returned array.
''', check=lambda res,expected,param: len(res)==len({*res}) and sum(res)==0 )
