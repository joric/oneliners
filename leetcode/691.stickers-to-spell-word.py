from lc import *

class Solution(object):
    def minStickers(self, stickers, target):
        t_count = Counter(target)
        A = [Counter(sticker) & t_count
             for sticker in stickers]

        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)

        self.best = len(target) + 1
        def search(ans = 0):
            if ans >= self.best: return
            if not A:
                if all(t_count[letter] <= 0 for letter in t_count):
                    self.best = ans
                return

            sticker = A.pop()
            used = max((t_count[letter] - 1) // sticker[letter] + 1
                        for letter in sticker)
            used = max(used, 0)

            for c in sticker:
                t_count[c] -= used * sticker[c]

            search(ans + used)
            for i in range(used - 1, -1, -1):
                for letter in sticker:
                    t_count[letter] += sticker[letter]
                search(ans + i)

            A.append(sticker)

        search()
        return self.best if self.best <= len(target) else -1

class Solution(object):
    def minStickers(self, stickers, target):
        t_count = Counter(target)
        A = [Counter(sticker) & t_count
             for sticker in stickers]
        for i in range(len(A) - 1, -1, -1):
            if any(A[i] == A[i] & A[j] for j in range(len(A)) if i != j):
                A.pop(i)
        stickers = ["".join(s_count.elements()) for s_count in A]
        dp = [-1] * (1 << len(target))
        dp[0] = 0
        for state in range(1 << len(target)):
            if dp[state] == -1: continue
            for sticker in stickers:
                now = state
                for letter in sticker:
                    for i, c in enumerate(target):
                        if (now >> i) & 1: continue
                        if c == letter:
                            now |= 1 << i
                            break
                if dp[now] == -1 or dp[now] > dp[state] + 1:
                    dp[now] = dp[state] + 1
        return dp[-1]

# https://leetcode.com/problems/stickers-to-spell-word/discuss/2155647/Python.-LRU-cache....

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d=[*map(Counter,s)]
        @cache
        def f(s):
            c=Counter(s)
            return s and min(s!=(r:=''.join(k*max(0,c[k]-w[k])for k in c))and 1+f(r)or inf for w in d)or 0
        return(r:=f(t),-1)[r==inf]

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d,f=[*map(Counter,s)],cache(lambda s:s and(c:=Counter(s))and min(s!=(r:=''.join(k*max(0,c[k]-w[k])for k in c))and 1+f(r)or inf for w in d)or 0);return(r:=f(t),-1)[r==inf]

# counter diff (2x slower)

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d = [*map(Counter,s)]
        f = cache(lambda s:(c:=Counter(s))and min(s!=(r:=''.join((c-w).elements()))and 1+f(r)or inf for w in d)or 0)
        return(-1,r:=f(t))[r<inf]

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d,f=[*map(Counter,s)],cache(lambda s:(c:=Counter(s))and min(s!=(r:=''.join((c-w).elements()))and 1+f(r)or inf for w in d)or 0);return(-1,r:=f(t))[r<inf]

# borderline TLE (8s)

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        return(-1,r:=(f:=cache(lambda x:x and min(x!=(r:=''.join((Counter(x)-Counter(w)).elements()))and 1+f(r)or inf for w in s)or 0))(t))[r<inf]

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        c=Counter;return(-1,r:=(f:=cache(lambda x:x and min(x!=(r:=''.join((c(x)-c(w)).elements()))and 1+f(r)or inf for w in s)or 0))(t))[r<inf]

test('''
691. Stickers to Spell Word
Hard

1148

92

Add to List

Share
We are given n different types of stickers. Each sticker has a lowercase English word on it.

You would like to spell out the given string target by cutting individual letters from your collection of stickers and rearranging them. You can use each sticker more than once if you want, and you have infinite quantities of each sticker.

Return the minimum number of stickers that you need to spell out target. If the task is impossible, return -1.

Note: In all test cases, all words were chosen randomly from the 1000 most common US English words, and target was chosen as a concatenation of two random words.

 

Example 1:

Input: stickers = ["with","example","science"], target = "thehat"
Output: 3
Explanation:
We can use 2 "with" stickers, and 1 "example" sticker.
After cutting and rearrange the letters of those stickers, we can form the target "thehat".
Also, this is the minimum number of stickers necessary to form the target string.
Example 2:

Input: stickers = ["notice","possible"], target = "basicbasic"
Output: -1
Explanation:
We cannot form the target "basicbasic" from cutting letters from the given stickers.
 

Constraints:

n == stickers.length
1 <= n <= 50
1 <= stickers[i].length <= 10
1 <= target.length <= 15
stickers[i] and target consist of lowercase English letters.
Accepted
54,964
Submissions
115,513
''')
