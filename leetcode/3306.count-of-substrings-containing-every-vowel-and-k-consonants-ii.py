from lc import *

# 2404 ms
class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        result = z = count = left = 0
        ans = Counter()
        vowel = {*'aeiou'}

        for i, ch in enumerate(word):
            if ch in vowel: ans[ch] += 1
            else: 
                z += 1
                count = 0

            while z > k:
                if word[left] not in vowel:
                    z -= 1
                else:
                    ans[word[left]] -= 1
                    ans = +ans
                left += 1

            while len(ans) == len(vowel) and z == k:
                count += 1
                if word[left] in vowel:
                    ans[word[left]] -= 1
                    ans = +ans
                else:
                    z -= 1
                left += 1
            result += count
        return result

# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/6092551/python-shortest-solution-with-sidling-window-and-dp/?envType=daily-question&envId=2025-03-10

class Solution:
    def countOfSubstrings(self, word: str, k: int) -> int:
        d, start, res, dp = defaultdict(int), 0, 0, [0] * (len(word) + 1)
        for i in range(len(word) - 1, -1, -1):
            if word[i] in 'aeiou': dp[i] = 1 + dp[i + 1]
        for end, c in enumerate(word):
            d[c] += 1
            while all(d[v] >= 1 for v in 'aeiou') and (cons := (end - start + 1) - sum(d[v] for v in 'aeiou')) >= k:
                if cons == k:
                    res += (1 + dp[end+1])
                d[word[start]] -= 1
                start += 1
        return res

class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        n=len(w);p,t,c,s,r=[0]*(n+1),'aeiou',Counter(),0,0
        for i in range(n-1,-1,-1):
            if w[i] in t:
                p[i] = 1 + p[i+1]
        for e,x in enumerate(w):
            c[x] += 1
            while all(1<=c[v]for v in t)and(q:=(e-s+1)-sum(c[v]for v in t))>=k:
                if q==k:
                    r += 1+p[e+1]
                c[w[s]] -= 1
                s += 1
        return r

# 9843 ms
class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        n=len(w);p,t,c,s,r=[0]*(n+1),'aeiou',Counter(),0,0;any(setitem(p,i,p[i+1]+1)for i in range(n-1,-1,-1)if w[i]in t);any(setitem(c,x,c[x]+1)or all(all(1<=c[v]for v in t)and(q:=(e-s+1)-sum(c[v]for v in t))>=k and(q==k and(r:=r+1+p[e+1]),setitem(c,w[s],c[w[s]]-1),s:=s+1)for _ in w)for e,x in enumerate(w));return r


test('''
3306. Count of Substrings Containing Every Vowel and K Consonants II
Medium
Topics
Companies
Hint
You are given a string word and a non-negative integer k.

Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

Example 1:

Input: word = "aeioqq", k = 1

Output: 0

Explanation:

There is no substring with every vowel.

Example 2:

Input: word = "aeiou", k = 0

Output: 1

Explanation:

The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

Example 3:

Input: word = "ieaouqqieaouqq", k = 1

Output: 3

Explanation:

The substrings with every vowel and one consonant are:

word[0..5], which is "ieaouq".
word[6..11], which is "qieaou".
word[7..12], which is "ieaouq".
 

Constraints:

5 <= word.length <= 2 * 105
word consists only of lowercase English letters.
0 <= k <= word.length - 5
Seen this question in a real interview before?
1/5
Yes
No
Accepted
11.8K
Submissions
53.2K
Acceptance Rate
22.2%
Topics
Hash Table
String
Sliding Window
Companies
Hint 1
We can use sliding window and binary search.
Hint 2
For each index r, find the maximum l such that both conditions are satisfied using binary search.
Similar Questions
Longest Substring Of All Vowels in Order
Medium
Count Vowel Substrings of a String
Easy
''')
