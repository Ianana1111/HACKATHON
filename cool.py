import info
class Tree:
    def __init__(self, name=None):
        self.parent = None
        self.child = None
        self.name = name
        self.degree = 0
        self.prev = None
        self.next = None


class TreeHead:
    def __init__(self):
        self.head = None
        self.tail = None


printer = None
ouo = ""

def init():
    global printer
    printer = TreeHead()


def comeon(node):
    while node is not None:
        print(node.name, end='')
        if node.child is not None:
            comeon(node.child)
        node = node.next


def bmerge(h, h2):
    new_printer = TreeHead()
    tmp1, tmp2 = h.head, h2.head

    while tmp1 is not None and tmp2 is not None:
        if tmp2.degree < tmp1.degree:
            if new_printer.head is None:
                new_printer.head = tmp2
                new_printer.tail = tmp2
            else:
                tmp2.prev = new_printer.tail
                new_printer.tail.next = tmp2
                new_printer.tail = tmp2
            tmp2 = tmp2.next
        else:
            if new_printer.head is None:
                new_printer.head = tmp1
                new_printer.tail = tmp1
            else:
                tmp1.prev = new_printer.tail
                new_printer.tail.next = tmp1
                new_printer.tail = tmp1
            tmp1 = tmp1.next

    if tmp1 is None and tmp2 is not None:
        while tmp2 is not None:
            if new_printer.head is None:
                new_printer.head = tmp2
                new_printer.tail = tmp2
            else:
                tmp2.prev = new_printer.tail
                new_printer.tail.next = tmp2
                new_printer.tail = tmp2
            tmp2 = tmp2.next
    elif tmp1 is not None and tmp2 is None:
        while tmp1 is not None:
            if new_printer.head is None:
                new_printer.head = tmp1
                new_printer.tail = tmp1
            else:
                tmp1.prev = new_printer.tail
                new_printer.tail.next = tmp1
                new_printer.tail = tmp1
            tmp1 = tmp1.next

    return new_printer


def bupdate(x, next_node):
    if x.child is not None:
        next_node.next = x.child
        x.child.prev = next_node
    else:
        next_node.next = None
    x.child = next_node
    next_node.parent = x
    next_node.prev = None
    x.degree += 1


def bunion(h, h2):
    new_printer = bmerge(h2, h)
    if new_printer.head is None:
        return new_printer

    prev = None
    x = new_printer.head
    next_node = x.next

    while next_node is not None:
        if (x.degree != next_node.degree) or (next_node.next is not None and next_node.next.degree == x.degree):
            prev = x
            x = next_node
        else:
            next_node.prev = prev
            if prev is None:
                new_printer.head = next_node
            else:
                prev.next = next_node

            bupdate(next_node, x)
            x = next_node

        next_node = x.next

    return new_printer


def binsert(name):
    global printer
    new_job = Tree(name)

    if printer.head is None:
        printer.head = new_job
        printer.tail = new_job
    else:
        tmp_tree_head = TreeHead()
        tmp_tree_head.head = new_job
        tmp_tree_head.tail = new_job
        printer = bunion(printer, tmp_tree_head)


def main():
    # rkotwkerpmgweprgmw4priogjerpgokwrp4ogjmwp4ojmgw
    wierd = info.HI # feowiafjawoeijfr
    # rpeitwjerptijkwperoktwgporgkwporgkwergwrgwoerpk[tokw]
    init()
    for char in wierd:
        binsert(char)
    tmp = printer.head
    comeon(tmp)


if __name__ == "__main__":
    main()
