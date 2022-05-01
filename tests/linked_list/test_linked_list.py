
from os import link
from src.linked_lists.linked_list import LinkedList


def test_len():
    linked_list = LinkedList()

    assert len(linked_list) == 0


def test_empty():
    linked_list = LinkedList()

    assert linked_list.empty() == True


def test_push_front():
    linked_list = LinkedList()

    linked_list.push_front(10)
    linked_list.push_front(13)

    assert len(linked_list) == 2


def test_value_at():
    linked_list = LinkedList()

    linked_list.push_front(13)
    linked_list.push_front(1)
    linked_list.push_front(5)

    assert linked_list.value_at(0) == 5
    assert linked_list.value_at(1) == 1
    assert linked_list.value_at(2) == 13
    assert linked_list.value_at(-10) == None
    assert linked_list.value_at(20) == None


def test_pop_front():
    linked_list = LinkedList()

    linked_list.push_front(7)
    linked_list.push_front(10)
    linked_list.push_front(20)

    assert linked_list.pop_front() == 20
    assert linked_list.pop_front() == 10
    assert linked_list.pop_front() == 7
    assert linked_list.pop_front() == None
    assert linked_list.pop_front() == None
    assert len(linked_list) == 0


def test_push_back():
    linked_list = LinkedList()

    linked_list.push_back(10)
    linked_list.push_back(20)
    linked_list.push_back(30)

    assert linked_list.value_at(0) == 10
    assert linked_list.value_at(1) == 20
    assert linked_list.value_at(2) == 30

    assert len(linked_list) == 3


def test_pop_back():
    linked_list = LinkedList()

    linked_list.push_back(10)
    linked_list.push_back(20)
    linked_list.push_back(30)

    assert linked_list.pop_back() == 30
    assert linked_list.pop_back() == 20
    assert linked_list.pop_back() == 10
    assert linked_list.pop_back() == None


def test_front():
    linked_list = LinkedList()

    linked_list.push_back(10)
    linked_list.push_back(20)
    linked_list.push_back(30)

    assert linked_list.front() == 10

    linked_list.pop_back()
    linked_list.pop_back()
    linked_list.pop_back()

    assert linked_list.front() == None


def test_back():
    linked_list = LinkedList()

    linked_list.push_back(11)
    linked_list.push_back(12)
    linked_list.push_back(13)

    assert linked_list.back() == 13

    linked_list.pop_back()
    linked_list.pop_back()

    assert linked_list.back() == 11

    linked_list.pop_back()

    assert linked_list.back() == None


def test_insert():
    linked_list = LinkedList()

    linked_list.push_back(1)
    linked_list.push_back(3)
    linked_list.push_back(10)

    linked_list.insert(1, 2)
    linked_list.insert(10, 2)
    linked_list.insert(0, 0)
    linked_list.insert(4, 4)
    linked_list.insert(1, 14)

    assert linked_list.value_at(0) == 0
    assert linked_list.value_at(1) == 14
    assert linked_list.value_at(2) == 1


def test_erase():
    linked_list = LinkedList()

    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)
    linked_list.push_back(4)
    linked_list.push_back(5)

    assert linked_list.erase(1) == 2
    assert linked_list.value_at(1) == 3
    assert linked_list.erase(3) == 5
    assert linked_list.erase(0) == 1
    assert linked_list.erase(-10) == None
    assert linked_list.erase(100) == None


def test_remove_value():
    linked_list = LinkedList()

    linked_list.push_back(1)
    linked_list.push_back(2)
    linked_list.push_back(3)

    assert linked_list.remove_value(0) == None
    assert linked_list.remove_value(100) == None
    assert linked_list.remove_value(-45) == None

    assert linked_list.remove_value(1) == 1
    assert linked_list.remove_value(3) == 3
    assert linked_list.remove_value(2) == 2
