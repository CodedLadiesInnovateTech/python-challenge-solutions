import sys
import textwrap

module_name = ', '.join(sorted(sys.builtin_module_names))
module_name = textwrap.fill(module_name)

print(module_name)
