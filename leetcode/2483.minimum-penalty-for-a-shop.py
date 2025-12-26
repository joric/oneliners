from lc import *

# https://leetcode.com/problems/minimum-penalty-for-a-shop/solutions/3978365/one-line-with-numpy-by-patrick40-mnvz/?envType=daily-question&envId=2025-12-26

class Solution:
    def bestClosingTime(self, c: str) -> int:
        return(n:=__import__('numpy')).argmin(n.cumsum([[1,-1][c=='Y']for c in 'Y'+c]))

# https://leetcode.com/problems/minimum-penalty-for-a-shop/discuss/2851607/Python-3-oror-3-lines-wexample-oror-TM%3A-120ms19.3MB

class Solution:
    def bestClosingTime(self, c: str) -> int:
        return(a:=[*accumulate([2*(x>'N')-1 for x in c],initial=0)]).index(max(a))

class Solution:
    def bestClosingTime(self, c: str) -> int:
        t=0;return(a:=[0]+[t:=t+2*(x>'N')-1for x in c]).index(max(a))

test('''
2483. Minimum Penalty for a Shop
Medium

339

12

Add to List

Share
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

 

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
 

Constraints:

1 <= customers.length <= 10^5
customers consists only of characters 'Y' and 'N'.
''')