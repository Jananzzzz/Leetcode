"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases,
 more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
"""

# bad problem with unclear description


class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s = list(s)
        save = []
        for i in s:
            if i.lower() in vowels:
                save.append(i)
        index = 0
        for j in range(len(s)):
            if s[-j-1].lower() in vowels:
                s[-j-1] = save[index]
                index += 1
        ans = ""
        for i in s:
            ans += i
        return ans


print(Solution.reverseVowels(Solution(), s="leetcode"))

        