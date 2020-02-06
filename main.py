from functions import start_samples, delete_same_values, set_max_min_lists, delete_useless_values, get_all_solutions, \
    get_solutions_index

max_samples = 5
affected_pairs = 1
affected = start_samples(affected_pairs, max_samples)
poisonous = start_samples(affected_pairs, max_samples)
poisonous = delete_same_values(affected, poisonous, max_samples)
min_list, max_list = set_max_min_lists(affected, poisonous)
min_list, max_list = delete_useless_values(min_list, max_list)

all_solutions = get_all_solutions(max_samples)

for i in range(0, len(all_solutions)):
   print("%s - %s" %(i, all_solutions[i]))

ranges_index = get_solutions_index(2, max_samples)
print(ranges_index)


#sadasdsadas