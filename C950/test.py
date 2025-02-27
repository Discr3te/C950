import csv
from hashmap import HashMap

with open("Data/package.csv") as package_csv:
    packages_csv = csv.reader(package_csv)
    hash_map = HashMap(41)

    for row in packages_csv:
        id = int(row[0])
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        special_note = row[7]
        delivery_status = ""
        delivery_time = ""

        package_detail = [ id, address, city, state, zip, deadline, weight, special_note, delivery_status, delivery_time ]
           
        hash_map.insert(id, package_detail)

print(hash_map.delete(2))
print(hash_map.table)