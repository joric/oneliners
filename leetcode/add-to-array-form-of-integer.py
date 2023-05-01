from lc import *

# ValueError: Exceeds the limit (4300) for integer string conversion: value has 10000 digits; use sys.set_int_max_str_digits() to increase the limit
class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return map(int,str(int(''.join(map(str,num)))+k))

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        for i in range(len(num) - 1, -1, -1):
            k, num[i] = divmod(num[i] + k, 10)
        return [int(i) for i in str(k)] + num if k else num

class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        return (all((d:=divmod(num[i]+k,10),k:=d[0],setitem(num,i,d[1])) for i in reversed(range(len(num)))),[int(i) for i in str(k)]+num if k else num)[1]

test('''

989. Add to Array-Form of Integer
Easy

2098

189

Add to List

Share
The array-form of an integer num is an array representing its digits in left to right order.

For example, for num = 1321, the array form is [1,3,2,1].
Given num, the array-form of an integer, and an integer k, return the array-form of the integer num + k.

 

Example 1:

Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234
Example 2:

Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455
Example 3:

Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021
 

Constraints:

1 <= num.length <= 10^4
0 <= num[i] <= 9
num does not contain any leading zeros except for the zero itself.
1 <= k <= 10^4
''')

