class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.__size = 0

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.head, str(self.head.value) + " "
        while cur.next != None:
            s += str(cur.next.value) + " "
            cur = cur.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        cur, s = self.tail, str(self.tail.value) + " "
        while cur.previous != None:
            s += str(cur.previous.value) + " "
            cur = cur.previous
        return s

    def isEmpty(self):
        return self.head == None

    def append(self, item):
        if self.isEmpty() :
            self.head = Node(item)
            self.tail = self.head
        else :
            current = self.head
            while current.next is not None :
                current = current.next
            current.next = Node(item)
            current.next.previous = self.tail
            self.tail = current.next
        self.__size += 1

    def addHead(self, item):
        new_node = Node(item)
        if not self.isEmpty() :
            new_node.next = self.head
            self.head.previous = new_node
            new_node.previous = None
        else : self.tail = new_node
        self.head = new_node
        self.__size += 1

    def insert(self, pos, item):
        new_node = Node(item)
        current = self.head
        if pos < 0 : 
            if -1*pos >= self.__size : pos = 0
            else : pos = self.__size + pos 
        if pos > self.__size - 1 : self.append(item)
        elif pos != 0 :
            count = 0
            while count < pos :
                if count == pos-1 : 
                    next = current.next
                    current.next = new_node
                    new_node.previous = current
                    next.previous = new_node
                    new_node.next = next
                current = current.next
                count += 1
            self.__size += 1
        else : self.addHead(item)

        

    def search(self, item):
        current = self.head
        while current is not None :
            if current.value == item : return "Found"
            current = current.next
        return "Not Found"

    def index(self, item):
        current = self.head
        count = 0
        while current is not None :
            if current.value == item : return count
            current = current.next
            count += 1
        return -1

    def size(self):
        return self.__size

    def pop(self, pos):
        current = self.head
        if self.isEmpty() or pos >= self.size() : return "Out of Range"
        if pos < 0 : 
                if -1*pos >= self.__size : pos = 0
                else : pos = self.__size + pos
        if pos == 0 : 
            self.head = self.head.next
            self.__size -= 1
            return "Success"
        else : 
            count = 0
            while current is not None :
                if count == pos-1 :
                    x = current
                    current.next.previous = x.previous
                    current.previous.next = x.next
                    break
                if count == pos : break
                current = current.next
                count += 1
            self.__size -= 1
            return "Success"


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())