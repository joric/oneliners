from lc import *

# https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/2610842/7-Lines-Of-code-oror-JAVA-oror-sliding-Window

class Solution:
    def maxFrequency(self, a: List[int], k: int) -> int:
        r=l=s=v=0
        a.sort()
        for r,x in enumerate(a):
            s += x
            while x*(r-l+1)-s>k:
                s -= a[l]
                l += 1
            v = max(v,r-l+1);
        return v

class Solution:
    def maxFrequency(self, a: List[int], k: int) -> int:
        r=l=s=v=0;a.sort();[(s:=s+x,all(k+s<x*(r-l+1)and(s:=s-a[l],l:=l+1)for _ in a),v:=max(v,r-l+1))for r,x in enumerate(a)];return v

# https://leetcode.com/problems/frequency-of-the-most-frequent-element/discuss/1175090/JavaC%2B%2BPython-Sliding-Window

class Solution:
    def maxFrequency(self, a: List[int], k: int) -> int:
        i=0;a.sort();[(k:=k+x,k<x*(j-i+1)and(k:=k-a[i],i:=i+1))for j,x in enumerate(a)];return len(a)-i

test('''
1838. Frequency of the Most Frequent Element
Medium

3088

84

Add to List

Share
The frequency of an element is the number of times it occurs in an array.

You are given an integer array nums and an integer k. In one operation, you can choose an index of nums and increment the element at that index by 1.

Return the maximum possible frequency of an element after performing at most k operations.

 

Example 1:

Input: nums = [1,2,4], k = 5
Output: 3
Explanation: Increment the first element three times and the second element two times to make nums = [4,4,4].
4 has a frequency of 3.
Example 2:

Input: nums = [1,4,8,13], k = 5
Output: 2
Explanation: There are multiple optimal solutions:
- Increment the first element three times to make nums = [4,4,8,13]. 4 has a frequency of 2.
- Increment the second element four times to make nums = [1,8,8,13]. 8 has a frequency of 2.
- Increment the third element five times to make nums = [1,4,13,13]. 13 has a frequency of 2.
Example 3:

Input: nums = [3,9,6], k = 2
Output: 1
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5
1 <= k <= 10^5
Accepted
60,181
Submissions
149,534
''')

