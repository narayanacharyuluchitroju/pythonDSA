class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    #
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            temp = self.head
            self.head = new_node
            self.head.next = temp
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None

        if self.length == 1:
            popped_element = self.head
            self.head = self.tail = None
            return popped_element

        pre = temp = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        popped_element = self.tail
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        return popped_element


    def pop_first(self):
        if self.head is None:
            print("List is empty")
            return None
        else:
            temp = self.head
            self.head = temp.next

    #
    def insert(self, index, value):
        new_node = Node(value)
        if self.length < index:
            return "Incorrect Index Value"
        elif index == 0:
            temp = self.head
            self.head = new_node
            new_node.next = temp
        else:
            pre = self.head
            temp = self.head
            act_index = 0
            while pre.next:
                # print(temp.value)
                if act_index == index:
                    pre.next = new_node
                    new_node.next = temp
                    return None
                act_index += 1
                pre = temp
                temp = temp.next

    def get(self, index):
        if self.length < index:
            return None
        elif self.length - 1 == index:
            return self.tail.value
        else:
            count = 0
            temp = self.head
            while temp.next:
                if count == index:
                    return temp.value
                count += 1
                temp = temp.next

    def set_value(self, index, value):
        new_node = Node(value)
        if self.length < index:
            return "Incorrect Index Value"
        elif self.length == 1:
            self.head = self.tail = new_node
        elif index == 0:
            temp = self.head
            self.head = new_node
            new_node.next = temp.next
        else:
            pre = self.head
            temp = self.head
            act_index = 0
            while pre.next:
                # print(temp.value)
                if act_index == index:
                    pre.next = new_node
                    if temp.next:
                        new_node.next = temp.next
                    else:
                        new_node.next = None
                        self.tail = new_node
                    return None
                act_index += 1
                pre = temp
                temp = temp.next

    def remove(self, index):
        if index < 0 or index > self.length:
            return None
        elif index == 0:
            temp = self.head
            self.head = temp.next
        else:
            pre = temp = self.head
            count = 0
            while pre.next:
                if count == index:
                    if temp.next is None:
                        pre.next = None
                    else:
                        pre.next = temp.next
                count += 1
                pre = temp
                temp = temp.next

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

    def print_list(self):
        print("List: ", end="")
        temp = self.head
        while temp:
            print(temp.value, end=" ")
            temp = temp.next
