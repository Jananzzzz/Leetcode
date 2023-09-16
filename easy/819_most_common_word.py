# https://leetcode.com/problems/most-common-word/

class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        paragraph_list = paragraph.split()
        res = ""
        max_count = 0
        for i in set(paragraph_list):
            if i not in banned:
                if paragraph_list.count(i) > max_count:
                    max_count = paragraph_list.count(i)
                    res = i
        return res
    
print(Solution.mostCommonWord(Solution(), paragraph="abc abc? abcd the jeff!", banned=["abc","abcd","jeff"]))