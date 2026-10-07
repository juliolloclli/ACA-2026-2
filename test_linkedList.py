from linkedList import LinkedList

def test_insert():
    objLinkedList=LinkedList()
    objLinkedList.insert(5)
    assert objLinkedList.head.value==5
    assert objLinkedList.head.ptrNext is None

    objLinkedList.insert(10)
    objLinkedList.insert(20)
    assert objLinkedList.head.ptrNext.value==10
    assert objLinkedList.head.ptrNext.ptrNext is None

def test_getIndex():
    objLinekedlist=LinkedList()
    objLinekedlist.insert(5)
    objLinekedlist.insert(10)
    objLinekedlist.insert(20)
    objLinekedlist.insert(30)

    assert objLinekedlist.getIndex(0)==5
    assert objLinekedlist.getIndex(1)==10
    assert objLinekedlist.getIndex(2)==20
    assert objLinekedlist.getIndex(3)==30

    try:
        objLinekedlist.getIndex(4)
    except OverflowError:
        assert True
    except Exception:
        assert False

def test_delete():
    objLinekedlist=LinkedList()

    objLinekedlist.insert(5)
    objLinekedlist.insert(10)
    objLinekedlist.insert(20)
    objLinekedlist.insert(30)

    objLinekedlist.delete(5)
    assert objLinekedlist.getIndex(0)==10

    objLinekedlist.delete(20)
    assert objLinekedlist.getIndex(0)==10
    assert objLinekedlist.getIndex(0)==30

    try:
        objLinekedlist.delete(40)
    except OverflowError:
        assert True
    except Exception:
        assert False