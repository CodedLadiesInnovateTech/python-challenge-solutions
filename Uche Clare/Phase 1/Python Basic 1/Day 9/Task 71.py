import os
import time

print('\n'.join(["%s %s" % (time.ctime(t),f) for t,f in
sorted([(os.path.getctime(x),x) for x in os.listdir(".")])]))