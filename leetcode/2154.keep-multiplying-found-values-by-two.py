from lc import *

# https://leetcode.com/problems/keep-multiplying-found-values-by-two/description/?envType=daily-question&envId=2025-11-19

class Solution:
    def findFinalValue(self, a: List[int], o: int) -> int:
        return reduce(lambda x,y:(x==y)*x+x,sorted(a),o)

class Solution:
    def findFinalValue(self, a: List[int], o: int) -> int:
        x=o;[x:=x+x*(x==y)for y in sorted(a)];return x

# https://leetcode.com/problems/keep-multiplying-found-values-by-two/solutions/7339327/one-line-solution-by-mikposp-ahxw/?envType=daily-question&envId=2025-11-19

class Solution:
    def findFinalValue(self, a: List[int], o: int) -> int:
        return o in a and self.findFinalValue(a,2*o)or o

class Solution:
    def findFinalValue(self, a: List[int], o: int) -> int:
        return min({o*2**i for i in range(11)}-{*a})

test('''
2154. Keep Multiplying Found Values by Two
Easy
Topics
premium lock icon
Companies
Hint
You are given an array of integers nums. You are also given an integer original which is the first number that needs to be searched for in nums.

You then do the following steps:

If original is found in nums, multiply it by two (i.e., set original = 2 * original).
Otherwise, stop the process.
Repeat this process with the new number as long as you keep finding the number.
Return the final value of original.

 

Example 1:

Input: nums = [5,3,6,1,12], original = 3
Output: 24
Explanation: 
- 3 is found in nums. 3 is multiplied by 2 to obtain 6.
- 6 is found in nums. 6 is multiplied by 2 to obtain 12.
- 12 is found in nums. 12 is multiplied by 2 to obtain 24.
- 24 is not found in nums. Thus, 24 is returned.
Example 2:

Input: nums = [2,7,9], original = 4
Output: 4
Explanation:
- 4 is not found in nums. Thus, 4 is returned.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i], original <= 1000
 
Seen this question in a real interview before?
1/5
Yes
No
Accepted
169,859/232K
Acceptance Rate
73.2%
Topics
Array
Hash Table
Sorting
Simulation
Weekly Contest 278
icon
Companies
Hint 1
Repeatedly iterate through the array and check if the current value of original is in the array.
Hint 2
If original is not found, stop and return its current value.
Hint 3
Otherwise, multiply original by 2 and repeat the process.
Hint 4
Use set data structure to check the existence faster.
Similar Questions
Largest Number At Least Twice of Others
Easy
Check If N and Its Double Exist
Easy
''')
