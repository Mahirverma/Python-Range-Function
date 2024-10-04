# Making your own range() function using generators
class My_gen:

    def __init__(self, first, last=None, step=None):
        if step is None:
            self.step = 1
            step = 1

        if last is None:
            self.first = 0
            self.last = first
        else:
            self.first = first
            self.last = last
            self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.first < self.last:
            num = self.first
            self.first = self.first + self.step
            return num
        raise StopIteration


for i in My_gen(0, 11, 3):
    print(i)
