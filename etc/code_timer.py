
#############################################################################

import time
import timeit
from time import perf_counter as pc

#################################### timeit 예제 ####################################

COUNT = 1

_INIT_ = """
def _init_():
	time.sleep(2)
"""

cmd = """
time.sleep(3)
"""

#res = timeit.timeit(cmd, setup=_INIT_, number=COUNT)
#print('{:.3f}'.format(res))

res = timeit.repeat(cmd, setup=_INIT_, number=COUNT, repeat=2)
print(*('{:.3f}'.format(x) for x in res))

#>>> 3.000 3.001

################################# time 예제 ############################################

start_time = time.time()
time.sleep(3)
end_time = time.time()

secs = end_time - start_time
print(f'{secs:.3f}')

############################## perf_counter 예제 ########################################

t0 = pc()
time.sleep(3)
secs = pc() - t0
print(f'{secs:.3f}')
