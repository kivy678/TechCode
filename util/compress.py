# -*- coding:utf-8 -*-

__all__=[
    'tarDecompress',
    'tarDecompressInMemory',
    'zipDecompress',
    'decompress7z',
]

##########################################################################

import shutil

import tarfile
import zipfile
import gzip
import py7zr

from io import BytesIO as BIO

from util.fsUtils import *

##########################################################################

def tarDecompress(src, drc):
    DirCheck(drc)

    try:
        with tarfile.open(src, mode='r:bz2') as tf:
            tf.extractall(drc)

        return True

    except Exception as e:
        print(e)
        return False

def tarDecompressInMemory(fp, drc):
    #fobj = BIO(fp.read())
    fobj = fp
    try:
        with tarfile.open(mode='r:bz2', fileobj=fobj) as tf:
            tf.extractall(drc)

        return True

    except Exception as e:
        print(e)
        return False

def zipDecompress(src, drc, pwd=None):
    DirCheck(drc)

    try:
        with zipfile.ZipFile(src) as zf:
            zf.extractall(drc, pwd=pwd)

        return True

    except Exception as e:
        print(e)
        return False

def decompress7z(src, drc, pwd=None):
    #DirCheck(drc)

    try:
        with py7zr.SevenZipFile(src, mode='r', password=pwd) as zf:
            zf.extractall(drc)

        return True

    except Exception as e:
        print(e)
        return False


def decompressRAR(src, drc, pwd=None):
    DirCheck(drc)

    try:
        res = sp.call([
            'RAR_PRCESS_PATH',
            "x",
            "-IBCK",
            "-INUL",
            "-o+",
            "-p-",
            src,
            drc
        ])

        if res == 0:
            return True

    except Exception as e:
        print(e)
        return False


def gzDecompress(src, drc):
    # src, drc 파일 경로
    try:
        with gzip.open(src) as gf:
            with open(drc, 'wb') as wf:
                shutil.copyfileobj(gf, wf)

        return True

    except Exception as e:
        print(e)
        return False
