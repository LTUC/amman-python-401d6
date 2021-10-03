"""
Calculator:
Your job is refactor this code to use a single calculate function that replicates behavior
"""

def calculate(a, b, operator_func):
    """
    Description of exactly what calculate does
    """
    result = operator_func(a,b)
    return f"Given {a} and {b} the result of your operation is {result}"


# lambdas are great, but sometimes worth it to make standalone function
# note the leading underscore to signal it's meant for interal use
def _max_val(a, b):
    if a > b:
        return a

    return b


if __name__ == "__main__":

    print("Add:", calculate(5, 10, lambda x,y: x + y ))

    print("Subtract:", calculate(5, 10, lambda x,y: x - y))

    print("Power Of:", calculate(2, 3, lambda x,y: x ** y))

    print("Max value", calculate(4,5, _max_val))
