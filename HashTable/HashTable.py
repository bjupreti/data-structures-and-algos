class HashTable:
    def __init__(self):
        self.MAX = 10
        self.ARR = [[] for i in range(self.MAX)]
        
    def get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)
        return hash % self.MAX
    
    # def add(self, key, val):
    #     hash = self.get_hash(key)
    #     self.ARR[hash] = val
        
    # def get(self, key):
    #     hash = self.get_hash(key)
    #     return self.ARR[hash]
    
    def __setitem__(self, key, val):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.ARR[hash]):
            if len(element) == 2 and element[0] == key: # Found key in hashtable which was previously stored
                self.ARR[hash][idx] = (key, val)
                return
        self.ARR[hash].append((key, val)) # Didn't found the key so appeneding the key, value pair
    
    def __getitem__(self, key):
        hash = self.get_hash(key)
        for element in self.ARR[hash]:
            if element[0] == key:
                return element[1]
        return None
    
    def __delitem__(self, key):
        hash = self.get_hash(key)
        for idx, element in enumerate(self.ARR[hash]):
            if element[0] == key:
                del self.ARR[hash][idx]
    
stocks = HashTable()
# stocks.add('march 6', 150)
# print(stocks.get('march 6'))
stocks['march 10'] = 140
print(stocks['march 10'])
del stocks['march 10']
print(stocks['march 10'])
stocks['march 6'] = 200
stocks['march 17'] = 120
print(stocks.ARR)
del stocks['march 17']
print(stocks.ARR)