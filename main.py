from functions import start_samples, delete_same_values, set_max_min_lists, delete_useless_values

max_samples = 15
affected_pairs = 10
affected = start_samples(affected_pairs, max_samples)
poisonous = start_samples(affected_pairs, max_samples)
poisonous = delete_same_values(affected, poisonous, max_samples)
min_list, max_list = set_max_min_lists(affected, poisonous)
print(min_list)
print(max_list)
min_list, max_list = delete_useless_values(min_list, max_list)
print(min_list)
print(max_list)

