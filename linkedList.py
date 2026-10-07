from node import Node

class LinkedList:
    def __init__(self):
        self.head=None

    def insert(self, x):
        node=Node(x)

        current=self.head

        if current in None:
            self.head=node
        else:
            while current.ptrNext is not None:
                current.ptrNext=node

            current.ptrNext=node

    def getIndex(self, i):
        cont=0
        current=self.head
        while cont<i and current is not None:
            current=current.ptrNext
            cont+=1
        if current is None:
            raise OverflowError

        return current.value

    def delete(self, v):
        current=self.head
        before=None

        while current is not None and current.value !=v:
            before= current
            current=current.ptrNext
        if current is None:
            raise ReferenceError

        if before is None:
            self.head = current.ptrNext

        else:
            before.ptrNext=current.ptrNext
            