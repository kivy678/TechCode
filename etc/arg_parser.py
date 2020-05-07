# -*- coding:utf-8 -*-

import argparse

############################## argparse 예제 ############################################

parser = argparse.ArgumentParser(prog='TEST', description='Hello World')
parser.add_argument('-v', '--version', action='version', version='%(prog)s 2.0')

parser.add_argument('-a', '--a', help='경로 입력하세요.', dest='a')

parser.add_argument('-b', type=int, default=20, dest='b')
parser.add_argument('-c', action='store_const', const=20, dest='c')

parser.add_argument('-d', action='store_true', dest='d')

args = parser.parse_args()

if args is None:
    parser.print_help()
    exit()

print(args.a)
print(args.b)
print(args.c)
print(args.d)
