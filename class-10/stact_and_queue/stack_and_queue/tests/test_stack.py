from stack_and_queue.node import Node
from stack_and_queue.stack import Stack
import pytest

# 1
# 2
# "cat"
def test_push(stack):
    """

    """
    actual = stack.top.value
    expected = "cat"
    assert actual == expected

def test_pop(stack):
    """

    """
    actual = stack.pop()
    expected = "cat"
    assert actual == expected

def test_is_empty(stack):
    assert stack.is_empty() == True

def test_peek(stack):
    actual=stack.peek()
    expected='cat'
    assert actual == expected

# decorator
@pytest.fixture
def stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push("cat")

    return stack

