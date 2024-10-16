from lc import *

# https://leetcode.com/problems/find-in-mountain-array/discuss/317754/Python-bisect-maniac-solution

class MountainArray:
    def __init__(self, data):
        self.data = data
    def get(self, index: int) -> int:
        return self.data[index]
    def length(self) -> int:
        return len(self.data)

class Solution:
    def findInMountainArray(self, t: int, m: 'MountainArray') -> int:
        r = range(n:=m.length())
        k = bisect_left(r,1,1,n-1,key=lambda i:m.get(i)>m.get(i+1))
        if (i:=bisect_left(r,t,0,k+1,key=m.get))<=k and m.get(i)==t:
            return i
        if (j:=bisect_left(r,-t,k+1,n,key=lambda i:-m.get(i)))<n and m.get(j)==t:
            return j
        return -1

class Solution:
    def findInMountainArray(self, t: int, m: 'MountainArray') -> int:
        b,g=bisect_left,m.get;k=b(r:=range(n:=m.length()),1,1,n-1,key=lambda i:g(i)>g(i+1));return i if(i:=b(r,t,0,k+1,key=g))<=k and g(i)==t else j if(j:=b(r,-t,k+1,n,key=lambda i:-g(i)))<n and g(j)==t else-1

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