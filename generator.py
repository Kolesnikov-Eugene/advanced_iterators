nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f'],
	[1, 2, None],
]

def gen(some_list):
    flat_list = []
    while some_list:
        checked_item = some_list.pop()
        if isinstance(checked_item, list):
            some_list.extend(checked_item)
        else:
            flat_list.append(checked_item)
    sorted_flat_list = flat_list[::-1]
    for item in sorted_flat_list:
        yield item

if __name__ == '__main__':
    for i in gen(nested_list):
        print(i)


