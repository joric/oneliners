from lc import *

# https://leetcode.com/problems/sum-of-distances/solutions/3401591/python-3-7-lines-w-comments-ts-72-89-by-gffze/

class Solution:
    def distance(self, a: List[int]) -> List[int]:
        d=defaultdict(list)
        for i,x in enumerate(a):
            d[x].append(i)
        for t in d.values():
            p = list(accumulate(t))
            s = sum(t)
            for i,x in enumerate(t):
                a[x] = s+(2*i+2-len(t))*x-2*p[i]
        return a

class Solution:
    def distance(self, a: List[int]) -> List[int]:
        d={};[d.setdefault(x,[]).append(i)for i,x in enumerate(a)];[setitem(a,x,s+(2*i+2-len(t))*x-2*p[i])for t in d.values()for i,x in enumerate(t)if(p:=[*accumulate(t)],s:=sum(t))];return a

class Solution:
    def distance(self, a: List[int]) -> List[int]:
        d={};[d.setdefault(c,[]).append(i)for i,c in enumerate(a)];[setitem(a,x,s-len(t)*x-2*(x*~i+(p:=p+x)))for t in d.values()if[s:=sum(t),p:=0]for i,x in enumerate(t)];return a

test('''
2615. Sum of Distances
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109
 

Note: This question is the same as 2121: Intervals Between Identical Elements.

 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
29,246/89.6K
Acceptance Rate
32.6%
Topics
Senior
Array
Hash Table
Prefix Sum
Weekly Contest 340
icon
Companies
Hint 1
Can we use the prefix sum here?
Hint 2
For each number x, collect all the indices where x occurs, and calculate the prefix sum of the array.
Hint 3
For each occurrence of x, the indices to the right will be regular subtraction while the indices to the left will be reversed subtraction.
Similar Questions
Remove Duplicates from Sorted Array
Easy
Find All Duplicates in an Array
Medium
Minimum Operations to Make All Array Elements Equal
Medium
''')
