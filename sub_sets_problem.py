from util_decorators import timeit

# Find and print all subsets(arrays) of a given set(array)! (Given as an array.)
@timeit
def all_sub_sets(original_array):
    """
    Iterative solution - best choose
    :param original_array: given data
    :return: array of all sub set/arrays
    """
    start_index = 0
    # array of all sets
    all_sets = [[]]
    current_len = 1
    while start_index < len(original_array):
        element = original_array[start_index]
        for i in range(0, current_len):
            sub_set = all_sets[i]
            copy_set = sub_set[:]
            copy_set.append(element)
            all_sets.append(copy_set)
       # all_sets.append([element])
        start_index += 1
        current_len = len(all_sets)
    return all_sets


@timeit
def all_sub_sets_recurs(original_array):
    """
       Recursive solution - not efficient at all, twice slower than iterative solution
       :param original_array: given data
       :return: array of all sub set/arrays
       """
    subset = [None] * len(original_array)
    all_sets = []
    __helper(original_array, subset, 0, all_sets)
    return all_sets


def __helper(original_array, subset, i, all_sets):
    """

    :param original_array: given data
    :param subset: current subset
    :param i: index of recursion
    :param all_sets:
    :return:
    """
    if i == len(original_array):
        all_sets.append(subset)
    else:
        subset[i] = None
        __helper(original_array, subset[:], i + 1, all_sets)
        subset[i] = original_array[i]
        __helper(original_array, subset[:], i + 1, all_sets)


# Find and print all subsets(arrays) of a given set(array)! (Given as an array.) - where sum(sunset) = original_sum
def all_sub_sets_sum(original_array, original_sum):
    """
      Variation of all sub sets problem
      Iterative solution - best choose
      :param original_array: given data
      :return: array of all sub set/arrays
      """
    start_index = 0
    # array of all sets
    all_sets = [[]]
    current_len = 1
    while start_index < len(original_array):
        element = original_array[start_index]
        for i in range(0, current_len):
            sub_set = all_sets[i]
            copy_set = sub_set[:]
            copy_set.append(element)
            all_sets.append(copy_set)
       # all_sets.append([element])
        start_index += 1
        current_len = len(all_sets)
    return all_sets


#staircase problem!
@timeit
def all_stair_path(num_stairs, steps_array):
    """
    Another problem - stair problem, all possible paths on top of stairs, where
    possible step sizes in steps_array
    :param num_stairs: - high of stairs - total number of steps
    :param steps_array: - array(set) of  integers > 0
    :return: all_ways [][]
    """
    all_ways = []
    build_ways = [[i] for i in steps_array if i <= num_stairs]
    while len(build_ways) > 0:
        path = build_ways[0]
        build_ways.remove(path)
        temp_sum = sum(path)
        for step_i in steps_array:
            if temp_sum < num_stairs:
                new_path = path[:]
                new_path.append(step_i)
                build_ways.append(new_path)
            elif temp_sum == num_stairs:
                all_ways.append(path)
                break;
    return all_ways

# test of all_stair_path
# test_step = [1, 3, 5]
# num_stairs = 5
# # test_step = [1, 2]
# # num_stairs = 4
# print(all_stair_path(num_stairs, test_step))

# test_set = [1, 2, 3, 4, 4]
# print(test_set)
# test_set = set(test_set)
# print(test_set)
# test_set = list(test_set)

# test performance  iterative  vs. recursive solution of all_sub_sets
test_set = [i for i in range(1, 21)]
test_all_sets = all_sub_sets(test_set)
print(len(test_all_sets))
#print(test_all_sets)
test_all_sets = all_sub_sets_recurs(test_set)
print(len(test_all_sets))
#print(test_all_sets)