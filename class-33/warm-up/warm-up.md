# Warm-Up Exercise

Analyze `tree_intersection` challenge from previous class for Big O time and space.

Use your own solution code, the sample code below, or both.

**NOTE:** The sample code's Tree class is *iterable*, that's why it can be used in a for loop. You'll learn about how to do that with your Tree (and other) classes soon.

```python
def tree_intersection(tree_a, tree_b):
    a_values_table = {}
    common_values = []

    for value in tree_a:
        a_values_table[value] = True

    for value in tree_b:
        if value in a_values_table:
            common_values.append(value)

    return common_values
```

## Feature Tasks

- Notice any trade offs between time and speed.
- Also analyze in terms of readability.
