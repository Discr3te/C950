class HashMap:
    def __init__(self, capacity):
        self.table = []
        for _ in range(capacity):
            self.table.append([])

    def create_hash_key(self, key):
        return int(key) % len(self.table)

    def insert(self, key, package_detail):
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]

        for key_value in bucket_list:
            if key_value[0] == key:
                key_value[1] = package_detail
                return True
        details = [key, package_detail]
        bucket_list.append(details)
        return True

    def delete(self, key):
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]

        for key_value in bucket_list:
            if key_value[0] == key:
                bucket_list.remove([key_value[0], key_value[1]])

    def search(self, key):
        key_hash = self.create_hash_key(key)
        bucket_list = self.table[key_hash]
                
        for key_value in bucket_list:
            if key_value[0] == key:
                return key_value[1]
            return None