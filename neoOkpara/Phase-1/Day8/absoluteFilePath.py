from __future__ import print_function


def absolute_file_path(path):
    import os
    return os.path.abspath(path)


print("Absolute file path:", absolute_file_path("distanceConvert.py"))
