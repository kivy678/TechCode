# -*- coding:utf-8 -*-

##################python 3.X##################################
import configparser
import os

################################################################
if __name__ == "__main__":
    config = configparser.ConfigParser()
    print(config.sections())

    config.read(os.path.join('set', 'inin.ini'))

    print(config.sections())

    for key in config['bitbucket.org']:
        print(key)

    print('Done...')

"""
##################python 2.X##################################
import ConfigParser

################################################################
if __name__ == "__main__":
    config = ConfigParser.ConfigParser()
    config.read(os.path.join('set', 'inin.ini'))
    config.get('bitbucket.org', "User")

    print('Done...')
"""