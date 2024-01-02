from lc import *

# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/discuss/3408742/one-liner

class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        return[[x for x in r if x]for r in zip_longest(*[[v]*c for v,c in Counter(n).items()])]

class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        c=Counter(n);return[[x for x in r if x]for r in zip_longest(*[[k]*c[k] for k in c])]

class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        c=Counter(n);return[[x for x,v in c.items()if i<v]for i in range(max(c.values()))]

# https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/discuss/3368523/JavaC%2B%2BPython-Maximum-Frequence

class Solution:
    def findMatrix(self, n: List[int]) -> List[List[int]]:
        c=Counter(n);k=max(c.values());return[[*c.elements()][i::k]for i in range(k)]

test('''
2610. Convert an Array Into a 2D Array With Conditions
Medium

481

13

Add to List

Share
You are given an integer array nums. You need to create a 2D array from nums satisfying the following conditions:

The 2D array should contain only the elements of the array nums.
Each row in the 2D array contains distinct integers.
The number of rows in the 2D array should be minimal.
Return the resulting array. If there are multiple answers, return any of them.

Note that the 2D array can have a different number of elements on each row.

 

Example 1:

Input: nums = [1,3,4,1,2,3,1]
Output: [[1,3,4,2],[1,3],[1]]
Explanation: We can create a 2D array that contains the following rows:
- 1,3,4,2
- 1,3
- 1
All elements of nums were used, and each row of the 2D array contains distinct integers, so it is a valid answer.
It can be shown that we cannot have less than 3 rows in a valid array.
Example 2:

Input: nums = [1,2,3,4]
Output: [[4,3,2,1]]
Explanation: All elements of the array are distinct, so we can keep all of them in the first row of the 2D array.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= nums.length
Accepted
36,356
Submissions
43,547
''', check=lambda res, exp, nums:sorted(chain(*res))==sorted(chain(*exp)) and all(len(set(r))==len(r) for r in res)
)

