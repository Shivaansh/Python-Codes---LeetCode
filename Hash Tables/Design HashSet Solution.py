class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = []
        for i in range(500):
            self.hashset.append(0)
        

    def add(self, key: int) -> None:
        ind = key%500
        if(self.hashset[ind] == 0):
            newList = [key]
            self.hashset[ind] = newList
        else:
            unique = True
            for i in self.hashset[ind]:
                if(i == key):
                    unique = False
            if(unique):
                self.hashset[ind].append(key)
            
    def remove(self, key: int) -> None:
        ind = key%500
        if(self.hashset[ind] == 0):
            return
        else:
            for i in self.hashset[ind]:
                if(i == key):
                    self.hashset[ind].remove(i)
            
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        ind = key%500
        if(self.hashset[ind] == 0):
            return False
        else:
            for i in self.hashset[ind]:
                if(i == key):
                    return True
            return False