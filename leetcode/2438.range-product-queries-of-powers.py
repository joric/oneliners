from lc import *

# https://leetcode.com/problems/range-product-queries-of-powers/solutions/2706717/python3-super-concise-3-line-code/?envType=daily-question&envId=2025-08-11

class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:
        p=[*accumulate([0]+[i for i in range(32)if(1<<i)&n])];return[pow(2,p[j+1]-p[i],10**9+7) for i,j in q]

# https://leetcode.com/problems/range-product-queries-of-powers/description/?envType=daily-question&envId=2025-08-11

class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:
        p=[i for i,c in enumerate(bin(n)[:1:-1])if'0'<c];return[pow(2,sum(p[a:b+1]),10**9+7)for a,b in q]

# https://leetcode.com/problems/range-product-queries-of-powers/solutions/7051624/two-simple-lines-of-code/?envType=daily-question&envId=2025-08-11

class Solution:
    def productQueries(self, n: int, q: List[List[int]]) -> List[int]:
        p=[1<<i for i in range(31)if 1<<i&n];return [prod(p[a:b+1])%(10**9+7)for a,b in q]

test('''
2438. Range Product Queries of Powers
Medium
Topics
premium lock icon
Companies
Hint
Given a positive integer n, there exists a 0-indexed array called powers, composed of the minimum number of powers of 2 that sum to n. The array is sorted in non-decreasing order, and there is only one way to form the array.

You are also given a 0-indexed 2D integer array queries, where queries[i] = [lefti, righti]. Each queries[i] represents a query where you have to find the product of all powers[j] with lefti <= j <= righti.

Return an array answers, equal in length to queries, where answers[i] is the answer to the ith query. Since the answer to the ith query may be too large, each answers[i] should be returned modulo 109 + 7.

 

Example 1:

Input: n = 15, queries = [[0,1],[2,2],[0,3]]
Output: [2,4,64]
Explanation:
For n = 15, powers = [1,2,4,8]. It can be shown that powers cannot be a smaller size.
Answer to 1st query: powers[0] * powers[1] = 1 * 2 = 2.
Answer to 2nd query: powers[2] = 4.
Answer to 3rd query: powers[0] * powers[1] * powers[2] * powers[3] = 1 * 2 * 4 * 8 = 64.
Each answer modulo 109 + 7 yields the same answer, so [2,4,64] is returned.
Example 2:

Input: n = 2, queries = [[0,0]]
Output: [2]
Explanation:
For n = 2, powers = [2].
The answer to the only query is powers[0] = 2. The answer modulo 109 + 7 is the same, so [2] is returned.
 

Constraints:

1 <= n <= 109
1 <= queries.length <= 105
0 <= starti <= endi < powers.length
Seen this question in a real interview before?
1/5
Yes
No
Accepted
28,085/57.9K
Acceptance Rate
48.5%
Topics
Array
Bit Manipulation
Prefix Sum
Biweekly Contest 89
icon
Companies
Hint 1
The powers array can be created using the binary representation of n.
Hint 2
Once powers is formed, the products can be taken using brute force.
''')
