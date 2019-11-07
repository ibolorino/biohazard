from random import random


def start_samples(order, max_samples):
    min = 1
    max = max_samples
    sample = []
    for _ in range(0, order):
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
