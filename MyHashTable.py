class MyHashTable:
    def __init__(self, length = 10):
        self.length = length
        self.data = [None] * length

    def Add(self, key, value):
        if(self.data[ self.GetIndex(key) ] is None):
            self.data[ self.GetIndex(key) ] = [[key, value]]
        else:
            for kvp in self.data[ self.GetIndex(key) ]:
                if (kvp[0] == key):
                    kvp[1] = value
                    return
            self.data[ self.GetIndex(key) ].append([key, value])


    def ContainsKey(self, key):
        return self.Get(key) is not None

    def Get(self, key):
        if(self.data[ self.GetIndex(key) ] is None): 
            return None

        for kvp in self.data[ self.GetIndex(key) ]:
            if (kvp[0] == key):
                return kvp[1]

        return None


    def GetIndex(self, key):
        return hash(key) % self.length       


''' https://coderbook.com/@marcus/how-to-create-a-hash-table-from-scratch-in-python '''