from lc import *
# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/solutions/7273273/swift-1-liner-code-explanation/?envType=daily-question&envId=2025-10-15

"""
class Solution {
    func maxIncreasingSubarrays(_ nums: [Int]) -> Int {
        nums
            .chunked(by: <)                             // Split into strictly increasing segments
            .map(\\.count)                               // Get the length of each increasing segment
            .adjacentPairs()                            // Pair each segment with its neighbor
            .map { max($0 / 2, $1 / 2, min($0, $1)) }   // Compute valid k for each pair
            .max() ?? nums.count / 2                    // Return the maximum k found, or half the array length if no adjacent pairs (i.e. only one segment)
    }
}
"""

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        b = [i for i, (x, y) in enumerate(pairwise(a), 1) if y <= x]
        c = [0] + b + [len(a)]
        s = [j - i for i, j in pairwise(c)]
        return len(a)//2 if len(s)==1 else max(max(x//2, y//2, min(x, y)) for x, y in pairwise(s))

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        s=[j-i for i,j in pairwise([0]+[i for i,(x,y)in enumerate(pairwise(a),1)if y<=x]+[len(a)])];return len(a)//2 if len(s)==1 else max(max(x//2,y//2,min(x,y))for x,y in pairwise(s))

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        return max((max(x//2,y//2,min(x,y))for x,y in pairwise([j-i for i,j in pairwise([0]+[i for i,(x,y)in enumerate(pairwise(a),1)if y<=x]+[len(a)])])),default=len(a)//2)

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        p=pairwise;return max((max(x//2,y//2,min(x,y))for x,y in p(j-i for i,j in p([0,*[i for i,(x,y)in enumerate(p(a),1)if y<=x],len(a)]))),default=len(a)//2)

# by AB

class Solution:
    def maxIncreasingSubarrays(self, n: list[int]) -> int:
        p=pairwise;return max(max(-b//2,-max(a,b))for a,b in p(starmap(sub,p(i for i,(c,d)in enumerate(p(n[:1]*2+n+n[-1:]))if c>=d))))

# https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/solutions/6028753/java-c-python-one-pass-o-1-space/?envType=daily-question&envId=2025-10-15

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        n = len(a)
        up = 1
        pre_max_up = 0
        res = 0
        for i in range(1, n):
            if a[i] > a[i - 1]:
                up = up + 1
            else:
                pre_max_up = up
                up = 1
            res = max(res, up // 2, min(pre_max_up, up))
        return res

class Solution:
    def maxIncreasingSubarrays(self, a: list[int]) -> int:
        u=p=1;return max(max(u//2,min(p,u))for x,y in pairwise(a)if x<y and(u:=u+1)or(p:=u,u:=1))

test('''
3350. Adjacent Increasing Subarrays Detection II
Medium
Topics
premium lock icon
Companies
Hint
Given an array nums of n integers, your task is to find the maximum value of k for which there exist two adjacent subarrays of length k each, such that both subarrays are strictly increasing. Specifically, check if there are two subarrays of length k starting at indices a and b (a < b), where:

Both subarrays nums[a..a + k - 1] and nums[b..b + k - 1] are strictly increasing.
The subarrays must be adjacent, meaning b = a + k.
Return the maximum possible value of k.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [2,5,7,8,9,2,3,4,3,1]

Output: 3

Explanation:

The subarray starting at index 2 is [7, 8, 9], which is strictly increasing.
The subarray starting at index 5 is [2, 3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 3 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.
Example 2:

Input: nums = [1,2,3,4,4,4,4,5,6,7]

Output: 2

Explanation:

The subarray starting at index 0 is [1, 2], which is strictly increasing.
The subarray starting at index 2 is [3, 4], which is also strictly increasing.
These two subarrays are adjacent, and 2 is the maximum possible value of k for which two such adjacent strictly increasing subarrays exist.


Other examples:

Input: nums = [-15,19]
Output: 1


Input: nums = [-15,-13,4,7]
Output: 2

Input: nums = [14,-3,12]
Output: 1

Constraints:

2 <= nums.length <= 2 * 105
-109 <= nums[i] <= 109
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
34,815/73.9K
Acceptance Rate
47.1%
Topics
Array
Binary Search
Weekly Contest 423
icon
Companies
Hint 1
Find the boundaries between strictly increasing subarrays.
Hint 2
Can we use binary search?
''')
