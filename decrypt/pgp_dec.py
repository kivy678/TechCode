# -*- coding:utf-8 -*-

import pgpy
import py7zr


emsg = pgpy.PGPMessage.from_file("Encrypt file path")
key, _ = pgpy.PGPKey.from_file("private key file path")

with key.unlock("input Passphrase key"):
	with open("Save path", 'wb') as fw:
		fw.write(key.decrypt(emsg).message)


with py7zr.SevenZipFile("src", mode='r', password='pass') as z:
	z.extractall("drc")
