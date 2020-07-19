from __future__ import print_function

s_var_names = sorted((set(globals().keys()) | set(__builtins__.__dict__.keys())) - set('_ names i'.split()))

print('\n************\n'.join(' '.join(s_var_names[i:i + 8]) for i in range(0, len(s_var_names), 8)))

# tar_var_names = globals().keys()
# print (tar_var_names)
# tar_var_names2 = __builtins__.__dict__.keys()
# print (tar_var_names2)
#
# print ("---------------------")
# var_tar_name = '_ names i'.split()
# print (var_tar_name)
