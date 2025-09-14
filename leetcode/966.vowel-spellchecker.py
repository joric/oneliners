from lc import *


# https://leetcode.com/problems/vowel-spellchecker/solutions/211189/java-c-python-two-hashmap/?envType=daily-question&envId=2025-09-14

class Solution:
    def spellchecker(self, w: List[str], q: List[str]) -> List[str]:
        a,b,c={x: x for x in w},{x.lower(): x for x in w[::-1]},{re.sub('[aeiou]','#',x.lower()):x for x in w[::-1]};return [a.get(x) or b.get(x.lower()) or c.get(re.sub('[aeiou]', '#', x.lower()), '') for x in q]

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        return (
            w:= {s:s for s in wordlist},
            c:= {s.lower(): s for s in wordlist[::-1]},
            v:= {(f:=lambda s:re.sub("[aeiou]", '*', s.lower()))(s): s for s in wordlist[::-1]}
        ) and [w.get(s) or c.get(s.lower()) or v.get(f(s),'') for s in queries]

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        return(p:=((lambda x:x,{}),(lambda x:x.lower(),{}),(lambda x:''.join([l if l not in set(list('aeiou')) else '*' for l in x.lower()]),{})))and [setitem(h,f(w),w) for f,h in p for w in wordlist if f(w) not in h] and [next((h[f(w)] for f,h in p if f(w) in h),'') for w in queries]

# https://leetcode.com/problems/vowel-spellchecker/solutions/7187768/swift-1-liner/?envType=daily-question&envId=2025-09-14

class Solution:
    def spellchecker(self, w: List[str], q: List[str]) -> List[str]:
        s=[lambda z:z,lambda z:z.lower(),lambda z:re.sub('[aeiou]',' ',z.lower())];m=[{f(y):y for y in w[::-1]}for f in s];return[next((d.get(f(x))for f,d in zip(s,m)if f(x) in d),'')for x in q]

test('''
966. Vowel Spellchecker
Medium

369

761

Add to List

Share
Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
When the query matches a word up to capitlization, you should return the first such match in the wordlist.
When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
If the query has no matches in the wordlist, you should return the empty string.
Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
Example 2:

Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
 

Constraints:

1 <= wordlist.length, queries.length <= 5000
1 <= wordlist[i].length, queries[i].length <= 7
wordlist[i] and queries[i] consist only of only English letters.
''')
