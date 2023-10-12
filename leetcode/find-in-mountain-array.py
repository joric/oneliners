from lc import *

class MountainArray:
    def __init__(self, data):
        self.data = data
    def get(self, index: int) -> int:
        return self.data[index]
    def length(self) -> int:
        return len(self.data)

# https://leetcode.com/problems/find-in-mountain-array/discuss/317754/Python-bisect-maniac-solution

class Solution:
    def findInMountainArray(self, t: int, m: 'MountainArray') -> int:
        n = m.length()
        r = range(n)
        k = bisect_left(r,1,1,n-1,key=lambda i:m.get(i)>m.get(i+1))
        i = bisect_left(r,t,0,k+1,key=m.get)
        if i<=k and m.get(i)==t:
            return i
        j = bisect_left(r,-t,k+1,n,key=lambda i:-m.get(i))
        if j<n and m.get(j)==t:
            return j
        return -1

class Solution:
    def findInMountainArray(self, t: int, m: 'MountainArray') -> int:
        n=m.length();r,b=range(n),bisect_left;k=b(r,1,1,n-1,key=lambda i:m.get(i)>m.get(i+1));i=b(r,t,0,k+1,key=m.get);return i if i<=k and m.get(i)==t else j if(j:=b(r,-t,k+1,n,key=lambda i:-m.get(i)))<n and m.get(j)==t else-1

test('''
1095. Find in Mountain Array
Hard

2271

87

Add to List

Share
(This problem is an interactive problem.)

You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target. If such an index does not exist, return -1.

You cannot access the mountain array directly. You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer. Also, any solutions that attempt to circumvent the judge will result in disqualification.

 

Example 1:

Input: target = 3, array = [1,2,3,4,5,3,1]
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.
Example 2:

Input: target = 3, array = [0,1,2,4,2,1]
Output: -1
Explanation: 3 does not exist in the array, so we return -1.
 

Constraints:

3 <= mountain_arr.length() <= 10^4
0 <= target <= 10^9
0 <= mountain_arr.get(index) <= 10^9
''')

