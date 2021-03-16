import os
import sys
import json

from idc import *
from idaapi import *
from idautils import *

from CFG import *
from Data import GenerateJson

if __name__ == '__main__':
	#wait for completing analysis
    autoWait()
    #Read paraments from file
    file=open("C:/Users/nocan/Desktop/CEC/BinaryAnalyze/Paraments",'rb')
    sign=int(file.readline()[0])
    path=file.readline()
    file.close()
    print("{0}\n{1}".format(sign,path))
    
    #analyze the disassembly code,generate cfg and feature
    file=open(path,'a')
    for func_sea in Functions(SegStart(FirstSeg())):
        #Only analyze seg in .text
        segname=SegName(func_sea)
        if segname not in ['.text']:
            continue
        #Ignore functions that gcc added 
        func_name = get_unified_funcname(func_sea)
        if func_name in ['_start','deregister_tm_clones','register_tm_clones', '__do_global_dtors_aux','__do_global_dtors_aux','__libc_csu_fini','frame_dummy']:
            continue
        print func_name
        #Generate CFG and feature
        func_ea = get_func(func_sea)
        '''
        if CheckInstruct(func_ea,sign):
            continue
        '''
        func_cfg = GenerateCFG(func_ea,sign)
        if len(func_cfg)==1:
            continue
        raw_json = GenerateJson(func_name, func_cfg, sign)
        file.write(json.dumps(raw_json))
        file.write('\n')
    file.close()
    
    #Exit program
    idc.Exit(0)