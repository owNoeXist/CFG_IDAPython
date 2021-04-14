#coding=utf-8
import os
import sys
import json

from idc import *
from idaapi import *
from idautils import *

from CFG import GenerateCFG,get_unified_funcname,CheckInstruct
from Data import GenerateJson
from Paraments import SIGN,SAVEDIR
from Instruction import x86_I,MIPS_I

if __name__ == '__main__':
	#wait for IDA pro completing analysis
    autoWait()
    
    #analyze the disassembly code,generate cfg and feature
    file=open(SAVEDIR,'a')
    for funcSEA in Functions(SegStart(FirstSeg())):
        #Only analyze seg in .text
        segname=SegName(funcSEA)
        if segname not in ['.text']:
            continue
        #Ignore functions that gcc added 
        funcName = get_unified_funcname(funcSEA)
        if funcName in ['_start','deregister_tm_clones','register_tm_clones', '__do_global_dtors_aux','__do_global_dtors_aux','__libc_csu_fini','frame_dummy']:
            continue
        #Ignore functions that have other instruction
        funcEA = get_func(funcSEA)
        if CheckInstruct(funcEA,SIGN):
            continue
        #Generate CFG
        cfg = GenerateCFG(funcEA,SIGN)
        if len(cfg)==1:
            continue
        print funcName
        rawJson = GenerateJson(funcName, cfg)
        file.write(json.dumps(rawJson)+'\n')
    file.close()
    
    #Exit program
    idc.Exit(0)
