from lc import *

# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/5008562/one-line-solution

class Solution:
    def sortedArrayToBST(self, a: List[int]) -> Optional[TreeNode]:
        return(f:=lambda a:a and TreeNode(a[m:=len(a)//2],f(a[:m]),f(a[m+1:]))or None)(a)

test('''
108. Convert Sorted Array to Binary Search Tree
Easy

10779

545

Add to List

Share
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary search tree.

 

Example 1:


Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Example 2:


Input: nums = [1,3]
Output: [3,1]
Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in a strictly increasing order.
Accepted
1,180,763
Submissions
1,649,399
''')
