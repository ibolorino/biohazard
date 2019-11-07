from random import random


def start_samples(affected_pairs, max_samples):
    min = 1
    max = max_samples
    sample = []
    for _ in range(0, affected_pairs):
        sample.append(scaled_random(min, max))
    return sample


def scaled_random(min, max):
    value = random()
    return min + (int(value * (max - min + 1)))


def delete_same_values(affected, poisonous, max_samples):
    for i in range(0, len(poisonous)):
        while poisonous[i] == affected[i]:
            poisonous[i] = scaled_random(1, max_samples)
    return poisonous


def set_max_min_lists(affected, poisonous):
    max_list = []
    min_list = []
    for i in range(0, len(poisonous)):
        max_list.append(max(affected[i], poisonous[i]))
        min_list.append(min(affected[i], poisonous[i]))
    min_ordered, max_ordered = order_lists(max_list, min_list)
    return min_ordered, max_ordered


def order_lists(list1, list2):
    zipped_pairs = zip(list2, list1)
    min_ordered = []
    max_ordered = []
    for x, y in sorted(zipped_pairs):
        min_ordered.append(x)
        max_ordered.append(y)
    return min_ordered, max_ordered


def delete_useless_values(list1, list2):
    values_to_delete = []
    for i in range(1, len(list1)):
        if list1[i] == list1[i-1]:
            values_to_delete.append(i)
    for i in range(0, len(values_to_delete)):
        val = values_to_delete[i]
        del (list1[val - i])
        del (list2[val - i])
    return list1, list2


def get_all_solutions(max_samples):
    solution = []
    all_solutions = []
    for k in range(1, max_samples+1):
        for i in range(k, max_samples+1):
            solution.clear()
            for j in range (k, i+1):
                solution.append(j)
                #print ("(%s, %s)" %(i,j))
            all_solutions.append(list(solution))
    return all_solutions


def get_range(num, max_samples):
    min_range = num - 1
    num = max_samples - num
    max_range = 0
    for i in range(max_samples, num, -1):
        max_range += i
    max_range -= 1
    return min_range, max_range


def get_solutions_index(num, max_samples):
    solutions_index = []
    for i in range(1, num+1):
        block_range = get_block_range(i, max_samples)
        start_range = block_range[0] + num - i
        stop_range = block_range[1]
        solutions_index.append([start_range, stop_range])
    return solutions_index


def get_block_range(num, max_samples):
    sum_max_samples = sum_all(max_samples)
    start_range = sum_max_samples - sum_all(max_samples - num + 1)
    stop_range = sum_max_samples - sum_all(max_samples - num) - 1
    return [start_range, stop_range]


def sum_all(num):
    sum = (num+1)*num/2
    return int(sum)


def get_num_coexisting_samples(all_solutions, min_list, max_list):
    return