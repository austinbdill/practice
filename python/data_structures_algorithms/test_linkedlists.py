from linkedlist import *

class TestSinglyLinkedList:

    def test_init(self):
        llist = SinglyLinkedList()
        assert llist != None
        assert llist.len == 0
        
    def test_append(self):
        llist = SinglyLinkedList()
        llist.append(10)
        assert llist.head.value == 10
        assert llist.tail.value == 10
        llist.append("string")
        assert llist.head.value == 10
        assert llist.tail.value == "string"
        
    def test_count(self):
        llist = SinglyLinkedList()
        assert llist.count() == 0
        llist.append(10)
        assert llist.count() == 1
        llist.append(30)
        assert llist.count() == 2
        llist.append(-5)
        assert llist.count() == 3
        
    def test_clear(self):
        llist = SinglyLinkedList()
        llist.append(100000)
        llist.append(30)
        llist.append("test_string")
        assert llist.count() == 3
        llist.clear()
        assert llist.count() == 0
        
    def test_traverse(self, capsys):
        llist = SinglyLinkedList()
        llist.append("test_string")
        llist.traverse()
        captured = capsys.readouterr()
        assert captured.out == "test_string\n"
        llist.append(10)
        llist.traverse()
        captured = capsys.readouterr()
        assert captured.out == "test_string\n10\n"
        
    def test_extend(self, capsys):
        llist = SinglyLinkedList()
        iterable = [0, 2, -10]
        llist.extend(iterable)
        llist.traverse()
        captured = capsys.readouterr()
        assert captured.out == "0\n2\n-10\n"