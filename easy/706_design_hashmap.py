# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        self.hashmap = []

    def put(self, key: int, value: int) -> None:
        keys = [i[0] for i in self.hashmap]
        if key not in keys:
            self.hashmap.append([key, value])
        else:
            self.hashmap[keys.index(key)][1] = value

    def get(self, key: int) -> int:
        keys = [i[0] for i in self.hashmap]
        try:
            return self.hashmap[keys.index(key)][1]
        except:
            return -1

    def remove(self, key: int) -> None:
        keys = [i[0] for i in self.hashmap]
        try:
            self.hashmap.remove(self.hashmap[keys.index(key)])
        except:
            pass

    # def __str__(self) -> str:
    #     return str(self.hashmap)
    
    # def get_data(self):
    #     return self.hashmap

obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
print(obj.get(3))
obj.put(2, 1)
print(obj.get(2))
obj.remove(2)
print(obj.get(2))
# print(obj)
# print(obj.get_data())

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)