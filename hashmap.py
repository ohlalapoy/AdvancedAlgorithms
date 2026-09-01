## Hash Map pattern ที่เห็นบ่อยๆ
my_map = {}

for item in data:
    if item not in my_map:
        my_map[item] = 1
    else: 
        my_map[item] += 1