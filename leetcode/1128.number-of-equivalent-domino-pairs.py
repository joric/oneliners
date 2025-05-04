from lc import *

# https://leetcode.com/problems/number-of-equivalent-domino-pairs/solutions/6696555/one-line-solution/?envType=daily-question&envId=2025-05-04

class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum(f*(f-1)//2 for f in Counter(map(tuple,map(sorted,a))).values())

class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum(f*(f-1)//2 for f in Counter(min(p)*10+max(p) for p in a).values())

class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum((f:=len([*g]))*(f-1)//2 for _,g in groupby(sorted(map(sorted,a))))

class Solution:
    def numEquivDominoPairs(self, a: List[List[int]]) -> int:
        return sum(comb(x,2)for x in Counter(map(tuple,map(sorted,a))).values())

test('''
1128. Number of Equivalent Domino Pairs
Solved
Easy
Topics
Companies
Hint
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

 

Example 1:

Input: dominoes = [[1,2],[2,1],[3,4],[5,6]]
Output: 1
Example 2:

Input: dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
Output: 3
 

Constraints:

1 <= dominoes.length <= 4 * 104
dominoes[i].length == 2
1 <= dominoes[i][j] <= 9
Seen this question in a real interview before?
1/5
Yes
No
Accepted
103.4K
Submissions
193.5K
Acceptance Rate
53.5%
Topics
Array
Hash Table
Counting
Companies
Hint 1
For each domino j, find the number of dominoes you've already seen (dominoes i with i < j) that are equivalent.
Hint 2
You can keep track of what you've seen using a hashmap.
''')
