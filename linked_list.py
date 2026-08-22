""" linked_list.py
    ตัวอย่างการสร้าง linked list แบบง่าย ๆ
    โดยใช้ class Node และ class LinkedList
    เพิ่มความเข้าใจเกี่ยวกับ linked list และการทำงานงับ


    Singly list ชี้ไปทางเดียว Head --> A ---> B ---> C
    Doubly list ที่ชี้ไปสองทาง Head ---> A ---> B ---> C
                           Head <--- A <--- B <--- C
"""
class Node:
    """
    Node ประกอบด้วย data และ pointer (next) ที่ชี้ไปยัง node ถัดไป
    ดังนั้นต้องสร้าง Object ของ Node ก่อนที่จะสร้าง linked list
    ต้องมี 2 attribute คือ data และ next
    อ่านเพิ่มกันลืมมมจ๊ะะ : https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/
    """

    def __init__(self, data):
        self.data = data
        self.next = None   # ยังไม่ชี้ไปไหน (ตัวถัดไป)
        
    def __repr__(self):
        return "<Node data: %s>" % self.data # replace % with self.data

class LinkedList:
    def __init__(self):
        self.head = None   # จุดเริ่มต้น ชี้ไป node แรก

    def add(self, data):
        """ เพิ่ม node ใหม่ที่จุดท้ายของ linked list 
            takes O(n) time complexity
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next is not None:   # ไล่หา node สุดท้าย
            current = current.next
        current.next = new_node           # ไป node ถัดไป วนจนกว่า current.next เป็น None

    """
    head -> node1 -> node2 -> node3 -> None
    ใส่ตัวแรกไปเช็คก่อนว่า ถ้า head เป็น None ให้ head ชี้ไป node ใหม่
    ถ้า head ไม่เป็น None ให้ไล่หา node สุดท้าย (current.next is not None) จะไปรัน current = current.next เพื่อบอกว่าไป Node ถัดไป
    พอเจอว่า อ่อ current.next ที่วนไปเรื่อยๆตอนนี้เจอ None แล้ว จะรัน ---> (current.next = new_node) เพื่อบอกว่า งั้น Node ถัดไปของ current ให้ชี้ไป node ใหม่ (new_node)
    1. สร้าง node ใหม่ (new_node = Node(data))
    """

    def print_list(self):
        current = self.head
        while current is not None:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def add_at_beginning(self, data):
        """ เพิ่ม node ใหม่ที่จุดเริ่มต้นของ linked list 
            takes O(1) time complexity
        """
        new_node = Node(data)
        new_node.next = self.head # point new_node.next ไปที่ node แรก (self.head)
        self.head = new_node ## เปลี่ยน self.head ให้ชี้ไปที่ node ใหม่ (new_node)

    def search(self, key):
        """ ค้นหา node ที่มีค่า data เท่ากับ key
            takes O(n) time complexity
        """
        current = self.head
        while current:
            if current.data == key:
                return current
            else :
                current = current.next
        return None

    def delete(self, key):
        """ ลบ node ที่มีค่า data เท่ากับ key
            takes O(n) time complexity
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head: #ถ้าตัวที่จะลบคือ node แรก (head)
                found = True # set found = True เพื่อออกจาก loop  ครั้งถัดไป 
                self.head = current.next # Remove แล้วให้เปลี่ยน head ให้ชี้ไป node ถัดไป (current.next)
            elif current.data == key:
                found = True
                previous.next = current.next # Remove แล้วให้เปลี่ยน previous.next(node ก่อนหน้า )ให้ชี้ไป node ถัดไป (current.next)
            else:
                previous = current # set previous = current เพื่อให้ previous ชี้ไป node ก่อนหน้า 
                current = current.next # เหมือนเป้นการเปลี่ยนตำแหน่ง current ไปเรื่อยๆจนกว่าจะเจอ current == key 
        return current


    def insert(self, index, data):
        """ แทรก node ใหม่ที่ตำแหน่ง index
            takes O(n) time complexity
        """
        if index < 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.add_at_beginning(data)
            return

        new_node = Node(data)
        current = self.head
        position = index

        while position > 1 and current is not None:
            current = current.next
            position -= 1

        if current is None:
            raise IndexError("Index out of bounds")

        new_node.next = current.next
        current.next = new_node

'''
เวลาเขียนลองนึกภาพ step by step เพราะ Computer ไม่รู้ว่าเราจะให้ทำอะไรบ้าง
ดังนั้นทุกๆ step จะต้อง Precise แบบ indetails และ repeat ซ้ำได้ 
ทริคง่ายสุดคือ ลองวาดภาพออกมาแล้วจะเขียนง่ายขึ้น 
'''