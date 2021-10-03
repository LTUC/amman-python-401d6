from codefellows.dsa.linked_list import LinkedList as BaseLinkedList

# possible class implementation
class LinkedList(BaseLinkedList):

    def __iter__(self):

        def value_generator():
            current = self.head
            while current:
                yield current.value
                current = current.next


        gen = value_generator()

        print(gen)

        return gen

    def traverse(self, work):
        current = self.head
        while current:

            work(current.value)

            current = current.next



linked = LinkedList(values=[3,4,5])


# multiple ways to accomplish tasks

sum = 0
product = 1
squares = []

# for num in linked:
#     sum += num
#     product *= num
#     squares.append(num**2)


# squares = [num**2 for num in linked]

# print("sum", sum)
# print("product", product)
# print("squares", squares)

linked.traverse(print)

class ThreeThingDoer:
    def __init__(self):
        self.sum = 0
        self.product = 1
        self.squares = []


    def adder(self, value):
        self.sum += value

    def multiplier(self, value):
        self.product *= value

    def squarer(self, value):
        self.squares.append(value)


doer = ThreeThingDoer()

linked.traverse(doer.adder)

print("doer sum", doer.sum)




