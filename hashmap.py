''' Hash Map pattern ที่เห็นบ่อยๆ
 Hashable : Numbers, Strings and Tuples
To track number that you''ve seen before !! 
 Pattern for Hash 
 - storing something
 - Looking for something 
 - Updating/initialise values

              Hash
Key ─────────────────→ Index
                         ↓
                    ┌──────────┐
                    │ Key Value│
                    └──────────┘
'''

my_map = {} # สมุดเปล่า ไว้จดค่าที่เข้าไปเช็ค 
data = []

for item in data: 
    if item not in my_map:
        my_map[item] = 1 
    else: 
        my_map[item] += 1 