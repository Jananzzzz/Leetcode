# https://leetcode.com/problems/shortest-completing-word/description/
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        new_license = licensePlate.replace(" ", "")
        new_license.lower()
        