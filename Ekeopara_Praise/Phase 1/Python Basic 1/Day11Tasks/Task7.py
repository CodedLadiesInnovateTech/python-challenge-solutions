'''7. Write a Python program to list the special variables used within the language.

s_var_names = sorted((set(globals().keys()) | set(___builtins__.__dict__.keys())) - set('_ names i'. split()))
print('\n'.join(' '.join(s_var_name[i:i+8]) for i in range(0, len(s_var_name), 8)))'''
