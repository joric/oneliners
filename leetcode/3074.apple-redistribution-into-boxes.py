from lc import *

# Q1. https://leetcode.com/contest/weekly-contest-388/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], c: List[int]) -> int:
        x = sum(apple)
        v = 0
        c.sort(reverse=True)
        n = len(c)
        for i in range(n):
            v += c[i]
            if v >= x:
                return i + 1
        return -1

class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return next((i+1 for i,x in enumerate(accumulate(sorted(c)[::-1]))if x>=sum(a)),len(c))

# https://leetcode.com/problems/apple-redistribution-into-boxes/solutions/7434223/one-line-solution-by-mikposp-5jik/?envType=daily-question&envId=2025-12-24

class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return sum(map(lt,accumulate(sorted(c)[::-1]),repeat(sum(a))))+1

class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return bisect_left([*accumulate(sorted(c)[::-1])],sum(a))+1

test('''
3074. Apple Redistribution into Boxes
User Accepted:19509
User Tried:21204
Total Accepted:20678
Total Submissions:34905
Difficulty:Easy
You are given an array apple of size n and an array capacity of size m.

There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.

Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.

Note that, apples from the same pack can be distributed into different boxes.

 

Example 1:

Input: apple = [1,3,2], capacity = [4,3,1,5,2]
Output: 2
Explanation: We will use boxes with capacities 4 and 5.
It is possible to distribute the apples as the total capacity is greater than or equal to the total number of apples.
Example 2:

Input: apple = [5,5,5], capacity = [2,4,2,7]
Output: 4
Explanation: We will need to use all the boxes.
 

Constraints:

1 <= n == apple.length <= 50
1 <= m == capacity.length <= 50
1 <= apple[i], capacity[i] <= 50
The input is generated such that it's possible to redistribute packs of apples into boxes.
''')
