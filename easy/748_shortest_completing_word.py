# https://leetcode.com/problems/shortest-completing-word/description/
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        new_license = licensePlate.replace(" ", "")
        new_license = ''.join(char for char in new_license if not char.isdigit())
        new_license = new_license.lower()
        print(new_license)
        words.sort(key=lambda x: len(x))
        
        license_table = {}
        for i in new_license:
            if i not in license_table:
                license_table[i] = new_license.count(i)
        
                
        for i in words:
            for key in license_table.keys():
                if license_table[key] > i.count(key):
                    break
                if key == list(license_table.keys())[-1]:
                    return i
            
            
print(Solution.shortestCompletingWord(Solution(),licensePlate = "1s3 PSt", words = ["step","steps","stripe","stepple"]))
            
        