from lc import *

def check(res, expected, nums):
    return nums[:res]==expected

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/968017/Python-binary-search-solution-(upper-bound-aka-bisect_right)

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = j = k = 0
        while k<len(nums):
            #while k<len(nums) and nums[j]==nums[k]: k += 1 # brute search
            k = bisect_right(nums, nums[j], j)
            for _ in range(min(2, k-j)):
                nums[i] = nums[j]
                i += 1
            j = k
        return i

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/27976/3-6-easy-lines-C%2B%2B-Java-Python-Ruby

class Solution2:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

class Solution1:
    def removeDuplicates(self, nums: List[int]) -> int:
        return reduce(lambda i,n:nums.__setitem__(i,n) or i+1 if i<2 or n>nums[i-2] else i, nums, 0)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/1133269/one-line-python-solution-python-one_line-Remove

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        [[nums.remove(num) for i in range(nums.count(num)-2)] for num in nums]

test('''
80. Remove Duplicates from Sorted Array II
Medium

4138

953

Add to List

Share
Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,1,2,2,3]
Output: [1,1,2,2,3]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: [0,0,1,1,2,3,3]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Input: nums = [-50,-50,-49,-48,-47,-47,-47,-46,-45,-43,-42,-41,-40,-40,-40,-40,-40,-40,-39,-38,-38,-38,-38,-37,-36,-35,-34,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-26,-25,-25,-24,-24,-24,-22,-22,-21,-21,-21,-21,-21,-20,-19,-18,-18,-18,-17,-17,-17,-17,-17,-16,-16,-15,-14,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,10,11,11,12,12,13,13,13,14,14,14,15,16,17,17,18,20,21,22,22,22,23,23,25,26,28,29,29,29,30,31,31,32,33,34,34,34,36,36,37,37,38,38,38,39,40,40,40,41,42,42,43,43,44,44,45,45,45,46,47,47,47,47,48,49,49,49,50]
Output: [-50,-50,-49,-48,-47,-47,-46,-45,-43,-42,-41,-40,-40,-39,-38,-38,-37,-36,-35,-34,-34,-33,-32,-31,-30,-28,-27,-26,-26,-25,-25,-24,-24,-22,-22,-21,-21,-20,-19,-18,-18,-17,-17,-16,-16,-15,-14,-14,-13,-13,-12,-12,-10,-10,-9,-8,-8,-7,-7,-6,-5,-4,-4,-3,-1,1,2,2,3,4,5,6,6,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,16,17,17,18,20,21,22,22,23,23,25,26,28,29,29,30,31,31,32,33,34,34,36,36,37,37,38,38,39,40,40,41,42,42,43,43,44,44,45,45,46,47,47,48,49,49,50]

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.
''', check=check)
