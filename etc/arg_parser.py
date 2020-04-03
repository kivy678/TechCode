# -*- coding:utf-8 -*-

import argparse

############################## argparse 예제 ############################################

parser = argparse.ArgumentParser(description='Hello World')
parser.add_argument('-p', '--path', help='경로 입력하세요.')

args = parser.parse_args()

if args is None:
    parser.print_help()
    exit()
