from lc import *

# https://leetcode.com/problems/rearranging-fruits/solutions/3143917/java-c-python-two-ways-to-swap/

class Solution:
    def minCost(self, A: List[int], B: List[int]) -> int:
        count = Counter(A + B)
        for c in count:
            if count[c] % 2:
                return -1
            count[c] >>= 1
        A2 = list((Counter(A) - count).elements())
        B2 = list((Counter(B) - count).elements())
        small = min(count)
        C = sorted(A2 + B2)
        return sum(min(small * 2, C[i]) for i in range(len(A2)))

# https://leetcode.com/problems/rearranging-fruits/solutions/4554864/python-8-lines-counter-magic/

class Solution:
    def minCost(self, a: List[int], b: List[int]) -> int:
        c = Counter(a)
        c.subtract(b)
        if any(i&1 for i in c.values()):
            return -1
        m = min(c)
        e = sorted((+c+-c).elements())
        return sum(min(i,2*m)for i in e[:len(e)//2:2])

class Solution:
    def minCost(self, a: List[int], b: List[int]) -> int:
        c=Counter(a);c.subtract(b);m,e=min(c),sorted((+c+-c).elements());return(sum(min(i,2*m)for i in e[:len(e)//2:2]),-1)[any(1&c[i]for i in c)]

test('''
2561. Rearranging Fruits
Hard
Topics
premium lock icon
Companies
Hint
You have two fruit baskets containing n fruits each. You are given two 0-indexed integer arrays basket1 and basket2 representing the cost of fruit in each basket. You want to make both baskets equal. To do so, you can use the following operation as many times as you want:

Chose two indices i and j, and swap the ith fruit of basket1 with the jth fruit of basket2.
The cost of the swap is min(basket1[i],basket2[j]).
Two baskets are considered equal if sorting them according to the fruit cost makes them exactly the same baskets.

Return the minimum cost to make both the baskets equal or -1 if impossible.

 

Example 1:

Input: basket1 = [4,2,2,2], basket2 = [1,4,1,2]
Output: 1
Explanation: Swap index 1 of basket1 with index 0 of basket2, which has cost 1. Now basket1 = [4,1,2,2] and basket2 = [2,4,1,2]. Rearranging both the arrays makes them equal.
Example 2:

Input: basket1 = [2,3,4,1], basket2 = [3,2,5,1]
Output: -1
Explanation: It can be shown that it is impossible to make both the baskets equal.

Other examples:

Input: basket1 = [4,4,4,4,3], basket2 = [5,5,5,5,3]
Output: 8

Constraints:

basket1.length == basket2.length
1 <= basket1.length <= 105
1 <= basket1[i],basket2[i] <= 109
Seen this question in a real interview before?
1/5
Yes
No
Accepted
12,559/35.2K
Acceptance Rate
35.7%
Topics
Array
Hash Table
Greedy
Sort
Weekly Contest 331
icon
Companies
Hint 1
Create two frequency maps for both arrays, and find the minimum element among all elements of both arrays.
Hint 2
Check if the sum of frequencies of an element in both arrays is odd, if so return -1
Hint 3
Store the elements that need to be swapped in a vector, and sort it.
Hint 4
Can we reduce swapping cost with the help of minimum element?
Hint 5
Calculate the minimum cost of swapping.
Similar Questions
The Latest Time to Catch a Bus
Medium
Minimum Number of Operations to Make Arrays Similar
Hard
''')
