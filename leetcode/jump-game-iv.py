from lc import *

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        v = defaultdict(list)
        for i, a in enumerate(arr):
            v[a].append(i)
        w,d = {0},{-1}
        for c in count():
            d.update(w)
            if len(arr)-1 in d:
                return c
            w={j for i in w for j in [i-1,i+1]+v.pop(arr[i],[])}-d

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        return next((c for c in count() if (len(arr)-1 in (d.update(w),w)[1] or not(w:={j for i in w for j in [i-1,i+1]+v.pop(arr[i],[])}-d,1))),(v:=defaultdict(list),any(v[a].append(i) for i, a in enumerate(arr)),w:={0},d:={-1}))

test('''
1345. Jump Game IV
Hard

2675

101

Add to List

Share
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that index 9 is the last index of the array.
Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You do not need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index of the array.
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8
''')
