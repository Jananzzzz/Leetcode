"""
Given a string s and a string array dictionary, return the longest string in the dictionary 
that can be formed by deleting some of the given string characters. 
If there is more than one possible result, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:

Input: s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
Output: "apple" 
Example 2:

Input: s = "abpcplea", dictionary = ["a","b","c"]
Output: "a"
"""

class Solution:
    def findLongestWord(self, s: str, dictionary: list[str]) -> str:
        matched_list = []
        for str in dictionary:
            current = 0
            for letter in str:
                is_match = False
                for j in range(current, len(s)):
                    if letter == s[j]:
                        current = j + 1
                        is_match = True
                        break
                if not is_match:
                    break
            if is_match:
                matched_list.append(str)
        sort_list = sorted(matched_list, key = lambda x: len(x))
        short_list = [x for x in sort_list if len(x) == len(sort_list[0])]
        sort_list = sorted(short_list, key = lambda x: x, reverse=True)
        return sort_list[0] if len(sort_list) > 0 else ""
        
print(Solution.findLongestWord(Solution(), s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]))
print(Solution.findLongestWord(Solution(), s = "abpcplea", dictionary = ["alk","apple","monkey","ale","plea"]))
print(Solution.findLongestWord(Solution(), s = "abpcplea", dictionary = ["alk","apple","monkey","plea"]))
print(Solution.findLongestWord(Solution(), s = "apple", dictionary = ["zxc","vbn"]))

                
            