"""
Calculator:
Your job is refactor this code to use a single calculate function that replicates behavior
"""

def calculate(a, b, operator_func):
    """
    Exactly what calculate does
    """
    result = operator_func(a,b)
    return f"Given {a} and {b} the result of your operation is {result}"




def _add(a, b):
    result = a + b
    return f"Given {a} and {b} the result of your operation is {result}"

def _subtract(a, b):
    result = a - b
    return f"Given {a} and {b} the result of your operation is {result}"


def _multiply(a, b):
    result = a * b
    return f"Given {a} and {b} the result of your operation is {result}"


def _divide(a,b):
    result = a / b
    return f"Given {a} and {b} the result of your operation is {result}"


def _max_val(a, b):
    if a > b:
        return a

    return b


if __name__ == "__main__":
    print("Old Way")
    print('Add:', _add(5,10))
    print('Subtract:', _subtract(5,10))
    print('Multiply:', _multiply(5,10))
    print('Divide:', _divide(5,10))


    print("\n" * 3)
    print("New Way")

    print("Add:", calculate(5, 10, lambda x,y: x + y ))

    print("Subtract:", calculate(5, 10, lambda x,y: x - y))

    print("Power Of:", calculate(2, 3, lambda x,y: x ** y))

    print("Max value", calculate(4,5, _max_val))
