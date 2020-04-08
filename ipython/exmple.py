import sys
import idaapi
import idc
import os

from idautils import *
from idaapi import *
from idc import *

def stdout_to_file(output_file_name, output_dir=None):
    '''Set stdout to a file descriptor

    param: output_file_name: name of the file where standard output is written.
    param: output_dir: output directory for output file, default to script directory.

    Returns: output file descriptor, original stdout descriptor
    '''
    # obtain this script path and build output path
    if not output_dir:
        output_dir = os.path.dirname(os.path.realpath(__file__))

    output_file_path = os.path.join(output_dir, output_file_name)

    # save original stdout descriptor
    orig_stdout = sys.stdout

    # create output file
    f = file(output_file_path, "w")

    # set stdout to output file descriptor
    sys.stdout = f

    return f, orig_stdout

def main(args):
    # get original stdout and output file descriptor
    f, orig_stdout = stdout_to_file("output.txt")

    if idc.ARGV:
        for i, arg in enumerate(idc.ARGV):
            print "[*] arg[{}]: {}".format(i, arg)

    # call something from IDA (get the original input file name from IDB)
    print "[*] filename from IDB: {}".format(idaapi.get_root_filename())
    print("[*] done, exiting.")

    # restore stdout, close output file
    sys.stdout = orig_stdout 
    f.close()

    # exit IDA
    idc.Exit(0)

if __name__ == "__main__":
    idaapi.autoWait()
    main(sys.argv)
