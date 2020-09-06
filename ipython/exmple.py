import sys
import idaapi
import idc
import os

from idautils import *
from idaapi import *
from idc import *



def stdout_to_file(output_file_name, output_dir=None):
    if not output_dir:
        output_dir = os.path.dirname(os.path.realpath(__file__))

    output_file_path = os.path.join(output_dir, output_file_name)

    orig_stdout = sys.stdout

    f = file(output_file_path, "w")

    sys.stdout = f
    return f, orig_stdout

def main(args):
    f, orig_stdout = stdout_to_file("output.txt")

    if idc.ARGV:
        for i, arg in enumerate(idc.ARGV):
            print "[*] arg[{}]: {}".format(i, arg)

    print "[*] filename from IDB: {}".format(idaapi.get_root_filename())

    sys.stdout = orig_stdout 
    f.close()

    idc.Exit(0)

if __name__ == "__main__":
    idaapi.autoWait()
    main(sys.argv)


