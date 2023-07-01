class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            new_node.prev = None
            new_node.next = None
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            new_node.next = None
        self.length += 1
        return True

    def pop(self):
        if self.head is None:
            return None
        elif self.length == 1:
            self.head = self.tail = None



    def reverse(self):
        temp_b = self.tail
        while temp_b:
            print(temp_b.value)
            temp_b = temp_b.prev

