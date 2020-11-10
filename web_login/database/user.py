# -*- coding:utf-8 -*-

from collections import namedtuple

User = namedtuple("User", "id, name, passwd, admin")

Users = [
	User(0, "test1", "aaaa", 0),
	User(1, "test2", "bbbb", 0),
	User(2, "admin", "cccc", 1)
]
