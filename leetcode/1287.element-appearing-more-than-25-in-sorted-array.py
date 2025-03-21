from lc import *

# boyer-moore https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/521862/JavaScript-Boyer-Moore-Voting-Algorithm

class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        r = c = 0
        for x in a:
            if c==0 or c==1:
                r = x
            c += 3 if r==x else -1
        return r

# editorial (log n)

class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        n=len(a);return next(x for x in(a[n//4],a[n//2],a[3*n//4])if bisect_right(a,x)-bisect_left(a,x)>n/4)

class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        n=len(a);return next(u for i in(1,2,3)if a[t:=bisect_left(a,u:=a[i*n//4])]==a[t+n//4])

# https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/discuss/930267/One-line-solution

class Solution:
    def findSpecialInteger(self, a: List[int]) -> int:
        return Counter(a).most_common()[0][0]

test('''
1287. Element Appearing More Than 25% In Sorted Array
Easy

1048

52

Add to List

Share
Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5
''')
