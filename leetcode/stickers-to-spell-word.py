from lc import *

# https://leetcode.com/problems/stickers-to-spell-word/discuss/2155647/Python.-LRU-cache....

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d=[*map(Counter,s)]
        @cache
        def f(s):
            k=(c:=Counter(s)).keys()
            return s and min(s!=(r:=reduce(lambda a,i:a+i*max(0,c[i]-w[i]),k,''))and 1+f(r)or inf for w in d)or 0
        return(r:=f(t),-1)[r==inf]

class Solution:
    def minStickers(self, s: List[str], t: str) -> int:
        d,f=[*map(Counter,s)],cache(lambda s:s and(k:=(c:=Counter(s)).keys())and min(s!=(r:=reduce(lambda a,i:a+i*max(0,c[i]-w[i]),k,''))and 1+f(r)or inf for w in d)or 0);return(r:=f(t),-1)[r==inf]

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

