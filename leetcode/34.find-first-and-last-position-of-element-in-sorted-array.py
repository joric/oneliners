from lc import *

# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array


'''cpp version with equal range (still longer than python)

// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/6652071/stdequal_range-by-beervirus-q0o3/

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto [l,r] = equal_range(nums.begin(), nums.end(), target);
        if (l == nums.end() || *l != target) return {-1,-1};
        return {(int)distance(nums.begin(), l), (int)distance(nums.begin(), r) - 1};
    }
};


// https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/solutions/1181940/c-short-stdequal_range-solution-by-seand-fpdh/

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) {
        auto [l, r] = equal_range(begin(nums), end(nums), target);
        if (l == end(nums) || *l != target)
            return {-1, -1};

        int i = l - begin(nums), j = r - 1 - begin(nums);
        return {i, j};
    }
};

'''


class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        return(v.index(t),len(v)-1-v[::-1].index(t))if v.count(t)else(-1,-1)

class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        a,b=bisect_left(v,t),bisect_right(v,t);return([-1]*2,(a,b-1))[a<b]

class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        a=v.count(t);return(v.index(t),a+v.index(t)-1)if a else[-1]*2

class Solution:
    def searchRange(self, v: List[int], t: int) -> List[int]:
        return(a:=v.count(t))and(b:=v.index(t),a+b-1)or[-1]*2

test('''
34. Find First and Last Position of Element in Sorted Array
Medium

18723

449

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
''')
