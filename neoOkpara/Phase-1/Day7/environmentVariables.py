import os

print(os.environ['JAVA_HOME'])


for k, v in os.environ.items():
    print('{0}={1}'.format(k, v))
