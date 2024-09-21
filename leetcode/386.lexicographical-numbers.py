from lc import *

# Q1. https://leetcode.com/contest/warm-up-contest/
# https://leetcode.com/problems/lexicographical-numbers/

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return map(int,sorted(map(str,range(1,n+1))))

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        return sorted(range(1,n+1),key=str)

test('''
386. Lexicographical Numbers
Medium

1936

142

Add to List

Share
Given an integer n, return all the numbers in the range [1, n] sorted in lexicographical order.

You must write an algorithm that runs in O(n) time and uses O(1) extra space. 

 

Example 1:

Input: n = 13
Output: [1,10,11,12,13,2,3,4,5,6,7,8,9]
Example 2:

Input: n = 2
Output: [1,2]
 

Constraints:

1 <= n <= 5 * 104
Accepted
120,409
Submissions
188,662
''')