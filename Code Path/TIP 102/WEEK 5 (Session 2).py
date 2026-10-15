"""
TIP 102 - Session 2: Classes Review and Linked Lists
Problems 1-7
"""


# ---------------------------------------------------------------
# Problem 1: Mutual Friends
# ---------------------------------------------------------------
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.friends = []

    def get_mutuals(self, new_contact):
        common = []
        for friend in self.friends:
            if friend in new_contact.friends:
                common.append(friend.name)
        return common


# ---------------------------------------------------------------
# Linked list setup
# ---------------------------------------------------------------
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next


# ---------------------------------------------------------------
# Problem 2: Build a linked list by hand (see __main__ below)
# K.K. Slider -> Harriet -> Saharah -> Isabelle
# ---------------------------------------------------------------


# ---------------------------------------------------------------
# Problem 3: Daily Tasks (add to the front)
# ---------------------------------------------------------------
def add_first(head, task):
    new_node = Node(task, head)   # new node points at the old head
    return new_node               # new node is the new head


# ---------------------------------------------------------------
# Problem 4: Halve List (traverse and change each value)
# ---------------------------------------------------------------
def halve_list(head):
    current = head
    while current is not None:
        half = current.value / 2
        if half == int(half):     # show 3 instead of 3.0
            half = int(half)
        current.value = half
        current = current.next
    return head


# ---------------------------------------------------------------
# Problem 5: Remove Last (stop on the second to last node)
# ---------------------------------------------------------------
def delete_tail(head):
    if head is None:              # empty list
        return None
    if head.next is None:         # only one node
        return None

    current = head
    while current.next.next is not None:
        current = current.next
    current.next = None
    return head


# ---------------------------------------------------------------
# Problem 6: Find Min (traverse and track the smallest value)
# ---------------------------------------------------------------
def find_min(head):
    smallest = float('inf')       # any real number is smaller than infinity
    curr = head
    while curr:
        if curr.value < smallest:
            smallest = curr.value
        curr = curr.next
    return smallest


# ---------------------------------------------------------------
# Problem 7: Remove From Inventory (prev / curr pointers)
# ---------------------------------------------------------------
def delete_item(head, item):
    if head is None:
        return None
    if head.value == item:        # the match is the head
        return head.next

    prev = head
    curr = head.next              # curr stays one step ahead of prev
    while curr:
        if curr.value == item:
            prev.next = curr.next # skip over curr
            return head
        prev = curr
        curr = curr.next
    return head                   # not found, list unchanged


if __name__ == "__main__":
    print("--- Problem 1: Mutual Friends ---")
    bob = Villager("Bob", "Cat", "pthhhpth")
    marshal = Villager("Marshal", "Squirrel", "sulky")
    ankha = Villager("Ankha", "Cat", "me meow")
    fauna = Villager("Fauna", "Deer", "dearie")
    raymond = Villager("Raymond", "Cat", "crisp")
    stitches = Villager("Stitches", "Cub", "stuffin")
    bob.friends = [stitches, raymond, fauna]
    marshal.friends = [raymond, ankha, fauna]
    print(bob.get_mutuals(marshal))
    ankha.friends = [marshal]
    print(bob.get_mutuals(ankha))

    print("\n--- Problem 2: Build a Linked List ---")
    kk_slider = Node("K.K. Slider")
    harriet = Node("Harriet")
    saharah = Node("Saharah")
    isabelle = Node("Isabelle")
    kk_slider.next = harriet
    harriet.next = saharah
    saharah.next = isabelle
    print_linked_list(kk_slider)

    print("\n--- Problem 3: Daily Tasks ---")
    task_1 = Node("shake tree")
    task_2 = Node("dig fossils")
    task_3 = Node("catch bugs")
    task_1.next = task_2
    task_2.next = task_3
    print_linked_list(add_first(task_1, "check turnip prices"))

    print("\n--- Problem 4: Halve List ---")
    node_one = Node(5)
    node_two = Node(6)
    node_three = Node(7)
    node_one.next = node_two
    node_two.next = node_three
    print_linked_list(halve_list(node_one))

    print("\n--- Problem 5: Remove Last ---")
    butterfly = Node("Common Butterfly")
    ladybug = Node("Ladybug")
    beetle = Node("Scarab Beetle")
    butterfly.next = ladybug
    ladybug.next = beetle
    print_linked_list(delete_tail(butterfly))

    print("\n--- Problem 6: Find Min ---")
    head1 = Node(5, Node(6, Node(7, Node(8))))
    head2 = Node(8, Node(5, Node(6, Node(7))))
    print(find_min(head1))
    print(find_min(head2))

    print("\n--- Problem 7: Remove From Inventory ---")
    slingshot = Node("Slingshot")
    peaches = Node("Peaches")
    beetle = Node("Scarab Beetle")
    slingshot.next = peaches
    peaches.next = beetle
    print_linked_list(delete_item(slingshot, "Peaches"))
    print_linked_list(delete_item(slingshot, "Triceratops Torso"))