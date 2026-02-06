from lc import *

# https://leetcode.com/problems/minimum-removals-to-balance-array/solutions/7040974/python-one-line-by-ante-k8rw/?envType=daily-question&envId=2026-02-06

class Solution:
    def minRemoval(self, a: List[int], k: int) -> int:
        return(lambda a:reduce(lambda i,x:i+(x>a[i]*k),a,0))(sorted(a))

class Solution:
    def minRemoval(self, a: List[int], k: int) -> int:
        a.sort();return reduce(lambda i,x:i+(x>a[i]*k),a,0)

class Solution:
    def minRemoval(self, a: List[int], k: int) -> int:
        a.sort();i=0;[i:=i+(x>a[i]*k)for x in a];return i

test('''
3634. Minimum Removals to Balance Array
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given an integer array nums and an integer k.

An array is considered balanced if the value of its maximum element is at most k times the minimum element.

You may remove any number of elements from nums​​​​​​​ without making it empty.

Return the minimum number of elements to remove so that the remaining array is balanced.

Note: An array of size 1 is considered balanced as its maximum and minimum are equal, and the condition always holds true.

 

Example 1:

Input: nums = [2,1,5], k = 2

Output: 1

Explanation:

Remove nums[2] = 5 to get nums = [2, 1].
Now max = 2, min = 1 and max <= min * k as 2 <= 1 * 2. Thus, the answer is 1.
Example 2:

Input: nums = [1,6,2,9], k = 3

Output: 2

Explanation:

Remove nums[0] = 1 and nums[3] = 9 to get nums = [6, 2].
Now max = 6, min = 2 and max <= min * k as 6 <= 2 * 3. Thus, the answer is 2.
Example 3:

Input: nums = [4,6], k = 2

Output: 0

Explanation:

Since nums is already balanced as 6 <= 4 * 2, no elements need to be removed.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109
1 <= k <= 105
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
30,022/78.3K
Acceptance Rate
38.4%
Topics
Senior
Array
Sliding Window
Sorting
Biweekly Contest 162
icon
Companies
Hint 1
Sort nums and use two pointers i and j so that the window's minimum is nums[i] and maximum is nums[j].
Hint 2
Expand j while nums[j] <= k * nums[i] to maximize the balanced window; answer = n - (j - i + 1).
''')
