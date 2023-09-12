"""
https://leetcode.com/problems/keyboard-row/
Given an array of strings words, return the words that can be typed using letters of 
the alphabet on only one row of American keyboard like the image below.
In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
"""

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        res = []
        for i in words:
            temp = i.lower()
            for j in temp:
                for k in keyboard_rows:
                    if j in k:
                        yes = True
                        for other_letter in temp:
                            if other_letter not in k:
                                yes = False
                                break
                        if yes:
                            res.append(i)
                            break
                break
        return res

print(Solution.findWords(Solution(), words = ["Hello","Alaska","Dad","Peace"]))

        