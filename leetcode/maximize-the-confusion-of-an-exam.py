from lc import *

# https://leetcode.com/problems/maximize-the-confusion-of-an-exam/discuss/1499049/JavaC%2B%2BPython-Sliding-Window-strict-O(n)

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        m = r = 0
        c = Counter()
        for i in range(len(s)):
            c[s[i]] += 1
            m = max(m, c[s[i]])
            if r - m < k:
                r += 1
            else:
                c[s[i-r]]-=1
        return r

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        m=r=0;c=Counter();[(c.update(s[i]),r-k<(m:=max(m,c[s[i]]))and(r:=r+1)or c.update({s[i-r]:-1}))for i in range(len(s))];return r

class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        r,c=0,Counter();[(c.update(s[i]),r-k<max(c.values())and(r:=r+1)or c.update({s[i-r]:-1}))for i in range(len(s))];return r

# bonus recursive function
class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        return (f:=lambda i,r,c:i<len(s)and f(c.update(s[i])or i+1,r+(not(r-k>=max(c.values())and[c.update({s[i-r]:-1})])),c)or r)(0,0,Counter())

# bonus Y-combinator: no semicolons, no walrus
class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        return (lambda y:lambda i,r,c:y(y,i,r,c))(lambda f,i,r,c:i<len(s)and f(f,c.update(s[i])or i+1,r+(not(r-k>=max(c.values())and[c.update({s[i-r]:-1})])),c)or r)(0,0,Counter())

# another solution
class Solution:
    def maxConsecutiveAnswers(self, s: str, k: int) -> int:
        return max(map(lambda q:max(map(sub,(z:=[i for i,x in enumerate(q+s+q)if x==q])[k+1:],z),default=len(s)+1)-1,'TF'))

test('''
2024. Maximize the Confusion of an Exam
Medium

1050

21

Add to List

Share
A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).

You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:

Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F').
Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

 

Example 1:

Input: answerKey = "TTFF", k = 2
Output: 4
Explanation: We can replace both the 'F's with 'T's to make answerKey = "TTTT".
There are four consecutive 'T's.
Example 2:

Input: answerKey = "TFFT", k = 1
Output: 3
Explanation: We can replace the first 'T' with an 'F' to make answerKey = "FFFT".
Alternatively, we can replace the second 'T' with an 'F' to make answerKey = "TFFF".
In both cases, there are three consecutive 'F's.
Example 3:

Input: answerKey = "TTFTTFTT", k = 1
Output: 5
Explanation: We can replace the first 'F' to make answerKey = "TTTTTFTT"
Alternatively, we can replace the second 'F' to make answerKey = "TTFTTTTT". 
In both cases, there are five consecutive 'T's.
 

Constraints:

n == answerKey.length
1 <= n <= 5 * 10^4
answerKey[i] is either 'T' or 'F'
1 <= k <= n
''')

