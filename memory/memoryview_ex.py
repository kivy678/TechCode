
#############################################################################

import time

#############################################################################

a = bytes([i for i in range(10)])
m = memoryview(a)

print(m.tobytes())
#>>> b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'
print(m.tolist())
#>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(m.hex())
#>>> 00010203040506070809

#############################################################################

a = bytearray(100000000)
start_time = time.time()

for i in range(len(a)): a[i] = 1

end_time = time.time()
secs = end_time - start_time
print(f'{secs:.3f}')

#############################################################################

m = memoryview(a)
start_time = time.time()

for i in range(len(m)): a[i] = 1

end_time = time.time()
secs = end_time - start_time
print(f'{secs:.3f}')
