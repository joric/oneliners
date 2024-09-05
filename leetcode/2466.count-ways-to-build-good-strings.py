from lc import *

# https://leetcode.com/problems/count-ways-to-build-good-strings/discuss/2807169/JavaC%2B%2BPython-DP-Solution

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp, mod = Counter({0: 1}), 10**9+7
        for i in range(1, high + 1):
            dp[i] = (dp[i - zero] + dp[i - one]) % mod
        return sum(dp[i] for i in range(low, high + 1)) % mod

# https://leetcode.com/problems/count-ways-to-build-good-strings/discuss/3518020/2-line-python-for-fun

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        @cache
        def dfs(curLen): return (int(low <= curLen and curLen <= high) + dfs(curLen+zero) + dfs(curLen + one)) % (10**9+7) if curLen <= high else 0
        return dfs(0)

class Solution:
    def countGoodStrings(self, l: int, h: int, z: int, o: int) -> int:
        return(f:=cache(lambda i:i<=h and((l<=i)+f(i+z)+f(i+o))%(10**9+7)))(0)

test('''
2466. Count Ways To Build Good Strings
Medium

724

68

Add to List

Share
Given the integers zero, one, low, and high, we can construct a string by starting with an empty string, and then at each step perform either of the following:

Append the character '0' zero times.
Append the character '1' one times.
This can be performed any number of times.

A good string is a string constructed by the above process having a length between low and high (inclusive).

Return the number of different good strings that can be constructed satisfying these properties. Since the answer can be large, return it modulo 109 + 7.

 

Example 1:

Input: low = 3, high = 3, zero = 1, one = 1
Output: 8
Explanation: 
One possible valid good string is "011". 
It can be constructed as follows: "" -> "0" -> "01" -> "011". 
All binary strings from "000" to "111" are good strings in this example.
Example 2:

Input: low = 2, high = 3, zero = 1, one = 2
Output: 5
Explanation: The good strings are "00", "11", "000", "110", and "011".
 

Constraints:

1 <= low <= high <= 10^5
1 <= zero, one <= low
Accepted
23,331
Submissions
45,834
Seen this question in a real interview before?

Yes

No
Climbing Stairs
Easy
Calculate the number of good strings with length less or equal to some constant x.
Apply dynamic programming using the group size of consecutive zeros and ones.
''')
