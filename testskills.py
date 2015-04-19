def sum_zero(list1):

    # all_sums = {}

    # for index, num in enumerate(list1):
    #     for next_num in list1[index + 1:]:
    #         sum = num + next_num
    #         all_sums.setdefault(sum, [])
    #         pair_list = sorted([num, next_num])
    #         all_sums[sum].append(tuple(pair_list))
    # print all_sums
           


    all_sums = set()

    for index, num in enumerate(list1):
        for next_num in list1[index + 1:]:
            sum = num + next_num
            if sum == 0:
                all_sums.add(tuple(sorted([num, next_num])))

    # return list(all_sums)


            # all_sums.setdefault(sum, [])
            # pair_list = sorted([num, next_num])
            # all_sums[sum].append(tuple(pair_list))
    print list(all_sums)           

sum_zero([1, 2, 3, -2, -1, 1, 0, 1, 0])
