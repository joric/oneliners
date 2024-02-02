from lc import *

# https://leetcode.com/problems/sequential-digits/discuss/751269/Python-3-One-Liner-for-fun

class Solution:
    def sequentialDigits(self, l: int, h: int) -> List[int]:
        return[i for i in(12,23,34,45,56,67,78,89,123,234,345,456,567,678,789,1234,2345,3456,4567,5678,6789,12345,23456,34567,45678,56789,123456,234567,345678,456789,1234567,2345678,3456789,12345678,23456789,123456789)if l<=i<=h]

# https://leetcode.com/problems/sequential-digits/discuss/1277345/Python-3-one-line-smart-binary-search

class Solution:
  def sequentialDigits(self, l: int, h: int) -> List[int]:
    r=range;return(x:=[int(''.join(map(str,r(j,i+j))))for i in r(2,10)for j in r(1,9-i+2)])[(i:=bisect_left(x,l)):bisect_left(x,h+1,i)]

# https://leetcode.com/problems/sequential-digits/discuss/451829/Python-3-(one-line)-(beats-100)

class Solution:
    def sequentialDigits(self,l: int, h: int) -> List[int]:
        return[int('123456789'[i:i+d])for d in range(len(str(l)),len(str(h))+1)for i in range(10-d)if l<=int('123456789'[i:i+d])<=h]

class Solution:
    def sequentialDigits(self, l: int, h: int) -> List[int]:
        return[x for d in range(len(str(l)),len(str(h))+1)for i in range(10-d)if l<=(x:=int('123456789'[i:i+d]))<=h]

# https://leetcode.com/problems/sequential-digits/discuss/627692/Python3-One-line-golf-solution

class Solution:
    def sequentialDigits(self, l: int, h: int) -> List[int]:
        return[s for i in range(len(str(l)),len(str(h))+1)for s in[int(''.join(str(x)for x in range(j,j+i)))for j in range(1,11-i)]if l<=s<= h]

class Solution:
    def sequentialDigits(self, l: int, h: int) -> List[int]:
        return sorted(x for i in range(9)for j in range(i+1,10)if l<=(x:=int(digits[1:][i:j]))<=h)

test('''
1291. Sequential Digits
Medium

2050

121

Add to List

Share
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]
Example 2:

Input: low = 1000, high = 13000
Output: [1234,2345,3456,4567,5678,6789,12345]
 

Constraints:

10 <= low <= high <= 10^9
Accepted
104,752
Submissions
168,367
''')
