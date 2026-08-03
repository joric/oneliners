from lc import *

# https://leetcode.com/problems/find-missing-elements/solutions/7375777/one-liner-python-by-user9702tw-nvby/?envType=daily-question&envId=2026-08-04

class Solution:
    def findMissingElements(self, a: List[int]) -> List[int]:
        return sorted({*range(min(a),max(a)+1)}-{*a})

test('''
3731. Find Missing Elements
Easy
Topics
premium lock icon
Companies
Hint
You are given an integer array nums consisting of unique integers.

Originally, nums contained every integer within a certain range. However, some integers might have gone missing from the array.

The smallest and largest integers of the original range are still present in nums.

Return a sorted list of all the missing integers in this range. If no integers are missing, return an empty list.

 

Example 1:

Input: nums = [1,4,2,5]

Output: [3]

Explanation:

The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. Among these, only 3 is missing.

Example 2:

Input: nums = [7,8,6,9]

Output: []

Explanation:

The smallest integer is 6 and the largest is 9, so the full range is [6,7,8,9]. All integers are already present, so no integer is missing.

Example 3:

Input: nums = [5,1]

Output: [2,3,4]

Explanation:

The smallest integer is 1 and the largest is 5, so the full range should be [1,2,3,4,5]. The missing integers are 2, 3, and 4.

 

Constraints:

2 <= nums.length <= 100
1 <= nums[i] <= 100
 
Seen this question in a real interview before?
1/6
Yes
No
Accepted
73,636/88.3K
Acceptance Rate
83.4%
Topics
Mid Level
Array
Hash Table
Sorting
Weekly Contest 474
icon
Companies
Hint 1
First, find the maximum and minimum elements in the array.
Hint 2
Then, iterate over all the integers in the range [min, max] and check if they are in the array.
Hint 3
If not, add them to the array, and return the sorted array at the end.
''')
