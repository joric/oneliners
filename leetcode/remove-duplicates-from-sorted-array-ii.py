from lc import *

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/968017/Python-binary-search-solution-(upper-bound-aka-bisect_right)

class Solution:
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

class Solution:
    def removeDuplicates(self, nums) -> int:
        i = 0
        for n in nums:
            if i < 2 or n > nums[i-2]:
                nums[i] = n
                i += 1
        return i

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return reduce(lambda i,n:setitem(nums,i,n) or i+1 if i<2 or n>nums[i-2] else i, nums, 0)

# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/discuss/1133269/one-line-python-solution-python-one_line-Remove

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        [[nums.remove(num) for i in range(nums.count(num)-2)] for num in nums]

# updated 2024-03-06 (not a daily problem)

class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        n[:]=[k for k,v in Counter(n).items()for _ in range(min(v,2))]

class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        c=Counter(n);n[:]=[k for k in c for i in range(min(c[k],2))]

class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        n[:]=[*chain(*[[k]*min(v,2)for k,v in Counter(n).items()])]

class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        c=Counter(n);n[:]=[*chain(*[[k]*min(c[k],2)for k in c])]

class Solution:
    def removeDuplicates(self, n: List[int]) -> int:
        [[n.remove(x)for i in range(n.count(x)-2)]for x in n]

test('''

80. Remove Duplicates from Sorted Array II
Medium

4195

959

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
Output: 5, nums = [1,1,2,2,3,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3]
Output: 7, nums = [0,0,1,1,2,3,3,_,_]
Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

Constraints:

1 <= nums.length <= 3 * 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

''', 

check=lambda res,exp,nums:nums[:exp[0]]==json.loads(exp[1].replace(',_',''))

)
