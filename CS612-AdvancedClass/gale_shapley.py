def gale_shapley(men_prefs, women_prefs):
    """
    men_prefs: dict {man: [women เรียงจากชอบมากไปน้อย]}
    women_prefs: dict {woman: [men เรียงจากชอบมากไปน้อย]}
    """
    free_men = list(men_prefs.keys())      # ผู้ชายที่ยังไม่มีคู่
    engaged = {}                            # dict เก็บคู่ที่จับคู่แล้ว {woman: man}
    next_proposal = {man: 0 for man in men_prefs}  # index ของคนต่อไปที่แต่ละคนจะขอ

    while free_men:
        man = free_men[0]                   # หยิบผู้ชายที่ยังว่างมาคนแรก
        woman = men_prefs[man][next_proposal[man]]  # ขอผู้หญิงคนถัดไปในลิสต์ของเขา
        next_proposal[man] += 1             # ครั้งหน้าถ้าถูกปฏิเสธ จะขอคนถัดไป

        if woman not in engaged:
            # ผู้หญิงคนนี้ยังว่างอยู่ -> ตอบรับทันที
            engaged[woman] = man
            free_men.pop(0)
        else:
            current_man = engaged[woman]
            # เทียบว่าผู้หญิงชอบผู้ชายคนใหม่ หรือคนเดิมมากกว่ากัน
            if women_prefs[woman].index(man) < women_prefs[woman].index(current_man):
                # ชอบคนใหม่มากกว่า -> เปลี่ยนคู่
                engaged[woman] = man
                free_men.pop(0)
                free_men.append(current_man)   # คนเก่ากลับไปเป็นคนว่าง ต้องไปขอคนใหม่
            # ถ้าไม่ชอบคนใหม่มากกว่า -> man ยังคงว่างอยู่ ไปขอคนถัดไปในรอบหน้า

    return engaged


# ตัวอย่าง
men_prefs = {
    "A": ["X", "Y", "Z"],
    "B": ["Y", "X", "Z"],
    "C": ["Y", "Z", "X"],
}
women_prefs = {
    "X": ["B", "A", "C"],
    "Y": ["C", "A", "B"],
    "Z": ["A", "B", "C"],
}

result = gale_shapley(men_prefs, women_prefs)
print(result)
# ผลลัพธ์จะเป็น dict เช่น {'X': 'A', 'Y': 'C', 'Z': 'B'}