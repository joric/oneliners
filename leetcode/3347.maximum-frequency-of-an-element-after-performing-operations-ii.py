from lc import *

# https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-ii/solutions/7290517/three-simple-lines-of-code/?envType=daily-question&envId=2025-10-22

class Solution:
    def maxFrequency(self, a: List[int], k: int, o: int) -> int:
        a,z,r=sorted(a),Counter(a),bisect_right;return max(max(min(r(a,v+k)-bisect_left(a,v-k)-z[v],o)+z[v],min(r(a,v+2*k)-i,o))for i,v in enumerate(a))

test('''
3347. Maximum Frequency of an Element After Performing Operations II
Solved
Hard
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and two integers k and numOperations.

You must perform an operation numOperations times on nums, where in each operation you:

Select an index i that was not selected in any previous operations.
Add an integer in the range [-k, k] to nums[i].
Return the maximum possible frequency of any element in nums after performing the operations.

 

Example 1:

Input: nums = [1,4,5], k = 1, numOperations = 2

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1], after which nums becomes [1, 4, 5].
Adding -1 to nums[2], after which nums becomes [1, 4, 4].
Example 2:

Input: nums = [5,11,20,20], k = 5, numOperations = 1

Output: 2

Explanation:

We can achieve a maximum frequency of two by:

Adding 0 to nums[1].
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
0 <= k <= 109
0 <= numOperations <= nums.length
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
10,605/27.5K
Acceptance Rate
38.5%
Topics
Array
Binary Search
Sliding Window
Sorting
Prefix Sum
Biweekly Contest 143
icon
Companies
Hint 1
Similar Questions
Frequency of the Most Frequent Element
Medium
Count Elements With Maximum Frequency
Easy
''')
