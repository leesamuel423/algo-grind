import random


class RandomizedSet:

    def __init__(self):
        self.values = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val not in self.map:
            self.map[val] = len(self.values)
            self.values.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        # print(self.length, self.values)
        if val not in self.map:
            return False

        index = self.map[val]
        last_valid_value = self.values[-1]

        self.values[index] = last_valid_value
        self.map[last_valid_value] = index
        del self.map[val]
        self.values.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
