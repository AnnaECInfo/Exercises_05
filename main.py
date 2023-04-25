# Exercise 1

def selection_sort(numbers: list):
    for fill_slot in range(0, len(numbers) - 1):
        position_of_max = fill_slot

        for location in range(fill_slot + 1, len(numbers)):
            if numbers[location] > numbers[position_of_max]:
                position_of_max = location

        temp = numbers[fill_slot]
        numbers[fill_slot] = numbers[position_of_max]
        numbers[position_of_max] = temp


# Exercise 2

def binary_search(text: list, target: str):
    first = 0
    last = len(text) - 1

    while first <= last:
        mid = (first + last) // 2
        if text[mid] == target:
            return text[mid]
        else:
            if target < text[mid]:
                last = mid - 1
            else:
                first = mid + 1


# Exercise 3


class HashTable:
    def __init__(self, data, size: int):
        self.size = size
        self.data = data
        self.slots = [None]*self.size
        self.bucket = [[] for self.slots in range(self.size)]

    # Exercise 4
    def __my_hash(self, key: int or str):
        if isinstance(key, int):
            return key % self.size
        if isinstance(key, str):
            new_key = len(key)
            return new_key % self.size

    # Exercise 5
    def put(self, key, data):
        hash_value = self.__my_hash(key)
        slot = self.slots[hash_value]
        if slot is None:
            self.slots[hash_value] = key
            self.bucket[hash_value].insert(0, data)
        else:
            self.slots[hash_value] = key
            self.bucket[hash_value].append(data)

    # Exercise 6
    def get(self, key):
        hash_value = self.__my_hash(key)
        if self.slots[hash_value] == key:
            return self.bucket[hash_value][0]
        else:
            for i in range(len(self.bucket[hash_value])):
                if self.bucket[hash_value][i] == key:
                    return self.bucket[hash_value][i]
        return None
