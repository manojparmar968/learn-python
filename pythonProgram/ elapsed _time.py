"""
Python Program to Measure the Elapsed Time in Python
"""

# import time

# start = time.time()
# end = time.time()
# print(end - start)

from timeit import default_timer as timer # timeit provides the most accurate results.

start = timer()

print(23*2.3)

end = timer()
print(end - start)