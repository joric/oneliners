from lc import *

# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/6519286/c-solution-using-subset-logic/?envType=daily-question&envId=2025-03-10

class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        def f(i):
            c=p=r=0;t,d='aeiou',Counter()
            for j in range(len(w)):
                w[j] in t and[d.update(w[j])]or(c:=c+1)
                while len(d)==len(t)and c>=i:
                    r+=len(w)-j
                    w[p] in t and(d:=d+Counter({w[p]:-1}))or(c:=c-1)
                    p+=1
            return r
        return f(k)-f(k+1)

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

# 9843 ms
class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        n=len(w);p,t,c,s,r=[0]*(n+1),'aeiou',Counter(),0,0;any(setitem(p,i,p[i+1]+1)for i in range(n-1,-1,-1)if w[i]in t);any(setitem(c,x,c[x]+1)or all(all(1<=c[v]for v in t)and(q:=(e-s+1)-sum(c[v]for v in t))>=k and(q==k and(r:=r+1+p[e+1]),setitem(c,w[s],c[w[s]]-1),s:=s+1)for _ in w)for e,x in enumerate(w));return r

# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/solutions/6520375/beats-95-very-easy-java-solution-give-it-a-try/?envType=daily-question&env

class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        r,j,t,q,d=0,-1,'aeiou',deque(),{}
        for i,c in enumerate(w):
            if c in t:
                d[c] = i
            else:
                q.append(i)
                if len(q) > k:
                    j = q.popleft()
            if k==len(q)and j<min(d.get(v,-1)for v in t):
                r += min(q[0]if k else inf,*d.values())-j
        return r

# 4000 ms
class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        j,t,q,d=-1,'aeiou',deque(),{};return sum((c in t and[setitem(d,c,i)]or(q.append(i),all(k<len(q)and(j:=q.popleft())for _ in w)),(k==len(q)and j<min(d.get(v,-1)for v in t))and min(q[0]if k else inf,*d.values())-j or 0)[1]for i,c in enumerate(w))


class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        r,j,t,q,d=0,-1,'aeiou',deque(),[-1]*5
        for i,c in enumerate(w):
            if c in t:
                d[t.find(c)] = i
            else:
                q.append(i)
                if k<len(q):
                    j = q.popleft()
            if k==len(q)and j<min(d):
                r += min(q[0]if k else inf,*d)-j
        return r

# 2000 ms
class Solution:
    def countOfSubstrings(self, w: str, k: int) -> int:
        j,t,q,d=-1,'aeiou',deque(),[-1]*5;return sum(k==len(q)and j<min(d)and min(q[0]if k else inf,*d)-j for i,c in enumerate(w)if c in t and[setitem(d,t.find(c),i)]or(q.append(i),all(k<len(q)and(j:=q.popleft())for _ in w)))

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
