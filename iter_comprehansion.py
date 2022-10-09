nested_list = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    [1, 2, None],
]

class NestedIter:
    def __init__(self, nested_list):
        self.start = -1
        self.nested_list = nested_list
        self.flat_list = []

    def __iter__(self):
        self.list_iter = iter(self.flat_list)

        return self

    def __next__(self):
        while nested_list:
            checked_item = nested_list.pop()
            if isinstance(checked_item, list):
                nested_list.extend(checked_item)
            else:
                self.flat_list.append(checked_item)
        sorted_flat_list = self.flat_list[::-1]
        self.start += 1
        if self.start == len(sorted_flat_list):
            raise StopIteration
        return sorted_flat_list[self.start]


if __name__ == '__main__':
    l = [item for item in NestedIter(nested_list)]
    print(l)