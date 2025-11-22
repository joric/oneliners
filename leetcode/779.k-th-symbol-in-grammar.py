from lc import *

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return~~(n!=1)and(self.kthGrammar(n-1,k)if k<=(p:=1<<n-2)else 1-self.kthGrammar(n-1,k-p))

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return(f:=lambda n,k:n-1and(1-f(n-1,k-p)if k>(p:=1<<n-2)else f(n-1,k)))(n,k)

# https://leetcode.com/problems/k-th-symbol-in-grammar/discuss/405670/C%2B%2B-and-x86-assembler-solutions-with-explanation

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return bin(k-1).count('1')&1;

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return int.bit_count(k-1)&1

# cpp is shorter here (also maybe equal_range problems could be shorter because python doesn't have it)
# return popcount(k-1u)&1;

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        return(k-1).bit_count()&1

test('''
779. K-th Symbol in Grammar
Medium

2771

306

Add to List

Share
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

 

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0
Example 2:

Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01
Example 3:

Input: n = 2, k = 2
Output: 1
Explanation: 
row 1: 0
row 2: 01

Example 4:
Input: n = 3, k = 2
Output: 1

Example 4:
Input: n = 3, k = 4
Output: 0

Constraints:

1 <= n <= 30
1 <= k <= 2^(n - 1)
''')