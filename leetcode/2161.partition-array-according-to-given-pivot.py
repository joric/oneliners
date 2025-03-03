from lc import *

# https://leetcode.com/problems/partition-array-according-to-given-pivot/solutions/3920776/python-one-line-solution/?envType=daily-question&envId=2025-03-03

class Solution:
    def pivotArray(self, a: List[int], p: int) -> List[int]:
        return [i for i in a if i<p] + [i for i in a if i==p] + [i for i in a if i>p]

# https://leetcode.com/problems/partition-array-according-to-given-pivot/solutions/1765575/one-liner-brief-python3/

class Solution:
    def pivotArray(self, a: List[int], p: int) -> List[int]:
        return sorted(a,key=lambda x:(x>p)-(x<p))

test('''
2161. Partition Array According to Given Pivot
Medium
Topics
Companies
Hint
You are given a 0-indexed integer array nums and an integer pivot. Rearrange nums such that the following conditions are satisfied:

Every element less than pivot appears before every element greater than pivot.
Every element equal to pivot appears in between the elements less than and greater than pivot.
The relative order of the elements less than pivot and the elements greater than pivot is maintained.
More formally, consider every pi, pj where pi is the new position of the ith element and pj is the new position of the jth element. If i < j and both elements are smaller (or larger) than pivot, then pi < pj.
Return nums after the rearrangement.

 

Example 1:

Input: nums = [9,12,5,10,14,3,10], pivot = 10
Output: [9,5,3,10,10,12,14]
Explanation: 
The elements 9, 5, and 3 are less than the pivot so they are on the left side of the array.
The elements 12 and 14 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [9, 5, 3] and [12, 14] are the respective orderings.
Example 2:

Input: nums = [-3,4,3,2], pivot = 2
Output: [-3,2,4,3]
Explanation: 
The element -3 is less than the pivot so it is on the left side of the array.
The elements 4 and 3 are greater than the pivot so they are on the right side of the array.
The relative ordering of the elements less than and greater than pivot is also maintained. [-3] and [4, 3] are the respective orderings.
 

Constraints:

1 <= nums.length <= 105
-106 <= nums[i] <= 106
pivot equals to an element of nums.
Seen this question in a real interview before?
1/5
Yes
No
Accepted
103.3K
Submissions
119.7K
Acceptance Rate
86.3%
Topics
Array
Two Pointers
Simulation
Companies
Hint 1
Could you put the elements smaller than the pivot and greater than the pivot in a separate list as in the sequence that they occur?
Hint 2
With the separate lists generated, could you then generate the result?
Similar Questions
Partition List
Medium
Rearrange Array Elements by Sign
Medium
''')
