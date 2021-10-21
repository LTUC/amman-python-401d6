from stack_and_queue.node import Node
from stack_and_queue.queue import Queue

#1
#2
#"python"
def test_enqueue():
    queue=Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue("Python")
    actual=queue.rear.value
    expected="Python"
    assert actual == expected

def test_is_empty():
    queue=Queue()
    assert queue.is_empty() == True
    # assert queue.is_empty()