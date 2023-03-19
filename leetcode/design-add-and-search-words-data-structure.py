from lc import *

class WordDictionary:
    def __init__(self):
        self.t = {}
    def addWord(self, word: str) -> None:
        reduce(lambda n,c:n.setdefault(c,{}),list(word)+[''],self.t)
    def search(self, word: str) -> bool:
        def f(d,c):
            a = []
            for n in d:
                if c=='.':
                    a += n.values()
                elif c in n:
                    a += [n[c]]
            return a
        return any('' in x for x in reduce(f,word,[self.t]))

WordDictionary = type('',(),{'__init__':lambda s:setattr(s,'t',{}),'addWord':lambda s,w:reduce(lambda n,c:n.setdefault(c, {}),list(w)+[''],s.t) or None,'search':lambda s,w:any('' in x for x in reduce(lambda d,c:sum(([*n.values()] if c=='.' else [n[c]] if c in n else [] for n in d),[]),w,[s.t]))})

class WordDictionary:
    def __init__(self):
        self.t = {}
    def addWord(self, word: str) -> None:
        reduce(lambda n,c:n.setdefault(c,{}),list(word)+[''],self.t)
    def search(self, word: str) -> bool:
        def f(n,i):
            if i >= len(word):
                return '' in n
            if word[i] == '.':
                return any(f(x,i+1) for x in n.values())
            if word[i] not in n:
                return False
            return f(n[word[i]],i+1)
        return f(self.t, 0)

WordDictionary = type('',(),{'__init__':lambda s:setattr(s,'t',{}),'addWord':lambda s,w:reduce(lambda n,c:n.setdefault(c, {}),list(w)+[''],s.t) or None,'search':lambda s,w:(f:=lambda n,i:'' in n if i>=len(w) else any(f(x,i+1) for x in n.values()) if w[i]=='.' else w[i] in n and f(n[w[i]],i+1))(s.t,0)})

test('''
211. Design Add and Search Words Data Structure
Medium

5902

340

Add to List

Share
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Example 2:

Input
["WordDictionary","addWord","addWord","search","search","search","search","search","search"]
[[],["a"],["a"],["."],["a"],["aa"],["a"],[".a"],["a."]]
Output
[null,null,null,true,true,false,true,false,false]

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.

Accepted
472,340
Submissions
1,098,093
''', classname=WordDictionary)
