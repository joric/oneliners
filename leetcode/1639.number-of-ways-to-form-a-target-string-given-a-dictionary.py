from lc import *

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        return (c:=[*map(Counter,zip(*words))]) and (f:=cache(lambda i,j:i==len(target) or j<len(words[0]) and f(i,j+1)+c[j][target[i]]*f(i+1,j+1)))(0,0)%(10**9+7)

class Solution:
    def numWays(self, w: List[str], t: str) -> int:
        return (c:=[*map(Counter,zip(*w))]) and (f:=cache(lambda i,j:i==len(t) or j<len(w[0]) and f(i,j+1)+c[j][t[i]]*f(i+1,j+1)))(0,0)%(10**9+7)

test('''

1639. Number of Ways to Form a Target String Given a Dictionary
Hard

724

40

Add to List

Share
You are given a list of strings of the same length words and a string target.

Your task is to form target using the given words under the following rules:

target should be formed from left to right.
To form the ith character (0-indexed) of target, you can choose the kth character of the jth string in words if target[i] = words[j][k].
Once you use the kth character of the jth string of words, you can no longer use the xth character of any string in words where x <= k. In other words, all characters to the left of or at index k become unusuable for every string.
Repeat the process until you form the string target.
Notice that you can use multiple characters from the same string in words provided the conditions above are met.

Return the number of ways to form target from words. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: words = ["acca","bbbb","caca"], target = "aba"
Output: 6
Explanation: There are 6 ways to form target.
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
"aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
"aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
"aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
Example 2:

Input: words = ["abba","baab"], target = "bab"
Output: 4
Explanation: There are 4 ways to form target.
"bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
"bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
"bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
"bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
 

Constraints:

1 <= words.length <= 1000
1 <= words[i].length <= 1000
All strings in words have the same length.
1 <= target.length <= 1000
words[i] and target contain only lowercase English letters.
Accepted
19,967
Submissions
40,109
Seen this question in a real interview before?

Yes

No
For each index i, store the frequency of each character in the ith row.
Use dynamic programing to calculate the number of ways to get the target string using the frequency array,
''')
