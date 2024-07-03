from lc import *

# https://leetcode.com/problems/intersection-of-two-arrays-ii

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        d = Counter(nums1)
        for i in nums2:
            if i in d:
                if d[i] > 1:
                    d[i] -= 1
                else:
                    del d[i]
                result.append(i)
        return result

# https://leetcode.com/problems/intersection-of-two-arrays-ii/discuss/82269/Short-Python-C%2B%2B

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        return reduce(and_,map(Counter,(a,b))).elements()

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        return(Counter(a)&Counter(b)).elements()

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        return((c:=Counter)(a)&c(b)).elements()

class Solution:
    def intersect(self, a: List[int], b: List[int]) -> List[int]:
        c=Counter;return(c(a)&c(b)).elements()

test('''
350. Intersection of Two Arrays II
Easy

7164

941

Add to List

Share
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.
 

Constraints:

1 <= nums1.length, nums2.length <= 1000
0 <= nums1[i], nums2[i] <= 1000
 

Follow up:

What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?
Accepted
1,224,967
Submissions
2,164,062
''')
