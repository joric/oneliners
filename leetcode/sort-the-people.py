from lc import *

# https://leetcode.com/problems/sort-the-people/discuss/2621126/python-sort-1-liner

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        return [names[i] for i in sorted(range(len(names)), key=lambda i: heights[i], reverse=True)]

# https://leetcode.com/problems/sort-the-people

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        return map(itemgetter(1),sorted(zip(h,n))[::-1])

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        return[x[1]for x in sorted(zip(h,n))[::-1]]

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        return[x for _,x in sorted(zip(h,n))[::-1]]

class Solution:
    def sortPeople(self, n: List[str], h: List[int], f=itemgetter(1)) -> List[str]:
        return map(f,sorted(zip(h,n))[::-1])

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        return[*zip(*sorted(zip(h,n))[::-1])][1]

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        return[*zip(*sorted(zip(h,n)))][1][::-1]

test('''
2418. Sort the People
Easy

1477

26

Add to List

Share
You are given an array of strings names, and an array heights that consists of distinct positive integers. Both arrays are of length n.

For each index i, names[i] and heights[i] denote the name and height of the ith person.

Return names sorted in descending order by the people's heights.

 

Example 1:

Input: names = ["Mary","John","Emma"], heights = [180,165,170]
Output: ["Mary","Emma","John"]
Explanation: Mary is the tallest, followed by Emma and John.
Example 2:

Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
Output: ["Bob","Alice","Bob"]
Explanation: The first Bob is the tallest, followed by Alice and the second Bob.
 

Constraints:

n == names.length == heights.length
1 <= n <= 103
1 <= names[i].length <= 20
1 <= heights[i] <= 105
names[i] consists of lower and upper case English letters.
All the values of heights are distinct.
Accepted
197,404
Submissions
237,651
''')
