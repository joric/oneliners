from lc import *

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res, total = 0, 0
        i = 0
        for j in range(n):
            total += nums[j]
            while i <= j and total * (j - i + 1) >= k:
                total -= nums[i]
                i += 1
            res += j - i + 1
        return res

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/solutions/5189236/bisect-o-nlogn/

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        pfx = [0] + list(accumulate(nums))
        res = 0
        for i in range(len(nums)):
            l, r = i, len(nums)
            while l < r:
                mid = (l+r+1)>>1
                if (pfx[mid]-pfx[i])*(mid-i) < k:
                    l = mid
                else: r = mid-1
            res+=l-i
        return res

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        p,n=[0,*accumulate(a)],len(a);return sum(bisect_right(range(n-i),k-1,key=lambda d:(p[i+d+1]-p[i])*(d+1))for i in range(n))

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        p,n=[0,*accumulate(a)],len(a);return sum(bisect_right(range(n-i),k-1,key=lambda d:(p[i+d+1]-p[i])*-~d)for i in range(n))

# https://leetcode.com/problems/count-subarrays-with-score-less-than-k/solutions/2138778/sliding-window/

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        s=r=j=0
        for i,x in enumerate(a):
            s += x
            while s*(i-j+1)>=k:
                s -= a[j]
                j += 1
            r += i-j +1
        return r

class Solution:
    def countSubarrays(self, a: List[int], k: int) -> int:
        s=j=0;return sum((s:=s+x,all(k<=s*(i-j+1)and(s:=s-a[j],j:=j+1)for _ in a),i-j+1)[2]for i,x in enumerate(a))

test('''
2302. Count Subarrays With Score Less Than K
Solved
Hard
Topics
Companies
Hint
The score of an array is defined as the product of its sum and its length.

For example, the score of [1, 2, 3, 4, 5] is (1 + 2 + 3 + 4 + 5) * 5 = 75.
Given a positive integer array nums and an integer k, return the number of non-empty subarrays of nums whose score is strictly less than k.

A subarray is a contiguous sequence of elements within an array.

 

Example 1:

Input: nums = [2,1,4,3,5], k = 10
Output: 6
Explanation:
The 6 subarrays having scores less than 10 are:
- [2] with score 2 * 1 = 2.
- [1] with score 1 * 1 = 1.
- [4] with score 4 * 1 = 4.
- [3] with score 3 * 1 = 3. 
- [5] with score 5 * 1 = 5.
- [2,1] with score (2 + 1) * 2 = 6.
Note that subarrays such as [1,4] and [4,3,5] are not considered because their scores are 10 and 36 respectively, while we need scores strictly less than 10.
Example 2:

Input: nums = [1,1,1], k = 5
Output: 5
Explanation:
Every subarray except [1,1,1] has a score less than 5.
[1,1,1] has a score (1 + 1 + 1) * 3 = 9, which is greater than 5.
Thus, there are 5 subarrays having scores less than 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 105
1 <= k <= 1015
Seen this question in a real interview before?
1/5
Yes
No
Accepted
84.4K
Submissions
138.7K
Acceptance Rate
60.9%
Topics
Array
Binary Search
Sliding Window
Prefix Sum
Companies
Hint 1
If we add an element to a list of elements, how will the score change?
Hint 2
How can we use this to determine the number of subarrays with score less than k in a given range?
Hint 3
How can we use “Two Pointers” to generalize the solution, and thus count all possible subarrays?
Similar Questions
Maximum Subarray
Medium
Subarray Product Less Than K
Medium
Binary Subarrays With Sum
Medium
''')

