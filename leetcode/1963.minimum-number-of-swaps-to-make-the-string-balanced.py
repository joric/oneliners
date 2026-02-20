from lc import *

# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1390193/Python-Greedy-O(n)-explained

class Solution:
    def minSwaps(self, s):
        bal, ans = 0, 0
        for symb in s:
            if symb == "[":
                bal += 1
            else:
                bal -= 1
            ans = min(bal, ans)
        return (-ans + 1)//2

# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1396109/Python-3-one-line-ridiculously-fast

class Solution:
    def minSwaps(self, s: str) -> int:
        return max(accumulate(map({'[':-1,']':1}.__getitem__,s),initial=1))//2

class Solution:
    def minSwaps(self, s: str) -> int:
        return max(accumulate([(1,-1)[c=='[']for c in s],initial=1))//2

# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/1437465/Python3-1-Line

class Solution:
    def minSwaps(self, s: str) -> int:
        return (reduce(lambda m,c:m+(-1 if (m>0 and c==']')else 1),s,0)+1)//2

class Solution:
    def minSwaps(self, s: str) -> int:
        return(reduce(lambda m,c:m+(1,-1)[m and c==']'],s,0)+1)//2

# https://leetcode.com/problems/minimum-number-of-swaps-to-make-the-string-balanced/discuss/2158554/Python-3-line-solution

class Solution:
    def minSwaps(self, s: str) -> int:
        m = 0
        for c in s:
            m = m + 1 if c == '[' else m - 1 if m > 0 else m
        return (m+1) // 2

class Solution:
    def minSwaps(self, s: str) -> int:
        m=1;[m:=m+((0,-1)[m>1],1)[c=='[']for c in s];return m//2

class Solution:
    def minSwaps(self, s: str) -> int:
        m=1;[m:=m-(m>1,-1)[c<']']for c in s];return m//2

test('''
1963. Minimum Number of Swaps to Make the String Balanced
Medium

1822

78

Add to List

Share
You are given a 0-indexed string s of even length n. The string consists of exactly n / 2 opening brackets '[' and n / 2 closing brackets ']'.

A string is called balanced if and only if:

It is the empty string, or
It can be written as AB, where both A and B are balanced strings, or
It can be written as [C], where C is a balanced string.
You may swap the brackets at any two indices any number of times.

Return the minimum number of swaps to make s balanced.

 

Example 1:

Input: s = "][]["
Output: 1
Explanation: You can make the string balanced by swapping index 0 with index 3.
The resulting string is "[[]]".
Example 2:

Input: s = "]]][[["
Output: 2
Explanation: You can do the following to make the string balanced:
- Swap index 0 with index 4. s = "[]][][".
- Swap index 1 with index 5. s = "[[][]]".
The resulting string is "[[][]]".
Example 3:

Input: s = "[]"
Output: 0
Explanation: The string is already balanced.
 

Constraints:

n == s.length
2 <= n <= 106
n is even.
s[i] is either '[' or ']'.
The number of opening brackets '[' equals n / 2, and the number of closing brackets ']' equals n / 2.
Accepted
82,110
Submissions
113,739
''')
