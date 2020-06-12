#program to check whether a given employee code is exactly 8 digits or 12 digits.
def is_valid_emp_code(emp_code):
  return len(emp_code) in [8, 12] and emp_code.isdigit()
print(is_valid_emp_code('12345678'))
print(is_valid_emp_code('1234567j'))
print(is_valid_emp_code('12345678j'))
print(is_valid_emp_code('123456789123'))
print(is_valid_emp_code('123456abcdef'))