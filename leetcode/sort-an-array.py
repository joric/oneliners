from lc import *

# quicksort (TLE)

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=1:
            return nums
        m = nums.pop()
        l = []
        g = []
        for i in nums:
            if i < m:
                l.append(i)
            else:
                g.append(i)
        return self.sortArray(l) + [m] + self.sortArray(g)

# builtin

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return sorted(nums)

# counting sort

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = []
        c = Counter(nums)
        for i in sorted(c.keys()):
            r += [i]*c[i]
        return r

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        r = []
        b = {k:0 for k in range(min(nums), max(nums)+1)}
        for x in nums:
            b[x] += 1
        for x in b.keys():
            if b[x]:
                r.extend(b[x]*[x])
        return r

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return (r:=[],b:={k:0 for k in range(min(nums),max(nums)+1)},any(setitem(b,x,b[x]+1) for x in nums),any(b[x] and r.extend([x]*b[x]) for x in b.keys()),r)[4]

test('''

912. Sort an Array
Medium

3577

631

Add to List

Share
Given an array of integers nums, sort the array in ascending order and return it.

You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

 

Example 1:

Input: nums = [5,2,3,1]
Output: [1,2,3,5]
Explanation: After sorting the array, the positions of some numbers are not changed (for example, 2 and 3), while the positions of other numbers are changed (for example, 1 and 5).
Example 2:

Input: nums = [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
Explanation: Note that the values of nums are not necessairly unique.
 

Constraints:

1 <= nums.length <= 5 * 10^4
-5 * 104 <= nums[i] <= 5 * 10^4
''')

