from lc import *

# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/solutions/6568657/powers-of-4/?envType=daily-question&envId=2025-09-06

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        res = 0
        for l, r in queries:
            total = 0
            p = 0
            for i in range(r.bit_length() // 2 + 2):
                p4 = 4 ** i
                if p4 > r:
                    break
                pl = max(l, p4)
                pr = min(r, p4 * 4 - 1)
                if pl <= pr:
                    p += 1
                    total += p * (pr - pl + 1)
            res += (total + 1) // 2
        return res

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        return sum((sum(((i+1)*(min(r,4**(i+1)-1)-max(l,4**i)+1)) for i in range(r.bit_length()//2+2) if max(l,4**i)<=min(r,4**(i+1)-1))+1)//2 for l,r in q)

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        return sum(-~sum(t*-~i for i in range(16)if(t:=min(r,4**-~i-1)-max(l,4**i)+1)>0)//2 for l,r in q)

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        return sum(-~sum(t*-~i for i in range(16)if(t:=min(r+1,4**-~i)-max(l,4**i))>0)//2 for l,r in q)

# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/solutions/6570962/math/

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        f=lambda a:a>0 and sum(a-4**i+1 for i in range(int(log(a,4))+1));return sum((1+f(r)-f(l-1))//2 for l,r in q)

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        f=lambda a:sum(max(0,a-4**i)for i in range(16));return sum((1+f(r+1)-f(l))//2 for l,r in q)

# https://leetcode.com/problems/minimum-operations-to-make-array-elements-zero/solutions/7161144/1-line-by-joric-dxtd/

class Solution:
    def minOperations(self, q: List[List[int]]) -> int:
        f=lambda x:sum(max(0,x-4**i)for i in range(16));return sum(f(b+1)-f(a)+1>>1 for a,b in q)

test('''
3495. Minimum Operations to Make Array Elements Zero
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given a 2D array queries, where queries[i] is of the form [l, r]. Each queries[i] defines an array of integers nums consisting of elements ranging from l to r, both inclusive.

In one operation, you can:

Select two integers a and b from the array.
Replace them with floor(a / 4) and floor(b / 4).
Your task is to determine the minimum number of operations required to reduce all elements of the array to zero for each query. Return the sum of the results for all queries.

 

Example 1:

Input: queries = [[1,2],[2,4]]

Output: 3

Explanation:

For queries[0]:

The initial array is nums = [1, 2].
In the first operation, select nums[0] and nums[1]. The array becomes [0, 0].
The minimum number of operations required is 1.
For queries[1]:

The initial array is nums = [2, 3, 4].
In the first operation, select nums[0] and nums[2]. The array becomes [0, 3, 1].
In the second operation, select nums[1] and nums[2]. The array becomes [0, 0, 0].
The minimum number of operations required is 2.
The output is 1 + 2 = 3.

Example 2:

Input: queries = [[2,6]]

Output: 4

Explanation:

For queries[0]:

The initial array is nums = [2, 3, 4, 5, 6].
In the first operation, select nums[0] and nums[3]. The array becomes [0, 3, 4, 1, 6].
In the second operation, select nums[2] and nums[4]. The array becomes [0, 3, 1, 1, 1].
In the third operation, select nums[1] and nums[2]. The array becomes [0, 0, 0, 1, 1].
In the fourth operation, select nums[3] and nums[4]. The array becomes [0, 0, 0, 0, 0].
The minimum number of operations required is 4.
The output is 4.

Other examples:

Input: queries = [[1,8]]
Output: 7

Constraints:

1 <= queries.length <= 105
queries[i].length == 2
queries[i] == [l, r]
1 <= l < r <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
6,645/19.6K
Acceptance Rate
33.8%
Topics
Array
Math
Bit Manipulation
Weekly Contest 442
icon
Companies
Hint 1
For a number x, the number of "/4" operations to change it to 0 is floor(log4(x)) + 1.
Hint 2
Always pair the 2 numbers with the maximum "/4" operations needed.
''')
