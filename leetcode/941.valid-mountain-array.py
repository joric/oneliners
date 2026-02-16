from lc import *

# https://leetcode.com/problems/valid-mountain-array/solutions/966752/python-one-pass-explained-by-dbabichev-vtov/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        beg, end = 0, n - 1
        while beg != n-1 and arr[beg + 1] > arr[beg]: beg += 1
        while end != 0 and arr[end - 1] > arr[end]: end -= 1 
        return beg == end and end != n-1 and beg != 0

# https://leetcode.com/problems/valid-mountain-array/solutions/1717229/python3-one-line-explained-by-jjmcinto-b593/

#Runtime: 212 ms, faster than 53.19% of Python3 online submissions for Valid Mountain Array.
#Memory Usage: 15.5 MB, less than 87.22% of Python3 online submissions for Valid Mountain Array.

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        return len(a)>2 and len(d:=[1 if a[i]>a[i-1]else-1 if a[i]<a[i-1]else 0 for i in range(1,len(a))])>0 and 0<(p:=len(d)-bisect(d[::-1],0))<len(d)and list(set(d[:p]))==[1]and list(set(d[p:]))==[-1]

# https://leetcode.com/problems/valid-mountain-array/solutions/1503684/2-line-python-based-on-def-by-m31_galaxy-7wxj/

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n,m=len(a),a.index(max(a));return 0<m<n-1 and all(a[i]<a[i+1] for i in range(m)) and all(a[i]>a[i+1] for i in range(m,n-1))

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        n,m=len(a),a.index(max(a));return 0<m<n-1 and 2>a.count(a[m])and a[:m+1]==sorted(a[:m+1]) and a[m:][::-1]==sorted(a[m:])

class Solution:
    def validMountainArray(self, a: List[int]) -> bool:
        m=a.index(max(a));return 1<m+1<len(a)and min(map(lt,a,a[1:m+1]))and min(map(gt,a[m:],a[m+1:]))

test('''
941. Valid Mountain Array
Solved
Easy
Topics
premium lock icon
Companies
Hint
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
547,847/1.6M
Acceptance Rate
34.9%
Topics
Mid Level
Array
Weekly Contest 111
icon
Companies
Hint 1
It's very easy to keep track of a monotonically increasing or decreasing ordering of elements. You just need to be able to determine the start of the valley in the mountain and from that point onwards, it should be a valley i.e. no mini-hills after that. Use this information in regards to the values in the array and you will be able to come up with a straightforward solution.
Similar Questions
Minimum Number of Removals to Make Mountain Array
Hard
Beautiful Towers I
Medium
''')
