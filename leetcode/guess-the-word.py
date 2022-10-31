from lc import *

class Master:
    def __init__(self, secret, words, guesses):
        self.w = secret
        self.n = guesses
        self.words = words
        self.res = None
    def guess(self, word):
        self.n -= 1
        if self.n==0:
            self.res = 'Either you took too many guesses, or you did not find the secret word.'
        if self.w == word:
            self.res = 'You guessed the secret word correctly.'
            return len(word)
        if word not in self.words: 
            return -1
        return sum(word[i]==self.w[i] for i in range(6))
    def result(self):
        return self.res

class Launcher:
    def run(self, secret, words, guesses):
        if self.init:
            init = False
            self.master = Master(secret, words, guesses)
        Solution().findSecretWord(words, self.master)
        return self.master.result()
    def __init__(self):
        self.init = True


class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:

        print('called', wordlist)

        def match(w0, w):
            return sum(w0[i]==w[i] for i in range(6))
        words = wordlist[:]
        while True:
            n = master.guess(words[0])
            if n==6:
                break
            words = [w for w in words[1:] if match(words[0], w)==n]

test('''

843. Guess the Word
Hard

1316

1578

Add to List

Share
You are given an array of unique strings words where words[i] is six letters long. One word of words was chosen as a secret word.

You are also given the helper object Master. You may call Master.guess(word) where word is a six-letter-long string, and it must be from words. Master.guess(word) returns:

-1 if word is not from words, or
an integer representing the number of exact matches (value and position) of your guess to the secret word.
There is a parameter allowedGuesses for each test case where allowedGuesses is the maximum number of times you can call Master.guess(word).

For each test case, you should call Master.guess with the secret word without exceeding the maximum number of allowed guesses. You will get:

"Either you took too many guesses, or you did not find the secret word." if you called Master.guess more than allowedGuesses times or if you did not call Master.guess with the secret word, or
"You guessed the secret word correctly." if you called Master.guess with the secret word with the number of calls to Master.guess less than or equal to allowedGuesses.
The test cases are generated such that you can guess the secret word with a reasonable strategy (other than using the bruteforce method).

 

Example 1:

Input: secret = "acckzz", words = ["acckzz","ccbazz","eiowzz","abcczz"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess, and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", words = ["hamada","khaled"], allowedGuesses = 10
Output: You guessed the secret word correctly.
Explanation: Since there are two words, you can guess both.
 

Constraints:

1 <= words.length <= 100
words[i].length == 6
words[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in words.
10 <= allowedGuesses <= 30

''', classname=Launcher)

