class SinglyLinkedList :     
    class Node :                    
        def __init__(self, data, next = None) :
            self.data = data
            if next is None : self.next = None
            else : self.next = next
        
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self):                
        s = ''
        p = self.head
        while p != None :
            s += str(p.data) + ' '
            p = p.next
        return s
          
    def __len__(self) :               
        return self.size         
            
    def isEmpty(self) :               
        return self.size == 0
        
    def indexOf(self,data) :          
        p = self.head
        for i in range(len(self)) :
            if p.data == data :
                return i
            p = p.next
        return -1
            
    def isIn(self,data) :            
        return self.indexOf(data) >= 0
    
    def nodeAt(self,i) :              
        p = self.head
        for j in range(0,i) :
            p = p.next
        return p
    
    def append(self,data):            
        if self.head is None :
          p = self.Node(data)
          self.head = p
          self.size += 1
        else :                        
          self.insertAfter(len(self)-1,data)   
    
    def insertAfter(self,i,data) :       
        q = self.nodeAt(i)
        p = self.Node(data)
        p.next = q.next
        q.next = p
        self.size += 1
    
    def deleteAfter(self,i) :            
        if self.size > 0 :  
          q = self.nodeAt(i)
          q.next = q.next.next
          self.size -= 1
    
    def delete(self,i) :                 
        if i == 0 and self.size > 0 :    
          self.head = self.head.next
          self.size -= 1
        else :
          self.deleteAfter(i-1)         
        
    def removeData(self,data) :         
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
            print(cur.data,end=' ')
            cur = cur.next
        print()
    def addNum(self,data) :
        if self.isEmpty() : self.append(data)
        else : 
            cur = self.head
            x = self.size
            for i in range(self.size) :
                if data > cur.data : cur = cur.next
                else : 
                    if i == 0 : self.addHead(data)
                    else : self.insertAfter(i-1,data)
                    break
            if self.size == x : self.append(data)
    def popleft(self) :
        x = self.head
        self.head = self.nodeAt(1)
        self.size -= 1
        return x

def find_max_digit(num) :
    if num == 0 : return 1
    count = 0
    while num != 0 :
        num //= 10
        count += 1
    return count
def get_digit(num,i) :
    result = 0
    num = abs(num)
    for j in range(i) :
        result = num%10
        num //= 10
        if j == i - 1 : return int(result)
def display_list(ls) :
    s = ' -> '
    return s.join(map(str,ls))

def isSorted(ls) :
    sort_ls = sorted(ls)
    return ls == sort_ls
def toString(ls) :
    s = ' '.join(map(str,ls))
    return s

if __name__ == '__main__':
    
    ls_bucket = [ SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList(),
                  SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList(),SinglyLinkedList()
                ]
    
    lsip = [int(e) for e in input('Enter Input : ').split()]
    print('------------------------------------------------------------')
    ls = []
    for e in lsip : ls.append(e)
    max_Round = find_max_digit(max(lsip))
    Round = 0
    if isSorted(ls) :
        print('Round : 1')
        count = 1
        print('{} : {}'.format(0,toString(ls)))
        for i in range(1,10) :
            print(f'{count} : ')
            count += 1
        print('------------------------------------------------------------')
    else :
        for i in range(1,max_Round+2) :
            for e in ls : ls_bucket[get_digit(int(e),i)].addNum(int(e))
            x = ls_bucket[0].size
            print(f'Round : {i}')
            count = 0
            ls.clear()
            for e in ls_bucket :
                print(f'{count} : ',end='')
                e.display()
                size = e.size
                for i in range(size) : ls.append(int(e.popleft().data))
                count += 1
            print('------------------------------------------------------------')
            if x != len(lsip) : Round += 1
            else : break
        
    print(f'{Round} Time(s)')
    print('Before Radix Sort : {}'.format(display_list(lsip)))
    print('After  Radix Sort : {}'.format(display_list(ls)))
    
    