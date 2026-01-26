from lc import *

# https://leetcode.com/problems/minimum-absolute-difference/solutions/7525931/greedy-two-approaches-python-3-by-santac-o1ov/?envType=daily-question&envId=2026-01-26

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();
        c=defaultdict(list)
        for i in range(len(a)-1):
            c[a[i+1]-a[i]].append([a[i],a[i+1]])
        return c[sorted(c)[0]]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();d=defaultdict(list);[d[y-x].append((x,y))for x,y in pairwise(a)];return d[min(d)]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        d=defaultdict(list);[d[y-x].append((x,y))for x,y in pairwise(sorted(a))];return d[min(d)]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        d=defaultdict(list);[d[-sub(*p)].append(p)for p in pairwise(sorted(a))];return d[min(d)]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        d={};[d.setdefault(-sub(*p),[]).append(p)for p in pairwise(sorted(a))];return d[min(d)]

# https://leetcode.com/problems/minimum-absolute-difference/solutions/7524943/one-line-solution-by-xxxxkav-qgl7/?envType=daily-question&envId=2026-01-26

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();return[[x,y]for x,y in pairwise(a)if y-x==min(b-a for a,b in pairwise(a))]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();t=[*pairwise(a)];return[[x,y] for x,y in t if y-x==min(b-a for a,b in t)]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        t=[*pairwise(sorted(a))];return[p for p in t if sub(*p)==max(starmap(sub,t))]

class Solution: # TLE
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();return[p for p in pairwise(a)if sub(*p)==max(map(sub,a,a[1:]))]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();m=max(map(sub,a,b:=a[1:]));return[p for p in zip(a,b)if sub(*p)==m]

class Solution:
    def minimumAbsDifference(self, a: List[int]) -> List[List[int]]:
        a.sort();m=max(map(sub,a,a[1:]));return[p for p in pairwise(a)if sub(*p)==m]

test('''
1200. Minimum Absolute Difference
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements.

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Example 2:

Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Example 3:

Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
 

Constraints:

2 <= arr.length <= 105
-106 <= arr[i] <= 106
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
332,447/454K
Acceptance Rate
73.2%
Topics
Array
Sorting
Weekly Contest 155
icon
Companies
Hint 1
Find the minimum absolute difference between two elements in the array.
Hint 2
The minimum absolute difference must be a difference between two consecutive elements in the sorted array.
Similar Questions
Minimum Cost of Buying Candies With Discount
Easy
Minimize the Maximum Difference of Pairs
Medium
''')
