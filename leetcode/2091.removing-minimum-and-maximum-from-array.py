from lc import *

# https://leetcode.com/problems/removing-minimum-and-maximum-from-array/solutions/8462295/two-simple-lines-of-code-by-mikposp-hvbo/?envType=daily-question&envId=2026-08-30

class Solution:
    def minimumDeletions(self, a: List[int]) -> int:
        n,i,j=len(a),*sorted([a.index(min(a)),a.index(max(a))]);return min(j+1,n-i,i+1+n-j)

class Solution:
    def minimumDeletions(self, a: List[int]) -> int:
        n=len(a);i,j=sorted(map(a.index,(min(a),max(a))));return min(j+1,n-i,n+i-j+1)

test('''
2091. Removing Minimum and Maximum From Array
Medium
Topics
premium lock icon
Companies
Hint
You are given a 0-indexed array of distinct integers nums.

There is an element in nums that has the lowest value and an element that has the highest value. We call them the minimum and maximum respectively. Your goal is to remove both these elements from the array.

A deletion is defined as either removing an element from the front of the array or removing an element from the back of the array.

Return the minimum number of deletions it would take to remove both the minimum and maximum element from the array.

 

Example 1:

Input: nums = [2,10,7,5,4,1,8,6]
Output: 5
Explanation: 
The minimum element in the array is nums[5], which is 1.
The maximum element in the array is nums[1], which is 10.
We can remove both the minimum and maximum by removing 2 elements from the front and 3 elements from the back.
This results in 2 + 3 = 5 deletions, which is the minimum number possible.
Example 2:

Input: nums = [0,-4,19,1,8,-2,-3,5]
Output: 3
Explanation: 
The minimum element in the array is nums[1], which is -4.
The maximum element in the array is nums[2], which is 19.
We can remove both the minimum and maximum by removing 3 elements from the front.
This results in only 3 deletions, which is the minimum number possible.
Example 3:

Input: nums = [101]
Output: 1
Explanation:  
There is only one element in the array, which makes it both the minimum and maximum element.
We can remove it with 1 deletion.
 

Constraints:

1 <= nums.length <= 105
-105 <= nums[i] <= 105
The integers in nums are distinct.
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
64,468/113.4K
Acceptance Rate
56.9%
Topics
Staff
Array
Greedy
Weekly Contest 269
icon
Companies
Hint 1
There can only be three scenarios for deletions such that both minimum and maximum elements are removed:
Hint 2
Scenario 1: Both elements are removed by only deleting from the front.
Hint 3
Scenario 2: Both elements are removed by only deleting from the back.
Hint 4
Scenario 3: Delete from the front to remove one of the elements, and delete from the back to remove the other element.
Hint 5
Compare which of the three scenarios results in the minimum number of moves.
Similar Questions
Maximum Points You Can Obtain from Cards
Medium
Minimum Deletions to Make Character Frequencies Unique
Medium
''')
