''' Hash Map pattern ที่เห็นบ่อยๆ เป็นการเล่นกับ Key, values
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
    if item not in my_map: #check ว่าค่าที่เราต้องการหาอยู่ในนี้ไหม 
        my_map[item] = 1 # ถ้าไม่มีให้เอาค่าเก็บเข้า my_map เพื่อให้รอบต่อไปเข้ามาเช็คต่อ
    else: 
        my_map[item] = my_map[item] + 1  #แต่ถ้าเจอ ให้บวกเพิ่มเข้าไป เหมือนเป้นการ count สะสมค่าที่เจอ