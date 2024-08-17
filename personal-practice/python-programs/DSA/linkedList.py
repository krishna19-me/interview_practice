class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = None
    
    def insertAtBeginning(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def printList(self):
        temp = self.head

        while temp:
            print(temp.data, end= " ")
            temp = temp.next
        print("\n")
        
    def deleteFromBeginning(self):
        if self.head is None:
            return "List is Empty !"
        self.head = self.head.next
    
    def deleteFromEnd(self):
        if self.head is None:
            return "List is Empty!"
        if self.head.next is None:
            self.head = None
        last = self.head
        while last.next.next:
            last = last.next
        last.next = None

    def searchElement(self,value):
        current = self.head
        position = 0
        while current:
            if current.data == value:
                return f"Value {value} found at position {position}"
            current = current.next
            position +=1
        return f"Value {value} is not in the list"

if __name__ == "__main__":
    linkedlist = LinkedList()

    # linkedlist.insertAtBeginning(1)
    # linkedlist.insertAtBeginning(2)
    # linkedlist.insertAtBeginning(3)
    # linkedlist.insertAtBeginning(4)
    # linkedlist.insertAtBeginning(5)

    #5 4 3 2 1
    linkedlist.insertAtEnd(1)
    linkedlist.insertAtEnd(2)
    linkedlist.insertAtEnd(3)
    linkedlist.insertAtEnd(4)
    linkedlist.insertAtEnd(5)

    # 1 2 3 4 5

    linkedlist.printList()
    print("After Deleting an Element from beginning : \n")
    linkedlist.deleteFromBeginning()
    linkedlist.printList()
    print("After Deleting an Element at the end : \n")
    linkedlist.deleteFromEnd()
    linkedlist.printList()
    print("========================")
    linkedlist.printList()

    print(linkedlist.searchElement(3))