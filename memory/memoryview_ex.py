a = bytes([i for i in range(10)])
m = memoryview(a)

print(m.tobytes())
#>>> b'\x00\x01\x02\x03\x04\x05\x06\x07\x08\t'
print(m.tolist())
#>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
