from lc import *

# Q3. https://leetcode.com/contest/weekly-contest-388/problems/shortest-uncommon-substring-in-an-array

# https://leetcode.com/problems/shortest-uncommon-substring-in-an-array/discuss/4852537/Python-3-oror-9-lines-Find-the-substrings-and-sort-oror-TS%3A-268-ms-16.7-MB

class Solution:
    def shortestSubstrings(self, a: List[str]) -> List[str]:
        r = ['']*len(a)
        for i,s in enumerate(a):
            for w in sorted(set(s[k:j]for k,j in combinations(range(len(s)+1),2)),key=lambda x:(len(x),x)):
                if all(i==j or w not in s for j,s in enumerate(a)):
                    r[i] = w
                    break
        return r

class Solution:
    def shortestSubstrings(self, a: List[str]) -> List[str]:
        r=['']*len(a);f=lambda i,s,w:all(i==j or w not in s for j,s in enumerate(a))and[setitem(r,i,w)];[any(f(i,s,w)for w in sorted(set(s[k:j]for k,j in combinations(range(len(s)+1),2)),key=lambda x:(len(x),x)))for i,s in enumerate(a)];return r

test('''
3076. Shortest Uncommon Substring in an Array
User Accepted:7958
User Tried:9941
Total Accepted:8504
Total Submissions:21402
Difficulty:Medium
You are given an array arr of size n consisting of non-empty strings.

Find a string array answer of size n such that:

answer[i] is the shortest substring of arr[i] that does not occur as a substring in any other string in arr. If multiple such substrings exist, answer[i] should be the lexicographically smallest. And if no such substring exists, answer[i] should be an empty string.
Return the array answer.

 

Example 1:

Input: arr = ["cab","ad","bad","c"]
Output: ["ab","","ba",""]
Explanation: We have the following:
- For the string "cab", the shortest substring that does not occur in any other string is either "ca" or "ab", we choose the lexicographically smaller substring, which is "ab".
- For the string "ad", there is no substring that does not occur in any other string.
- For the string "bad", the shortest substring that does not occur in any other string is "ba".
- For the string "c", there is no substring that does not occur in any other string.
Example 2:

Input: arr = ["abc","bcd","abcd"]
Output: ["","","abcd"]
Explanation: We have the following:
- For the string "abc", there is no substring that does not occur in any other string.
- For the string "bcd", there is no substring that does not occur in any other string.
- For the string "abcd", the shortest substring that does not occur in any other string is "abcd".
 

Constraints:

n == arr.length
2 <= n <= 100
1 <= arr[i].length <= 20
arr[i] consists only of lowercase English letters.
''')
