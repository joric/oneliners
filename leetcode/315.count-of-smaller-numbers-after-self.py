from lc import *

# https://leetcode.com/problems/count-of-smaller-numbers-after-self/solutions/6083115/solution-using-sortedlist-in-five-lines-zjeo6/

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        n=len(nums)
        current_list = SortedList()
        result=[0]*n
        for i in range(n-1,-1,-1):
            bisect_left_index= current_list.bisect_left(nums[i])
            result[i]=bisect_left_index
            current_list.add(nums[i])
        return result

class Solution:
    def countSmaller(self, a: List[int]) -> List[int]:
        c=SortedList();return[c.bisect_left(x)for x in a[::-1]if[c.add(x)]][::-1]

class Solution:
    def countSmaller(self, a: List[int]) -> List[int]:
        c=[];return[bisect_left(c,x)for x in a[::-1]if[insort(c,x)]][::-1]

test('''
315. Count of Smaller Numbers After Self
Solved
Hard
Topics
premium lock icon
Companies
Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
388,367/894K
Acceptance Rate
43.4%
Topics
Array
Binary Search
Divide and Conquer
Binary Indexed Tree
Segment Tree
Merge Sort
Ordered Set
icon
Companies
Similar Questions
Count of Range Sum
Hard
Queue Reconstruction by Height
Medium
Reverse Pairs
Hard
How Many Numbers Are Smaller Than the Current Number
Easy
Count Good Triplets in an Array
Hard
Count the Number of K-Big Indices
Hard
''')
