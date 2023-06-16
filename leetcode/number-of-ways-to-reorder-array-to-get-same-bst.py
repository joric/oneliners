from lc import *

class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        def f(a):
            if len(a)<3:
                return 1
            return comb(len(l:=[v for v in a if v<a[0]])+len(r:=[v for v in a if v>a[0]]),len(r))*f(l)*f(r)
        return (f(nums)-1) % (10**9+7)

class Solution:
    def numOfWays(self, n: List[int]) -> int:
        f=lambda a:len(a)>2and comb(len(l:=[v for v in a if v<a[0]])+len(r:=[v for v in a if v>a[0]]),len(r))*f(l)*f(r)or 1;return(f(n)-1)%(10**9+7)

class Solution:
    def numOfWays(self, n):
        f=lambda a:a and comb(len(a)-1,len(l:=[v for v in a if v<a[0]]))*f(l)*f([v for v in a if v>a[0]])or 1;return(f(n)-1)%(10**9+7)

test('''
1569. Number of Ways to Reorder Array to Get Same BST
Hard

627

69

Add to List

Share
Given an array nums that represents a permutation of integers from 1 to n. We are going to construct a binary search tree (BST) by inserting the elements of nums in order into an initially empty BST. Find the number of different ways to reorder nums so that the constructed BST is identical to that formed from the original array nums.

For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left child, and 3 as a right child. The array [2,3,1] also yields the same BST but [3,2,1] yields a different BST.
Return the number of ways to reorder nums such that the BST formed is identical to the original BST formed from nums.

Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:


Input: nums = [2,1,3]
Output: 1
Explanation: We can reorder nums to be [2,3,1] which will yield the same BST. There are no other ways to reorder nums which will yield the same BST.
Example 2:


Input: nums = [3,4,5,1,2]
Output: 5
Explanation: The following 5 arrays will yield the same BST: 
[3,1,2,4,5]
[3,1,4,2,5]
[3,1,4,5,2]
[3,4,1,2,5]
[3,4,1,5,2]
Example 3:


Input: nums = [1,2,3]
Output: 0
Explanation: There are no other orderings of nums that will yield the same BST.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= nums.length
All integers in nums are distinct.
Accepted
13,986
Submissions
27,982
Seen this question in a real interview before?

Yes

No
Use a divide and conquer strategy.
The first number will always be the root. Consider the numbers smaller and larger than the root separately. When merging the results together, how many ways can you order x elements in x+y positions?
''')

