from lc import *

# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/808502/O(N)-Solution-with-Clear-Explanation-Python-%2B-One-Line-Solution

class Solution:
    def canMakeArithmeticProgression(self, a: List[int]) -> bool:
        n,m=len(a),min(a);x=(max(a)-m)/(n-1);return sum(a)==n*(m-x+(n+1)/2*x)

# https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/discuss/720386/Python-Two-Line

class Solution:
    def canMakeArithmeticProgression(self, a: List[int]) -> bool:
        a.sort();return len({j-i for i,j in zip(a,a[1:])})<2

test('''
1502. Can Make Arithmetic Progression From Sequence
Easy

1093

66

Add to List

Share
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
 

Constraints:

2 <= arr.length <= 1000
-10^6 <= arr[i] <= 10^6
Accepted
134,136
Submissions
198,350
Seen this question in a real interview before?

Yes

No
Consider that any valid arithmetic progression will be in sorted order.
Sort the array, then check if the differences of all consecutive elements are equal.
''')

