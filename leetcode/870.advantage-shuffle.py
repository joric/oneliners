from lc import *

class Solution:
    def advantageCount(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (lambda s: [s.pop(s[-1]>b and bisect_right(s, b)) for b in nums2])(sorted(nums1))

class Solution:
    def advantageCount(self, a: List[int], b: List[int]) -> List[int]:
        return a.sort() or [a.pop(a[-1]>x and bisect_right(a,x)) for x in b]

test('''

870. Advantage Shuffle
Medium

1390

87

Add to List

Share
You are given two integer arrays nums1 and nums2 both of the same length. The advantage of nums1 with respect to nums2 is the number of indices i for which nums1[i] > nums2[i].

Return any permutation of nums1 that maximizes its advantage with respect to nums2.

 

Example 1:

Input: nums1 = [2,7,11,15], nums2 = [1,10,4,11]
Output: [2,11,7,15]
Example 2:

Input: nums1 = [12,24,8,32], nums2 = [13,25,32,11]
Output: [24,32,8,12]
 

Constraints:

1 <= nums1.length <= 10^5
nums2.length == nums1.length
0 <= nums1[i], nums2[i] <= 10^9


''')