import cProfile


def sum_num():
    for i in range(2, 10, 2):
        print(i)


# https://julien.danjou.info/guide-to-python-profiling-cprofile-concrete-case-carbonara/

cProfile.run('sum_num()')
