"""
Given two arrays of strings list1 and list2, find the common strings with the least index sumreturn min(result_list)
A common string is a string that appeared in both list1 and list2.
A common string with the least index sum is a common string such that if it appeared 
at list1[i] and list2[j] then i + j should be the minimum value among all the other common strings.
Return all the common strings with the least index sum. Return the answer in any order.
"""

class Solution:
    def findRestaurant(self, list1: list[str], list2: list[str]) -> list[str]:
        index_string_pair = []
        for i in list1:
            if i in list2:
                index_string_pair.append([list1.index(i) + list2.index(i), i])
        sorted_list = sorted(index_string_pair, key = lambda x: x[0])
        result_list = []        
        for i in sorted_list:
            if i[0] == sorted_list[0][0]:
                result_list.append(i[1])
        return result_list
        
    
test = Solution()
result = test.findRestaurant(
    list1 = ["Shogun","Tapioca Express","Burger King","KFC"], 
    list2 = ["Piatti","The Grill at Torrey Pines","KFC","Hungry Hunter Steakhouse","Shogun"]
    )
print(result)