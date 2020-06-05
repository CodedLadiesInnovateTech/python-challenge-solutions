# Write a Python program to get a list of locally installed Python modules
import pkg_resources
installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["{} == {}".format(i.key, i.version) for i in installed_packages])
for m in installed_packages_list:
    print(m)