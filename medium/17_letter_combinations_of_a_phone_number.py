# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        letter_table = {
            '2': "abc",
            '3': "def",
            '4': "ghi",
            '5': "jkl",
            '6': "mno",
            '7': "pqrs",
            '8': "tuv",
            '9': "wxyz",
        }
        
        def backtrack(combination: str, next_digits: str):
            if not next_digits:
                output.append(combination)
            else:
                for letter in letter_table[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])
                

        output = []
        backtrack("", digits)
        return output

            
            
        
        
        
