# https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/

# round down, so (end = mid), not need (end = mid - 1)
class Solution:
    def nextGreatestLetter(self, letters: list[str], target: str) -> str:
        if target >= letters[-1]:
            return letters[0]
        start = 0
        end = len(letters) - 1
        while(start < end):
            mid = (start + end)//2
            if letters[mid] <= target:
                start = mid + 1
            else:
                end = mid
        return letters[start]

print(Solution.nextGreatestLetter(Solution(),letters = ["c","f","j"], target = "c"))
print(Solution.nextGreatestLetter(Solution(),letters = ["c", "e", "f","j"], target = "f"))
        