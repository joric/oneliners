from lc import *

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return [w for w,_ in sorted(Counter(words).items(), key=lambda x:(-x[1],x[0]))[:k]]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(zip(*nsmallest(k, Counter(words).items(), key=lambda x:(-x[1],x[0]))))[0]
        #return [w for w,_ in nsmallest(k, Counter(words).items(), key=lambda a:(-a[1],a[0]))]
        #return [w for w,_ in sorted(Counter(words).items(), key=lambda a:(-a[1],a[0]))[:k]]

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        f=Counter(words);return nsmallest(k, f.keys(), key=lambda x:(-f[x],x))
        return (f:=Counter(words)) and nsmallest(k, f.keys(), key=lambda x:(-f[x],x))

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return list(zip(*Counter(sorted(words)).most_common(k)))[0]
        #return [w for _, w in nsmallest(k, [(-c, w) for w, c in Counter(words).items()])]
        #return (f:=Counter(words)) and nsmallest(k, f.keys(), key=lambda x:(-f[x],x))
        #return nsmallest((f:=Counter(words),k)[1], f.keys(), key=lambda x:(-f[x],x))

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return nsmallest(k, (f:=Counter(words)).keys(), key=lambda x:(-f[x],x))


test('''
692. Top K Frequent Words

Medium

Given an array of strings words and an integer k, return the k most frequent strings.

Return the answer sorted by the frequency from highest to lowest. Sort the words with the same frequency by their lexicographical order.

Example 1:

Input: words = ["i","love","leetcode","i","love","coding"], k = 2
Output: ["i","love"]
Explanation: "i" and "love" are the two most frequent words.
Note that "i" comes before "love" due to a lower alphabetical order.

Example 2:

Input: words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output: ["the","is","sunny","day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words, with the number of occurrence being 4, 3, 2 and 1 respectively.

Example 3:

Input: words = ["i","love","leetcode","i","love","coding"], k = 3
Output: ["i","love","coding"]

Constraints:

1 <= words.length <= 500
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
k is in the range [1, The number of unique words[i]]
 

Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
''')

