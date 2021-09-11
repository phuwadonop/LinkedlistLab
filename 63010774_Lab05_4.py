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
            print(cur.data,end='')
            if cur.next is not None : print('->',end='')
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
    def isLoop(self) :
        data_temp = []
        cur = self.head
        while cur is not None :
            if cur.next in data_temp : return True
            data_temp.append(cur)
            cur = cur.next
        return False


# /////////////////////////////////////////////////
if __name__ == '__main__':
    
    lsip = input('Enter input : ').split(',')
    sll = SinglyLinkedList()
    for e in lsip :
        if e[0] == 'A' : 
            sll.append(int(e[2:]))
            sll.display()
        else :
            if sll.isEmpty() : print('Error! {}'.format("{list is empty}"))
            else :
                index,n2 = e[2:].split(':')
                index,n2 = int(index),int(n2)
                if index >= len(sll) : print('Error! {}: {}'.format("{index not in length}",index))
                elif n2 < len(sll) : 
                    print('Set node.next complete!, index:value = {}:{} -> {}:{}'.format(index,sll.nodeAt(index).data,n2,sll.nodeAt(n2).data))
                    sll.nodeAt(index).next = sll.nodeAt(n2)
                    sll.size -= abs(index-n2+1)
                else : 
                    sll.append(int(n2))
                    print(f'index not in length, append : {n2}')
         
    if sll.isLoop() : print('Found Loop')
    else : 
        print('No Loop')
        if not sll.isEmpty() : sll.display()
        else : print('Empty')