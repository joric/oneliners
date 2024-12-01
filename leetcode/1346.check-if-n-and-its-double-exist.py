from lc import *

# https://leetcode.com/problems/check-if-n-and-its-double-exist/

class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        s = set()
        for i in a:
            if 2*i in s or i%2==0 and i//2 in s:
                return True
            s.add(i)
        return False

# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/833189/One-line-Python-solution

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        return arr.count(0) > 1 or len(set(x*2 for x in arr if x != 0).intersection(set(arr))) > 0 

# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/610810/Python-one-line-solution

class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        return [*{*a}]==[0]or any(x//2 in a for x in a if x%2==0 and x)

# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/6098545/Actually-optimal-Python-one-liner

class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        return a.count(0)>1 or any(2*x in a for x in a if x)

# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/624111/one-line-javascript-solution
# var checkIfExist = function(arr) { return arr.filter(e=> arr.includes(e*2)) };

class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        return[*filter(lambda x:x*2 in a,a)]not in([],[0])

# https://leetcode.com/problems/check-if-n-and-its-double-exist/discuss/503657/1-line-Python

class Solution:
    def checkIfExist(self, a: List[int]) -> bool:
        return any(x==2*y for x,y in permutations(a,2))

test('''
1346. Check If N and Its Double Exist
Easy

2018

211

Add to List

Share
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
 

Other examples:

Input: arr = [-2,0,10,-19,4,6,-8]
Output: false

Input: arr = [10,2,5,3]
Output: true

Input: arr = [0,0]
Output: true

Constraints:

2 <= arr.length <= 500
-103 <= arr[i] <= 103
Accepted
395,764
Submissions
1,042,832
''')
