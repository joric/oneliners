from lc import *

# https://leetcode.com/problems/minimum-operations-to-make-binary-array-elements-equal-to-one-i/solutions/6510546/minimum-operations-to-make-binary-array-elements-equal-to-one-i/?envType=daily-question&envId=2025-03-19

class Solution:
    def minOperations(self, a: List[int]) -> int:
        c = 0
        for i in range(2, len(a)):
            if a[i - 2] == 0:
                a[i-2] ^= 1
                a[i-1] ^= 1
                a[i-0] ^= 1
                c += 1
        return(-1,c)[sum(a)==len(a)]

class Solution:
    def minOperations(self, a: List[int]) -> int:
        c = 0
        for i in range(len(a)-2):
            if a[i] == 0:
                a[i+1] ^= 1
                a[i+2] ^= 1
                c += 1
        return(-1,c)[a[-2]==a[-1]==1]

# exec does not work on LC site for some reason
# remote: 3.11.10 (main, Sep  7 2024, 18:35:41) [GCC 13.2.0]
# local:  3.12.9 (tags/v3.12.9:fdb8142, Feb  4 2025, 15:27:58) [MSC v.1942 64 bit (AMD64)]
# exec('a[i+j]^=1',{'a':a,'i':i,'j':j}

class Solution:
    def minOperations(self, a: List[int]) -> int:
        return(-1,len([[setitem(a,i+j,a[i+j]^1)for j in(1,2)]for i in range(len(a)-2)if a[i]<1]))[a[-2]+a[-1]==2]

test('''
3191. Minimum Operations to Make Binary Array Elements Equal to One I
Medium
Topics
Companies
Hint
You are given a binary array nums.

You can do the following operation on the array any number of times (possibly zero):

Choose any 3 consecutive elements from the array and flip all of them.
Flipping an element means changing its value from 0 to 1, and from 1 to 0.

Return the minimum number of operations required to make all elements in nums equal to 1. If it is impossible, return -1.

 

Example 1:

Input: nums = [0,1,1,1,0,0]

Output: 3

Explanation:
We can do the following operations:

Choose the elements at indices 0, 1 and 2. The resulting array is nums = [1,0,0,1,0,0].
Choose the elements at indices 1, 2 and 3. The resulting array is nums = [1,1,1,0,0,0].
Choose the elements at indices 3, 4 and 5. The resulting array is nums = [1,1,1,1,1,1].
Example 2:

Input: nums = [0,1,1,1]

Output: -1

Explanation:
It is impossible to make all elements equal to 1.

Other solutions:

Input: nums = [0,1,1,0,1,0,0]
Output: -1


Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 1
Seen this question in a real interview before?
1/5
Yes
No
Accepted
94.2K
Submissions
122.2K
Acceptance Rate
77.1%
Topics
Array
Bit Manipulation
Queue
Sliding Window
Prefix Sum
Companies
Hint 1
If nums[0] is 0, then the only way to change it to 1 is by doing an operation on the first 3 elements of the array.
Hint 2
After Changing nums[0] to 1, use the same logic on the remaining array.
Similar Questions
Minimum Number of K Consecutive Bit Flips
Hard
''')
