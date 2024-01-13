class Hashmap:
    #define hash map
    def __init__(self,size):
        self.map=[None]*self.size
        #define hash function
    def _get_hash(self, key):
        return key% self.size
    def add(self, key, value):
        #add/update key, value pairs
        key_hash=self._get_hash(key)
        key_value=[key, value]
        
        if self.map[key_hash] is None:
            self.map[key_hash]=list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0]==key:
                    pair[1]=value
                    return True
                
            self.map[key_hash].append(key_value)
            return True
    def get(self, key):
        #return value of given key
        key_hash=self._get_hash(key)
        if self.map[key_hash] is not None:
            for i in self.map[key_hash]:
                if i[0]==key:
                    return i[1]
        return None
        
                
            
        


        

