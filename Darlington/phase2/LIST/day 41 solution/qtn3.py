#program to flatten a shallow list.
import itertools
original_list = [[2,4,3],[1,5,6], [9], [7,9,0]]
second_list = [[11,12,13], [11,14,15], [16,14,15],[10,]]
new_merged_list = list(itertools.chain(*original_list))
second_merge = list(itertools.chain(*second_list))
print(new_merged_list)
print(second_merge)
print(sorted(second_merge))
