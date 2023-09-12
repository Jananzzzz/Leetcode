"""
https://leetcode.com/problems/number-of-segments-in-a-string/
Given a string s, return the number of segments in the string.
A segment is defined to be a contiguous sequence of non-space characters.

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1
"""

class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()
        s_list = s.split(' ')
        return sum([1 for i in s_list if i != ''])

print(Solution.countSegments(Solution(), s = "Hello, my name is John"))
print(Solution.countSegments(Solution(), s = ""))   # bad case
print(Solution.countSegments(Solution(), s = " 1 2 "))   # bad case
print(Solution.countSegments(Solution(), s = " "))   # bad case
print(Solution.countSegments(Solution(), s = ", , , ,        a, eaefa"))   # bad case
