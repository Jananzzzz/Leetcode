# https://leetcode.com/problems/unique-morse-code-words/description/

class Solution:
    def uniqueMorseRepresentations(self, words: list[str]) -> int:
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        words_to_morse = []
        for i in words:
            morse = ""
            for j in i:
                morse += morse_code[ord(j) - ord('a')]
            words_to_morse.append(morse)

        return len(set(words_to_morse))