from lc import *

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        q, i, n = deque(), 0, len(arr)
        while i < n:
            if arr[i] == 0:
                q.append(0)
            if q:
                q.append(arr[i])
                arr[i] = q.popleft()
            i += 1

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        [arr.insert(i,0) or arr.pop() for i in range(len(arr)-1,-1,-1) if not arr[i]]

class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        arr[:]=[x for a in arr for x in ([a] if a else [0,0])][:len(arr)]


test('''

1089. Duplicate Zeros
Easy

Given a fixed-length integer array arr, duplicate each occurrence of zero, shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

Example 1:

Input: arr = [1,0,2,3,0,4,5,0]
Output: [1,0,0,2,3,0,0,4]
Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]

Example 2:

Input: arr = [1,2,3]
Output: [1,2,3]
Explanation: After calling your function, the input array is modified to: [1,2,3]

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 9

''',
check=lambda res, expected, arr: arr==expected

)
