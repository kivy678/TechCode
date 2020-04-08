# -*- coding:utf-8 -*-

from idaapi import *
from idautils import *
from idc import *

def getOpcode(self):
    off_size = 4

    for funcea in Functions():
        functionName = GetFunctionName(funcea)
        opcode_list = list()
        address_list = list()
        if len(list(FuncItems(funcea))) <= off_size:
            continue
        for (startea, endea) in Chunks(funcea):
            opcode_list.append('{0};'.format(len(list(FuncItems(funcea)))))   # functionsize;
            for head in Heads(startea, endea):
                #print functionName, ":", "0x%08x"%(head), ":", GetDisasm(head)
                #Log.info('{0} : 0x{1:08x} : {2}'.format(functionName,head,GetManyBytes(head, DecodeInstruction(head)).encode('hex')))
                opcode_list.append('{0}'.format(GetManyBytes(head, self.size).encode('hex'))) # firstinstrunction
                address_list.append('{0:x};'.format(head)) # startaddress;

        yield ''.join(opcode_list) + '#' + ''.join(address_list) + '\n'

def getSection(addr):
    return SegName(SegStart(addr))
