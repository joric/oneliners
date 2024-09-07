from lc import *


# https://leetcode.com/problems/next-permutation/

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        perm, l = False, len(nums) - 2
        while 0 <= l:
            r = len(nums) - 1  
            while l < r and nums[r] <= nums[l]:
                r -= 1
            if r <= l:
                l -= 1
            else:
                nums[l], nums[l + 1:], perm = nums[r], sorted(nums[l + 1:r] + [nums[l]] + nums[r + 1:]), True
                break
        if not perm:
            nums.sort()

class Solution: # WRONG, unfortunately
    def nextPermutation(self, a: List[int]) -> None:
        s = sorted(a)
        if a==s[::-1]:
            p = s
        else:
            for i,p in enumerate(permutations(a)):
                print(p)
                if i==1: break
        a[:] = p

# https://leetcode.com/problems/next-permutation/discuss/1043577/Python-O(n)-inplace-solution-explained/1217662

class Solution:
    def nextPermutation(self, v: List[int]) -> None:
        a = next((i for i in range(len(v)-2,-1,-1)if v[i]<v[i+1]), None)
        if a is not None:
            b = next((i for i in range(len(v)-1,a,-1)if v[i]>v[a]), None)
            v[a], v[b] = v[b], v[a]
            v[a+1:]=sorted(v[a+1:])
        else:
            v.sort()

class Solution:
    def nextPermutation(self, v: List[int]) -> None:
        (a:=next((i for i in range(len(v)-2,-1,-1)if v[i]<v[i+1]), None))is not None and(b:=next((i for i in range(len(v)-1,a,-1)if v[i]>v[a]), None),exec('v[a],v[b]=v[b],v[a];v[a+1:]=sorted(v[a+1:])'))or v.sort()

test('''
31. Next Permutation
Medium

18619

4730

Add to List

Share
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums.

The replacement must be in place and use only constant extra memory.

 

Example 1:

Input: nums = [1,2,3]
Output: [1,3,2]

Example 2:

Input: nums = [3,2,1]
Output: [1,2,3]

Example 3:

Input: nums = [1,1,5]
Output: [1,5,1]

Other examples:

Input: nums = [1,3,2]
Output: [2,1,3]

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 100
Accepted
1,482,781
Submissions
3,618,906
''', check=lambda r,e,a:e==a)
