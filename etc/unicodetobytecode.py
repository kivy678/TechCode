# -*- coding:utf-8 -*-

print(b"\x55\x48\x8b\x05\xb8\x13\x00\x00")
string_byte = "\\x55\\x48\\x8b\\x05\\xb8\\x13\\x00\\x00".encode()


# 가장 먼저 바이트로 인코딩
string_byte = string_byte.encode()

# 유니코드를 ISO-8859-1 로 변환
string_byte = string_byte.decode('unicode-escape').encode('ISO-8859-1')

print(string_byte)

print("Main Done...")

