# Create Hash Map Class
class HashMap:
    def __init__(self, capacity):
        self.table = []
        for _ in range(capacity):
            self.table.append([])

    def create_hash_key(self, key):
        return int(key) % len(self.table)

    # Inserts a new item into the hash table
    # Citing source: C950-Webinar-1 Let's Go Hashing-Complete Python Code
    def insert(self, key, package_detail):
        # get the buket list where this item will go.
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]

        # Update kye if it is already in the bucket
        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = package_detail
                return True
        
        # If not, insert the item to the end of the bucket list
        details = [key, package_detail]
        bucket_list.append(details)
        return True

    # Search the hash table to find the key and remove the information associated with the key
    def delete(self, key):
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])

    # Search the hash table for the key
    def search(self, key):
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]
                
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
            return None