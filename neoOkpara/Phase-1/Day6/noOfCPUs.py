import os


def check_count():
    # Python 2.6+
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except (ImportError, NotImplementedError):
        pass

    # https://github.com/giampaolo/psutil
    try:
        import psutil
        return psutil.cpu_count()   # psutil.NUM_CPUS on old versions
    except (ImportError, AttributeError):
        pass

    # POSIX
    try:
        import os
        res = int(os.sysconf('SC_NPROCESSORS_ONLN'))

        if res > 0:
            return str(res) + ' - POSIX'
    except (AttributeError, ValueError):
        pass

    # Windows
    try:
        import os
        res = int(os.environ['NUMBER_OF_PROCESSORS'])

        if res > 0:
            return str(res) + ' - Windows'
    except (KeyError, ValueError):
        pass

    # jython
    try:
        from java.lang import Runtime
        runtime = Runtime.getRuntime()
        res = runtime.availableProcessors()
        if res > 0:
            return str(res) + ' - jython'
    except ImportError:
        pass
    raise Exception('Can not determine number of CPUs on this system')


resp = check_count()
print("Number of CPUs in the system: " + resp)
