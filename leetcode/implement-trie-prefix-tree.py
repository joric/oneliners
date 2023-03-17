from lc import *

class Trie:
    def __init__(self):
        self.root = {}
    def insert(self, word):
        reduce(lambda node, c: node.setdefault(c, {}), list(word) + [''], self.root)
    def search(self, word):
        return '' in reduce(lambda node, c: node.get(c, {}), word, self.root)
    def startsWith(self, prefix):
        return bool(reduce(lambda node, c: node.get(c, {}), prefix, self.root))

Trie = type('',(),{
    '__init__':lambda s:setattr(s,'r',{}),
    'insert':lambda s,w:reduce(lambda n,c:n.setdefault(c,{}),list(w)+[''],s.r) or None,
    'search':lambda s,w:'' in reduce(lambda n,c:n.get(c,{}),w,s.r),
    'startsWith':lambda s,p:bool(reduce(lambda n,c:n.get(c,{}),p,s.r))
})

Trie = type('',(),{'__init__':lambda s:setattr(s,'r',{}),'insert':lambda s,w:reduce(lambda n,c:n.setdefault(c,{}),list(w)+[''],s.r) or None,'search':lambda s,w:'' in reduce(lambda n,c:n.get(c,{}),w,s.r),'startsWith':lambda s,p:bool(reduce(lambda n,c:n.get(c,{}),p,s.r))})

test('''

208. Implement Trie (Prefix Tree)
Medium

9085

110

Add to List

Share
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
 

Example 1:

Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True
 

Constraints:

1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.

Accepted
747,240
Submissions
1,211,859

''', classname=Trie)

