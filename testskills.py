def common_items(list1, list2):

    dict = {}
    new_list = []

    for item in list1:
        dict.setdefault(item, [])
        dict[item].append(item)
    for item in list2:
        dict.setdefault(item, [])
        new_list.extend(dict[item])

    # return []
common_items([1, 1, 2, 2], [1, 2, 3, 4])
common_items([1, 2, 3, 4], [1, 1, 2, 2])
