from LinkedList import LinkedList

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
# (2) Items - Returns 2 Node

print(my_linked_list.pop().value)
# # (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())
