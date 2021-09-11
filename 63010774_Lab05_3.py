class SinglyLinkedList :     # ทำงานเหมือนกับ List (อ้าง อินเด็กซ์แบบเดียวกัน)
    class Node :                    # โหนดเก็บข้อมูล
        def __init__(self, data, next = None) :
            self.data = data
            if next is None : self.next = None
            else : self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):                # แสดงข้อมูลทุกตัวใน linked list
        s = ''
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s
          
    def __len__(self) :               # เพิ่ม เมื่อ เติมข้อมูล  ลด เมื่อ นำข้อมูลออก
        return self.size         
            
    def isEmpty(self) :               # ตรวจสอบว่ามีข้อมูลใน linked list ไหม
        return self.size == 0
        
    def indexOf(self,data) :          # หา อินเด็กของข้อมูลว่าอยู่ที่ตำแหน่งใด
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :             # ตรวจสอบว่าใน linked list นี้ มีข้อมูลตัวนี้ไหม
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              # หาค่าตำแหน่งของโหนด เทียบกับ อินเด็กซ์
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):            # เพิ่ม ข้อมูล ไปที่ด้านท้ายของ linked list
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :                        # เพิ่ม ในกรณีที่ไม่ใช่ Node แรก
          self.insertAfter(len(self)-1,data)   #len(self) = จำนวนสมาชิก - 1 คือ index
    
    def insertAfter(self,i,data) :       #เพิ่ม ข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1
    
    def deleteAfter(self,i) :            #ลบ โหนดข้อมูล ในสายข้อมูลที่มีอยู่แล้ว
        if self.size > 0 :  # len(self)
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 #ลบข้อมูลที่ อินเด็กซ์ที่กำหนด
        if i == 0 and self.size > 0 :    #ลบตัวแรก
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)          #ลบตัวก่อนหน้า
        
    def removeData(self,data) :          #ลบข้อมูลใน linked list
        if self.isIn(data) :
            self.deleteAfter(self.indexOf(data)-1)
          
    def addHead(self,data) :
        if self.isEmpty() :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :
          p = self.Node(data,self.head)
          self.head = p
          self.size += 1

    def display(self) :
        cur = self.head
        while cur is not None :
            print(cur.data,end='')
            if cur.next is not None : print(' <- ',end='')
            cur = cur.next
        print()
    
    def add_to_linkedlist(self,string) :
        temp = ''
        i = 0
        while i < len(string) :
            if string[i] != '-' : temp += string[i]
            if string[i] == '-' and string[i+1] == '>' or i == len(string)-1 :
                self.append(temp)
                temp = ''
                i += 2
            else : i += 1

    
    def reverse(self) :
        current = self.head
        previous,next = None,None
        while current is not None :
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous


    def mergeList(self,sll) :
        cur = sll2.head
        while cur is not None :
            self.append(cur.data)
            cur = cur.next


# /////////////////////////////////////////////////
if __name__ == '__main__':
    
    sll1 = SinglyLinkedList()
    sll2 = SinglyLinkedList()
    s1,s2 = input('Enter Input (L1,L2) : ').split()
    sll1.add_to_linkedlist(s1)
    sll2.add_to_linkedlist(s2)
    print(f'L1    : {sll1}')
    print(f'L2    : {sll2}')
    sll2.reverse()
    sll1.mergeList(sll2)
    print(f'Merge : {sll1}')

    