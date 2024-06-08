from bs import *

# https://binarysearch.com/problems/Longest-Common-Substring

class Solution:
    def solve(self, a: str, b: str) -> int:
        dp=[[0 for _ in b] for _ in a]
        for i in range(len(b)):
            dp[0][i] = b[i]==a[0]
        for i in range(len(a)):
            dp[i][0] = a[i]==b[0]
        for i in range(1,len(a)):
            for j in range(1,len(b)):
                if a[i]==b[j]:
                    dp[i][j] = 1+dp[i-1][j-1]
        return max(max(r) for r in dp)

test('''
Longest Common Substring

Check if ith character in one string A is equal to jth character in string B

Case 1: both characters are same

LCS[i][j] = 1 + LCS[i-1][j-1] (add 1 to the result and remove the last character from both the strings and check the result for the smaller string.)

Case 2: both characters are not same.

LCS[i][j] = 0

At the end, traverse the matrix and find the maximum element in it, This will the length of Longest Common Substring.

https://algorithms.tutorialhorizon.com/dynamic-programming-longest-common-substring/

Examples

Input: a = "GeeksforGeeks", b = "GeeksQuiz" 
Output: 5 
Explanation:
The longest common substring is "Geeks" and is of length 5.

Input: a = "abcdxyz", b = "xyzabcd" 
Output: 4
Explanation:
The longest common substring is "abcd" and is of length 4.

Input: a = "zxabcdezy", b = "yzabcdezx" 
Output: 6 
Explanation:
The longest common substring is "abcdez" and is of length 6.
''')
