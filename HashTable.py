class HashTable:
    #initalizes as a list containing 10 empty lists (or hash table with 10 buckets)
    def __init__(self, capacity=10):
        self.list = []
        for i in range(capacity):
            self.list.append([])

    #source -- WGU code repository W-2_ChainingHashTable_zyBooks_Key-Value_CSV_Greedy.py
    #Adds item to hash table
    def insert(self, key, item):
        index = hash(key) % len(self.list) #gets index of bucket for insert
        b_list = self.list[index]   #sets b_list with the list at the given index

        for kv in b_list:
            if kv[0] == key: #if the key entered matches an existing key, the item is updated
                kv[1] = item
                return True

        key_value = [key,item] #if no key matches, they key item pair is appended to b_list
        b_list.append(key_value)
        return True
    #returns an item given a corisponding key
    def search(self, key):
        index = hash(key) % len(self.list)
        b_list = self.list[index]

        for pair in b_list:
            if key == pair[0]:    #if the key matches an exising entry, the item is returned
                return pair[1]
        return None            #if the key has no match, None is returned
    #deletes a key item pair given the key
    def delete(self, key):
        index = hash(key) % len(slef.list)
        b_list = self.list[index]

        for kv in b_list: #if the key matches an existing key, the pair is removed
            if kv[0] == key:
                b_list.remove([kv[0], kv[1]])
    #prints all items in hash table
    def print_all(self):
        i = 0
        while i < len(self.list):
            bucket = self.list[i]
            if (bool(bucket)):
                for pair in bucket:
                    key = pair[0]
                    print(HashTable.search(self, key))
            i += 1

