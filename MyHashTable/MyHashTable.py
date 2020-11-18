class MyHashTable:
    """A dummy hash table not intended  to replace a dictionary ;)"""

    def __init__(self, length = 4):
        """
        Parameters
        ----------
        length : str
            The number of buckets used for split the key-value.
        """
        self.length = length
        self.buckets = [None] * length

    def Add(self, key, value):
        """Add a key value to the hash table.

        Parameters
        ----------
        key : object
            The key of the key-value

        value : object
            The value of the key-value
        """
        index = self.GetIndex(key)
        bucket =  self.buckets[ index ]
        if(bucket is None):
            self.buckets[ index ] = [[key, value]]
        else:
            for kvp in bucket:
                if (kvp[0] == key):
                    kvp[1] = value
                    return
            self.buckets[ index ].append([key, value])

    def ContainsKey(self, key):
        """Returns if the key exists in the hash table.

        Parameters
        ----------
        key : object
            The key of the key-value to look for.
        """
        return self.Get(key) is not None

    def Get(self, key):
        """Return the value associated to the key stored in the hash table.

        Parameters
        ----------
        key : object
            The key of the key-value to look for.

        Raises
        ------
        KeyError
            If the kety is not found.
        """

        if(self.buckets[ self.GetIndex(key) ] is None): 
            raise KeyError

        for kvp in self.buckets[ self.GetIndex(key) ]:
            if (kvp[0] == key):
                return kvp[1]

        return None


    def GetIndex(self, key):
        return hash(key) % self.length       