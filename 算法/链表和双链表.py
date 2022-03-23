class Node:
    def __init__(self,element):
        self.item = element
        self.next = None
        self.piror = None

#批量创建一个头插法的单链表
def create_linklist_head(li):
    head = Node(li[0])

    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head

#创建一个尾插发的单链表
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head

#在链表中加入一个元素
def add_element(head,element,number):
    tail = head
    #找到位置
    for i in range(number - 1):
        tail = tail.next
    New_node = Node(element)
    New_node.next = tail.next
    tail.next = New_node

def remove_element(head,number):
    tail = head
    #找到位置
    for i in range(number - 1):
        tail = tail.next
    tail.next = tail.next.next
    del tail

#创建一个双链表
def create_de_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head.piror = node
        head = node
    return head

#创建一个双链表尾插发
def create_de_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        node.piror = tail
        tail = node
    return tail

#移除双链表中的一个元素
def remove_de_element(head,number):
    tail = head
    for i in range(number -1):
        tail = tail.next
    p = tail.next
    tail.next = p.next
    p.next.piror = tail
    del p

#添加一个元素
def add_de_element(head,element,number):
    tail = head
    for i in range(number - 1):
        tail = tail.next
    node = Node(element)
    node.next = tail.next
    node.next.piror = node
    node.piror = tail
    tail.next = node


#打印单链表
def print_linklist(head):
    while head:
        print(head.item,end = ',')
        head = head.next

#反向打印
def print_linklist_reverse(tail):
    while tail:
        print(tail.item,end = ',')
        tail = tail.piror


lk = create_de_linklist_head([1,2,3,4,5])
add_de_element(lk,11,2)
#remove_de_element(lk,1)
print_linklist(lk)