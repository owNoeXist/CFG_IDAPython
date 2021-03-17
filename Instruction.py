SIGN = 0
SAVEDIR = 'C:\\Users\\nocan\\Desktop\\DataX86-O0.json'
#------------------------------------------------------------------------------------------------------------------
#0.transfer 1.arithmetical 2.logical 3.string-solve 4.jump 5.call 6.CPU-resolve 7.other 8.return
#------------------------------------------------------MIPS Framework----------------------------------------------
MIPS_I = {'move':0,'movf':0,'movt':0,'movn':0,'movz':0,
        'la':0,'li':0,'lui':0,
        'sb':0,'sh':0,
        'lb':0,'lbu':0,
        'ld':0,'ldl':0,'ldr':0,
        'lw':0,'lwl':0,'lwr':0,
        'sd':0,'sdl':0,'sdr':0,
        'sw':0,'swl':0,'swr':0,
        'lh':0,'lhu':0, 
        'lw':0,'lwu':0,
        'mfhi':0,'mflo':0,'mthi':0,'mtlo':0,

        'add':1, 'addu':1, 'addi':1,'addiu':1,'add.s':1,'add.d':1,
        'sub':1,'subu':1,'sub.s':1,'sub.d':1,
        'mul':1,'mult':1,'multu':1,'mul.s':1,'mul.d':1,
        'div':1,'divu':1,'div.s':1,'div.d':1,
        'madd':1,'maddu':1,'msub':1,'msubu':1,
        'teq':1,'clo':1,'clz':1,
        'slt':1,'slti':1,'sltiu':1,'sltu':1,
        'abs.s':1,'abs.d':1,'neg.s':1,'neg.d':1,
        
        'and':2,'andi':2,'nor':2,'or':2,  'ori':2,'xor':2,'xori':2,
        'sll':2,'sllv':2,'sra':2,'srav':2,'srl':2,'srlv':2,

        'j':4,'b':4,
        'bc0f':4,'bc0fl':4,'bc0t':4,'bc0tl':4,
        'bc1f':4,'bc1fl':4,'bc1t':4,'bc1tl':4,
        'bc2f':4,'bc2fl':4,'bc2t':4,'bc2tl':4,
        'beq':4,'beql':4,'beqz':4,'beqzl':4,
        'bge':4,'bgel':4,'bgez':4,'bgezl':4,'bgeu':4,'bgeul':4,
        'bgt':4,'bgtl':4,'bgtz':4,'bgtzl':4,'bgtu':4,'bgtul':4,
        'ble':4,'blel':4,'blez':4,'blezl':4,'bleu':4,'bleul':4,
        'blt':4,'bltl':4,'bltz':4,'bltzl':4,'bltu':4,'bltul':4,
        'bne':4,'bnel':4,'bnez':4,'bnezl':4,
    
        'jal':5, 'jalr':5,'bal':5,'jr':8,
        'bgezal':5,'bgezall':5,'bltzal':5,'bltzall':5,

        'nop':6,'ssnop':6
}

#------------------------------------------------------x86 Framework-----------------------------------------------
x86_I = {'mov':0,'movsx':0,'movsxd':0,'movzx':0,'movbe':0,
        'xchg':0,'cmpxchg':0,'cmpxchg8b':0,'xlat':0,'xgetbv':0,'bswap':0,
        'push':0,'pusha':0,'pushad':0,'pop':0,'popa':0,'popad':0,
        'lea':0,'lds':0,'les':0,'lfs':0,'lgs':0,'lss':0,
        'pushf':0,'pushfq':0,'pushfd':0,'popf':0, 'popfq':0, 'popfd':0,'lahf':0,'sahf':0,
        'in':0,'ins':0,'insb':0,'insw':0,'insd':0,
        'out':0,'outs':0,'outsb':0,'outsw':0,'outsd':0,
        'cmove':0,'cmovz':0,'cmovne':0,'cmovnz':0,'cmova':0,'cmovnbe':0,'cmovae':0,'cmovnb':0,
        'cmovb':0,'cmovnae':0,'cmovbe':0,'cmovna':0,'cmovg':0,'cmovnle':0,'cmovge':0,'cmovnl':0,
        'cmovl':0,'cmovnge':0,'cmovle':0,'cmovbg':0,'cmovc':0,'cmovnc':0,'cmovo':0,'cmovno':0,
        'cmovs':0,'cmovns':0,'cmovp':0,'cmovpe':0,'cmovnp':0,'cmovpo':0,
            
        'inc':1,'add':1,'adc':1,'xadd':1,'adcx':1,'adox':1,
        'dec':1,'sub':1,'sbb':1,
        'mul':1,'imul':1,
        'div':1,'idiv':1,
        'neg':1,'cmp':1,
        'cbw':1,'cwd':1,'cdq':1,'cqo':1,'cwde':1,'cdqe':1,
        'aaa':1,'daa':1,'aas':1,'das':1,'aam':1,'aad':1,
            
        'and':2,'or':2, 'not':2,'xor':2,'test':2, 
        'sal':2,'shl':2,'rol':2,'rcl':2,'shld':2,
        'shr':2,'sar':2,'ror':2,'rcr':2,'shrd':2,
        'bt':2, 'bts':2,'btr':2,'btc':2,
        'bsf':2,'bsr':2,
            
        'movs':3,'movsb':3,'movsw':3,'movsd':3,'movsq':3,
        'cmps':3,'cmpsb':3,'cmpsw':3,'cmpsd':3,'cmpsq':3,
        'scas':3,'scasb':3,'scasw':3,'scasd':3,'scasq':3,
        'stos':3,'stosb':3,'stosw':3,'stosd':3,'stosq':3,
        'lods':3,'lodsb':3,'lodsw':3,'lodsd':3,'lodsq':3,
        #rep,repe,repne,repz,repnz
            
        'jmp':4,
        'je':4, 'jz':4, 'jne':4,'jnz':4,'jp':4, 'jpe':4, 'jnp':4, 'jpo':4,
        'js':4, 'jns':4,'jo':4, 'jno':4,'jc':4, 'jnc':4, 
        'ja':4, 'jnbe':4, 'jae':4, 'jnb':4, 'jb':4, 'jnae':4, 'jbe':4, 'jna':4,
        'jg':4, 'jnle':4, 'jge':4, 'jnl':4, 'jl':4, 'jnge':4, 'jle':4, 'jng':4,
        'loop':4,'loope':4,'loopz':4,'loopne':4,'loopnz':4,
        'jcxz':4,'jecxz':4,'jrcxz':4,
        
        'call':5,'ret':8,'retn':8,

        'int':6,'into':6,'iret':6,   
        'clc':6,'stc':6,'cmc':6,'cld':6,'std':6,'cli':6,'sti':6,
        'hlt':6,'wait':6,'lock':6,'nop':6,'ud2':6,
            
        'bound':7,'enter':7,'leave':7,
        'lar':7,'lsl':7,'lgdt':7,'sgdt':7,'lidt':7,'sidt':7,'lldt':7,'sldt':7,
        'ltr':7,'str':7,'lmsw':7,'smsw':7,'verr':7,'verw':7,'arpl':7,'clts':7,
        'seto':7,'setno':7,'sets':7,'setns':7,
        'setc':7,'setb':7,'setnae':7,'setnc':7,'setnb':7,'setae':7,
        'setz':7,'sete':7,'setnz':7,'setne':7,
        'setp':7,'setpe':7,'setnp':7,'setpo':7,
        'setbe':7,'setna':7,'setnbe':7,'seta':7,
        'setl':7,'setnge':7,'setnl':7,'setge':7,
        'setle':7,'setng':7,'setnle':7,'setg':7,
        'cpuid':7,'rdtsc':7,'rdmsr':7,'wrmsr':7,'rsm':7,'rdpmc':7,'align':7,
        'sfence':7,'lfence':7,'mfence':7,'pause':7,'clflush':7,'crc32':7,
        }

MMX_I = {'movd':0,'movq':0,
        'packsswb':0,'packssdw':0,'packuswb':0,
        'punpckhbw':0,'punpckhwd':0,'punpckhdq':0,
        'punpcklbw':0,'punpcklwd':0,'punpckldq':0,

        'paddb':1,'paddw':1,'paddd':1,'paddq':1,
        'paddsb':1,'paddsw':1,'paddusb':1,'paddusw':1,
        'psubb':1,'psubw':1,'psubd':1,'psubq':1,
        'psubsb':1,'psubsw':1,'psubusb':1,'psubusw':1,
        'pmullw':1,'pmulhw':1,'pmulluw':1,'pmulhuw':1,
        'pmaddwd':1,
        'pcmpeqb':1,'pcmpeqw':1,'pcmpeqd':1,
        'pcmpgtpb':1,'pcmpgtpw':1,'pcmpgtpd':1,

        'pand':2, 'pandn':2,'por':2,'pxor':2,
        'psllw':2,'pslld':2,'psllq':2,
        'psrlw':2,'psrld':2,'psrlq':2,
        'psraw':2,'psrad':2,

        'emms':6
        }

SSE_I = {'movss':0,
        'movaps':0,'movhps':0,'movlps':0,'movups':0,
        'movhlps':0,'movlhps':0,
        'pmovmskb':0,'movmskps':0,
        'movntq':0,'movntps':0,'maskmovq':0,
        'pmaxsw':0,'maxps':0,'pmaxub':0,'maxss':0,
        'pminsw':0,'minps':0,'pminub':0,'minss':0,
        'cvtpi2ps':0,'cvtps2pi':0,'cvtsi2ss':0,'cvtss2si':0,
        'cvttps2pi':0,'cvttss2si':0,
        'shufps':0,'pshufw':0,'pextrw':0,'pinsrw':0,
        'unpckhps':0,

        'addps':1,'addss':1,
        'subps':1,'subss':1,
        'mulps':1,'mulss':1,
        'divps':1,'divss':1,
        'pavgw':1,'pavgb':1,
        'rcpps':1,'rcpss':1,
        'sqrtps':1,'sqrtss':1,
        'rsqrtps':1,'rsqrtss':1,
        'psadbw':1,

        'andps':2,'andnps':2,
        'orps':2,'xorps':2,
        'cmpps':2,'cmpss':2,
        'comiss':2,'ucomiss':2,

        'prefetchnta':6,'prefetcht0':6,'prefetcht1':6,'prefetcht2':6,
        'stmxcsr':6,'ldmxcsr':6,
        }

SSE2_I = {'movapd':0,'movdqa':0,'movhpd':0,'movlpd':0,'movupd':0,'movdqu':0,
        'movdq2q':0,'movq2dq':0,'movntpd':0,'movntdq':0,'movnti':0,
        'maskmovdqu':0,'movmskpd':0,
        'maxpd':0,'maxsd':0,
        'minpd':0,'minsd':0,
        'cvtdq2pd':0,'cvtdq2ps':0,'cvtps2dq':0,'cvtps2pd':0,
        'cvtpd2dq':0,'cvtpd2pi':0,'cvtpd2ps':0,'cvtpi2pd':0,
        'cvtsd2si':0,'cvtsd2ss':0,'cvtss2sd':0,'cvtsi2sd':0,
        'cvttpd2dq':0,'cvttpd2pi':0,'cvttps2dq':0,'cvttsd2si':0,
        'pshufd':0,'shufpd':0,'pshufhw':0,'pshuflw':0,
        'unpckhpd':0,'unpcklpd':0,

        'addpd':1,'addsd':1,
        'subpd':1,'subsd':1,
        'mulpd':1,'mulsd':1,'pmuludq':1,
        'divpd':1,'divsd':1,
        'sqrtpd':1,'sqrtsd':1,

        'andpd':2,'andnpd':2,
        'orpd':2,'xorpd':2, 
        'pslldq':2,'psrldq':2,
        'cmppd':2,'cmpsd':2,'cmpnltsd':2,
        'pcmpgtw':2,'pcmpgtd':2,'pcmpgtb':2,
        'comisd':2,'ucomisd':2

        #'movsd':1,'movd':1,'movq':1,'pmovmskb':1,
        #'paddw':1,'paddd':1,'paddq':1,'paddb':1,
        #'paddsw':1,'paddsb':1,'paddusw':1,'paddusb':1,
        #'psubw':1,'psubd':1,'psubq':1,'psubb':1,
        #'psubsw':1,'psubsb':1,'psubusw':1,'psubusw':1,
        #'pmulhw':1,'pmulhuw':1,'pmullw':1,
        #'pand':1,'pandn':1,'por':1,'pxor':1,
        #'psllw':1,'pslld':1,'psllq':1,'psllw':1,
        #'psraw':1,'psrad':1,
        #'psrlw':1,'psrld':1,'psrlq':1,
        #'pmaddwd':1,'packssdw':1,'packuswb':1,'punpcklqdq':1,'punpckhqdq':1,
        #'pmaxsw':1,'pmaxub':1,'pminsw':1,'pminub':1,
        #'pcmpeqw':1,'pcmpeqd':1,'pcmpeqb':1,
        #'pavgw':1,'pavgb':1,'pextrw':1,'pinsrw':1,
        #'packsswb':1,'psadbw':1,
        #'punpckhwd':1,'punpckhdq':1,'punpckhqdq':1,'punpckhbw':1,
        #'punpcklwd':1,'punpckldq':1,'punpcklqdq':1,'punpcklbw':1
        }

SSE3_I = {'movddup':0,'movshdup':0,'movsldup':0,
        'lddqu':0,

        'haddpd':1,'haddps':1,
        'hsubpd':1,'hsubps':1,
        'addsubpd':1,'addsubps':1
        }

SSSE3_I = {'palignr':1,'pshufb':1,

        'phaddw':1,'phaddd':1,'phaddsw':1,
        'phsubw':1,'phsubd':1,'phsubsw':1,
        'pabsw':1,'pabsd':1,'pabsb':1,
        'pmulhrsw':1,'pmaddubsw':1,
        'psignb':1,'psignw':1,'psignd':1
        }

SSE41_I = {'blendpd':0,'blendps':0,'blendvpd':0,'blendvps':0,'pblendw':0,'pblendvb':0,
        'pmovsxwd':0,'pmovsxwq':0,'pmovsxdq':0,'pmovsxbw':0,'pmovsxbd':0,'pmovsxbq':0,
        'pmovzxwd':0,'pmovzxwq':0,'pmovzxdq':0,'pmovzxbw':0,'pmovzxbd':0,'pmovzxbq':0,
        'pmaxsd':0,'pmaxsb':0,'pmaxuw':0,'pmaxud':0,
        'pminuw':0,'pminud':0,
        'phminposuw':0,'packusdw':0,'movntdqa':0,
        'pextrb':0,'pextrd':0,'pextrq':0,'extractps':0,
        'pinsrb':0,'pinsrd':0,'pinsrq':0,'insertps':0,
        'roundpd':0,'roundps':0,'roundsd':0,'roundss':0,

        'pmuldq':1,'pmulld':1,
        'pcmpeqq':1,'mpsadbw':1,
        'dppd':1,'dpps':1,

        'ptest':2
        }

SSE42_I = {'pcmpestri':1,'pcmpestrm':1,'pcmpistri':1,'pcmpistrm':1,'pcmpgtq':1}

AVX_I = {'vmovapd':1,'vmovaps':1,'vmovdqa':1,'vmovupd':1,'vmovups':1,'vmovdqu':1,'vmovntpd':1,'vmovntps':1,
        'vmaskmovpd':1,'vmaskmovps':1,'vmovddup':1,'vmovshdup':1,'vmovsldup':1,'vmovmskpd':1,'vmovmskps':1,
        'vmovd':1,'vmovq':1,
            
        'vaddpd':1,'vaddps':1,'vhaddpd':1,'vhaddps':1,
        'vsubpd':1,'vsubps':1,'vhsubpd':1,'vhsubps':1,
        'vaddsubpd':1,'vaddsubpd':1,
        'vmulpd':1,'vmulps':1,
        'vdivpd':1,'vdivps':1,
        'vdpps':1,'vrsqrtps':1,'vsqrtpd':1,

        'vandpd':1,'vandps':1,'vandnpd':1,'vandnps':1,
        'vorpd':1,'vorps':1,'vxorpd':1,'vxorps':1,'vpxor':1,
        'vtestpd':1,'vtestps':1,'vptest':1,
        'vcmppd':1,'vcmpps':1,'vcmpsd':1,'vcmpss':1,

        'vmaxpd':1,'vmaxps':1,'vminpd':1,'vminps':1,
        'vblendpd':1,'vblendps':1,'vblendvpd':1,'vblendvps':1,
        'vbroadcastsd':1,'vbroadcastss':1,'vpbroadcastw':1,'vbroadcastf128':1,
        'vcvtdq2pd':1,'vcvtdq2ps':1,'vcvtpd2dq':1,
        'vcvtpd2ps':1,'vcvtps2dq':1,'vcvtps2pd':1,
        'vcvttpd2dq':1,'vcvttps2dq':1,
        'vextractf128':1,'vinsertf128':1,'vlddqu':1,
        'vpextrd':1,'vpextrq':1,'vpextrqb':1,
        'vpermilpd':1,'vpermilps':1,'vperm2f128':1,
        'vpinsrd':1,'vpinsrq':1,'vpinsrb':1,
        'vroundpd':1,'vroundps':1,'vrcpps':1,
        'vshufpd':1,'vzeroall':1,'vzeroupper':1,
        'vunpckhpd':1,'vunpckhps':1,'vunpcklpd':1,'vunpcklps':1
        }

AVX2_I = {'vpmovsxbw':0,'vpmovsxwd':0,'vpmovsxwq':0,
        'vpmaskmovd':0,'vpmaskmovq':0,'vpmovmskb':0,
        'vpmaxsb':0,'vpmaxsw':0,'vpmaxsd':0,
        'vpmaxub':0,'vpmaxuw':0,'vpmaxud':0,
        'vpminsb':0,'vpminsw':0,'vpminsd':0,
        'vpminub':0,'vpminuw':0,'vpminud':0,
            
        'vpaddb':1,'vpaddw':1,'vpaddd':1,'vpaddq':1,
        'vpaddsb':1,'vpaddsw':1,'vpaddusb':1,'vpaddusw':1,
        'vphaddw':1,'vphaddd':1,'vphaddsw':1,
        'vpsubb':1,'vpsubw':1,'vpsubd':1,'vpsubq':1,
        'vpsubsb':1,'vpsubsw':1,'vpsubusb':1,'vpsubusw':1,
        'vphsubw':1,'vphsubd':1,'vphsubsw':1,
        'vpmuldq':1,'vpmuludq':1,'vpmulhw':1,'vpmulhuw':1,
        'vpmullw':1,'vpmulld':1,'vpmulhrsw':1,
        'vpabsw':1,'vpabsd':1,'vpabsb':1,
        'vpmaddwd':1,'vpmaddubsw':1,
        'vpcmpeqw':1,'vpcmpeqd':1,'vpcmpeqq':1,'vpcmpeqb':1,
        'vpcmpgtw':1,'vpcmpgtd':1,'vpcmpgtq':1,'vpcmpgtb':1,
        'vpsadbw':1,'vmpsadbw':1,

        'vpand':2,'vpandn':2,
        'vpor':2,'vpxor':2,
        'vpsllw':2,'vpslld':2,'vpsllq':2,
        'vpslldq':2,'vpsllvd':2,'vpsllvq':2,
        'vpsraw':2,'vpsrad':2,'vpsravd':2,
        'vpsrlw':2,'vpsrld':2,'vpsrlq':2,
        'vpsrldq':2,'vpsrlvd':2,'vpsrlvq':2,

        'vpalignr':1,'vpavgw':1,'vpavgb':1,
        'vpblendw':1,'vpblendd':1,'vpblendvb':1,
        'vpbroadcastb':1,'vpbroadcastd':1,'vpbroadcastq':1,'vbroadcasti128':1,
        'vextracti128':1,'vinserti128':1,'vperm2i128':1,
        'vpermq':1,'vpermpd':1,'vpermd':1,'vpermps':1,
        'vpshufd':1,'vpshufb':1,'vpshufhw':1,'vpshuflw':1,
        'vpsignw':1,'vpsignd':1,'vpsignb':1,
        'vpgatherdd':1,'vpgatherdq':1,'vpgatherpd':1,'vpgatherps':1,'vpgatherqd':1,'vpgatherqq':1,
        'vpacksswb':1,'vpackssdw':1,'vpackuswb':1,'vpackusdw':1,
        'vpunpckhwd':1,'vpunpckhdq':1,'vpunpckhqdq':1,'vpunpckhbw':1,
        'vpunpcklwd':1,'vpunpckldq':1,'vpunpcklqdq':1,'vpunpcklbw':1,
        'vmovntdqa':1
    }

AVX512_I = {'vp4dpwssd':1,'vp4dpwssds':1,'v4fmaddps':1,'v4fmaddss':1,'v4fnmaddps':1,'v4fnmaddss':1,
        'vpmovwb':1,'vpmovdw':1,'vpmovsxdq':1,'vpmovdb':1,'vpmovqw':1,'vpmovqd':1,'vpmovqb':1,
        'vpmovzxwd':1,'vpmovzxwq':1,'vpmovzxdq':1,'vpmovzxbw':1,'vpmovzxbd':1,'vpmovzxbq':1,
        'vpmovswb':1,'vpmovsdw':1,'vpmovsdb':1,'vpmovsqw':1,'vpmovsqd':1,'vpmovsqb':1,
        'vpmovuswb':1,'vpmovusdw':1,'vpmovusdb':1,'vpmovusqw':1,'vpmovusqd':1,'vpmovusqb':1,'vdbpsadbw':1,
        'vmovdqa32':1,'vmovdqa64':1,'vmovsd':1,'vmovss':1,'vmovdqu8':1,'vmovdqu16':1,'vmovdqu32':1,'vmovdqu64':1,
        'vmovddup':1,'vmovshdup':1,'vmovsldup':1,'vpmovw2m':1,'vpmovd2m':1,'vpmovq2m':1,'vpmovb2m':1,
        'vpmovm2w':1,'vpmovm2d':1,'vpmovm2q':1,'vpmovm2b':1,'vmovntdq':1,
        'kmovw':1,'kmovd':1,'kmovq':1,'kmovb':1,
        'vpmaxsq':1,'vpmaxuq':1,'vmaxsd':1,'vmaxss':1,
        'vpminsq':1,'vpminuq':1,'vminsd':1,'vminss':1,
        'valignd':1,'valignq':1,
        'vpblendmw':1,'vpblendmd':1,'vpblendmq':1,'vpblendmb':1,'vblendmpd':1,'vblendmps':1,
        'vcvtqq2pd':1,'vcvtuqq2pd':1,'vcvtqq2ps':1,'vcvtuqq2ps':1,
        'vcvtsi2ss':1,'vcvtusi2ss':1,'vcvtsi2sd':1,'vcvtusi2sd':1,
        'vcvtpd2qq':1,'vcvtpd2uqq':1,'vcvtsd2si':1,'vcvtsd2usi':1,
        'vcvtps2qq':1,'vcvtss2si':1,'vcvtph2ps':1,
        'vcvtps2ph':1,'vcvtsd2ss':1,'vcvtss2sd':1,
        'vcvtudq2ps':1,'vcvtudq2pd':1,
        'vcvtss2usi':1,'vcvtpd2udq':1,
        'vcvtps2udq':1,'vcvtps2uqq':1,
        'vcvtne2ps2bf16':1,'vcvtneps2bf16':1,
        'vcvttpd2qq':1,'vcvttpd2uqq':1,'vcvttps2qq':1,'vcvttps2uqq':1,
        'vcvttsd2si':1,'vcvttsd2usi':1,'vcvttss2si':1,'vcvttss2usi':1,
        'vcvttps2udq':1,'vcvttpd2udq':1,

        'vaddsd':1,'vaddss':1,
        'kaddb':1,'kaddw':1,'kaddd':1,'kaddq':1,
        'vsubsd':1,'vsubss':1,
        'vmulsd':1,'vmulss':1,'vpmultishiftqb':1,
        'vdivsd':1,'vdivss':1,
        'vpmadd52huq':1,'vpmadd52luq':1,'vpabsq':1,
        'vpcmpb':1,'vpcmpw':1,'vpcmpd':1,'vpcmpq':1,
        'vpcmpub':1,'vpcmpuw':1,'vpcmpud':1,'vpcmpuq':1,
        'vcomisd':1,'vcomiss':1,'vucomiss':1,
        'vfmadd132pd':1,'vfmadd213pd':1,'vfmadd231pd':1,
        'vfmadd132ps':1,'vfmadd213ps':1,'vfmadd231ps':1,
        'vfmadd132sd':1,'vfmadd213sd':1,'vfmadd231sd':1,
        'vfmadd132ss':1,'vfmadd213ss':1,'vfmadd231ss':1,
        'vfmaddsub132pd':1,'vfmaddsub213pd':1,'vfmaddsub231pd':1,
        'vfmaddsub132ps':1,'vfmaddsub213ps':1,'vfmaddsub231ps':1,
        'vfmsub132pd':1,'vfmsub213pd':1,'vfmsub231pd':1,
        'vfmsub132ps':1,'vfmsub213ps':1,'vfmsub231ps':1,
        'vfmsub132sd':1,'vfmsub213sd':1,'vfmsub231sd':1,
        'vfmsub132ss':1,'vfmsub213ss':1,'vfmsub231ss':1,
        'vfmsubadd132pd':1,'vfmsubadd213pd':1,'vfmsubadd231pd':1,
        'vfmsubadd132ps':1,'vfmsubadd213ps':1,'vfmsubadd231ps':1,
        'vfnmadd132pd':1,'vfnmadd213pd':1,'vfnmadd231pd':1,
        'vfnmadd132ps':1,'vfnmadd213ps':1,'vfnmadd231ps':1,
        'vfnmadd132sd':1,'vfnmadd213sd':1,'vfnmadd231sd':1,
        'vfnmadd132ss':1,'vfnmadd213ss':1,'vfnmadd231ss':1,
        'vsqrtps':1,'vsqrtsd':1,'vsqrtss':1,  
        'vrsqrt14pd':1,'vrsqrt14ps':1,'vrsqrt14sd':1,'vrsqrt14ss':1,
        'vrsqrt28pd':1,'vrsqrt28ps':1,'vrsqrt28sd':1,'vrsqrt28ss':1,

        'kandb':1,'kandw':1,'kandd':1,'kandq':1,
        'kandnb':1,'kandnw':1,'kandnd':1,'kandnq':1,
        'vpandq':1,'vpandd':1,'vpandnd':1,'vpandnq':1,
        'knotb':1,'knotw':1,'knotd':1,'knotq':1,
        'korb':1,'korw':1,'kord':1,'korq':1,
        'kxorb':1,'kxorw':1,'kxord':1,'kxorq':1,
        'vpord':1,'vporq':1,'vpxord':1,'vpxorq':1,
        'kxnorb':1,'kxnorw':1,'kxnord':1,'kxnorq':1,
        'ktestb':1,'ktestw':1,'ktestd':1,'ktestq':1,
        'kortestb':1,'kortestw':1,'kortestd':1,'kortestq':1,
        'vptestmb':1,'vptestmw':1,'vptestmd':1,'vptestmq':1,
        'vptestnmb':1,'vptestnmw':1,'vptestnmd':1,'vptestnmq':1,
        'kshiftlb':1,'kshiftlw':1,'kshiftld':1,'kshiftlq':1,
        'kshiftrb':1,'kshiftrw':1,'kshiftrd':1,'kshiftrq':1,
        'vpshldw':1,'vpshldd':1,'vpshldq':1,'vpshldvw':1,'vpshldvd':1,'vpshldvq':1,
        'vpshrdw':1,'vpshrdd':1,'vpshrdq':1,'vpshrdvw':1,'vpshrdvd':1,'vpshrdvq':1,
        'vpsllvw':1,'vpsravw':1,'vpsravq':1,'vpsrlvw':1,
            
            
        'vbroadcastf32x2':1,'vbroadcastf32x4':1,'vbroadcastf32x8':1,
        'vbroadcastf64x2':1,'vbroadcastf64x4':1,
        'vbroadcasti32x2':1,'vbroadcasti32x4':1,'vbroadcasti32x8':1,
        'vbroadcasti64x2':1,'vbroadcasti64x4':1,
        'vpbroadcastmb2q':1,'vpbroadcastmw2d':1,


        'vpshufbitqmb':1,
        'vcompresspd':1,'vcompressps':1,'vcompresspw':1,
        'vpcompressw':1,'vpcompressd':1,'vpcompressq':1,'vpcompressb':1,
        'vpconflictd':1,'vpconflictq':1,
        'vdpbf16ps':1,'vpdpbusd':1,'vpdpbusds':1,'vpdpwssd':1,'vpdpwssds':1,
        'vexp2pd':1,'vexp2ps':1,'vfixupimmpd':1,'vfixupimmps':1,'vfixupimmsd':1,'vfixupimmss':1,
        'vpexpandw':1,'vpexpandd':1,'vpexpandq':1,'vpexpandb':1,'vexpandpd':1,'vexpandps':1,
        'vextractf32x4':1,'vextractf32x8':1,'vextractf64x2':1,'vextractf64x4':1,
        'vextracti32x4':1,'vextracti32x8':1,'vextracti64x2':1,'vextracti64x4':1,
        'vfpclasspd':1,'vfpclassps':1,'vfpclasssd':1,'vfpclassss':1,
        'vgetexppd':1,'vgetexpps':1,'vgetexpsd':1,'vgetexpss':1,
        'vgetmantpd':1,'vgetmantps':1,'vgetmantsd':1,'vgetmantss':1,'vgatherdps':1,'vgatherdpd':1,'vgatherqpd':1,'vgatherqps':1,
        'vpscatterdd':1,'vscatterdps':1,'vpscatterdq':1,'vscatterdpd':1,'vpscatterqd':1,'vpscatterqq':1,'vscatterqpd':1,'vscatterqps':1,
        'vinsertf32x4':1,'vinsertf32x8':1,'vinsertf64x2':1,'vinsertf64x4':1,
        'vinserti32x4':1,'vinserti32x8':1,'vinserti64x2':1,'vinserti64x4':1,
        'kunpckbw':1,'kunpckbq':1,'kunpckbd':1,
        'vplzcntd':1,'vplzcntq':1,
        'vpermt2w':1,'vpermt2d':1,'vpermt2q':1,'vpermt2b':1,'vpermt2pd':1,'vpermt2ps':1,
        'vpermi2w':1,'vpermi2d':1,'vpermi2q':1,'vpermi2b':1,'vpermi2pd':1,'vpermi2ps':1,
        'vpermw':1,'vpermb':1,'vpopcntw':1,'vpopcntd':1,'vpopcntq':1,'vpopcntb':1,
        'vgatherpf0dps':1,'vgatherpf1dps':1,'vgatherpf0dpd':1,'vgatherpf1dpd':1,
        'vgatherpf0qpd':1,'vgatherpf1qpd':1,'vgatherpf0qps':1,'vgatherpf0qps':1,
        'vscatterpf0dps':1,'vscatterpf0dps':1,'vscatterpf0dpd':1,'vscatterpf1dpd':1,
        'vscatterpf0qpd':1,'vscatterpf1qpd':1,'vscatterpf0qps':1,'vscatterpf0qps':1,
        'vrangepd':1,'vrangeps':1,'vrangesd':1,'vrangess':1,
        'vrcp14pd':1,'vrcp14ps':1,'vrcp14sd':1,'vrcp14ss':1,
        'vrcp28pd':1,'vrcp28ps':1,'vrcp28sd':1,'vrcp28ss':1,
        'vreducepd':1,'vreduceps':1,'vreducesd':1,'vreducess':1,
        'vprold':1,'vprolq':1,'vprolvd':1,'vprolvq':1,
        'vprord':1,'vprorq':1,'vprorvd':1,'vprorvq':1,
        'vrndscalepd':1,'vrndscaleps':1,'vrndscalesd':1,'vrndscaless':1,
        'vscalefpd':1,'vscalefps':1,'vscalefsd':1,'vscalefss':1,
        'vshuff32x4':1,'vshuff64x2':1,'vshufi32x4':1,'vshufi64x2':1,
        'vpternlogd':1,'vpternlogq':1,

        #'vpmovsxwd':1,'vpmovsxwq':1,'vpmovsxbw':1,'vpmovsxbd':1,'vpmovsxbq':1,
        #'vmovapd':1,'vmovaps':1,'vmovupd':1,'vmovups':1,'vmovntdqa':1,'vmovntpd':1,'vmovntps':1,
        #'vpaddw':1,'vpaddd':1,'vpaddq':1,'vpaddb':1,'vaddpd':1,'vaddps':1,'vpaddsw':1,'vpaddsb':1,'vpaddusw':1,'vpaddusb':1,
        #'vpsubw':1,'vpsubd':1,'vpsubq':1,'vpsubb':1,'vsubpd':1,'vsubps':1,'vpsubsw':1,'vpsubsb':1,'vpsubusw':1,'vpsubusb':1,
        #'vpabsw':1,'vpabsd':1,
        #'vpmuldq':1,'vpmuludq':1,'vmulpd':1,'vmulps':1,'vpmulhw':1,'vpmulhuw':1,'vpmulhrsw':1,'vpmullw':1,'vpmulld':1,'vpmullq':1,
        #'vdivpd':1,'vdivps':1,
        #'vandpd':1,'vandps':1,'vandnpd':1,'vandnps':1,
        #'vorpd':1,'vorps':1,
        #'vxorpd':1,'vxorps':1,
        #'vcmppd':1,'vcmpps':1,'vcmpsd':1,'vcmpss':1,'vpcmpeqd':1,'vpcmpeqq':1,'vpcmpgtq':1,
        #'vpmaxsw':1,'vpmaxsd':1,'vpmaxsb':1,'vpmaxuw':1,'vpmaxud':1,'vpmaxub':1,
        #'vpminsw':1,'vpminsd':1,'vpminsb':1,'vpminuw':1,'vpminud':1,'vpminub':1,
        #'vpslldq':1,'vpsrldq':1,
        #'vpsllw':1,'vpslld':1,'vpsllq':1,'vpsllvd':1,'vpsllvq':1,
        #'vpsraw':1,'vpsrad':1,'vpsraq':1,'vpsravd':1,
        #'vpsrlw':1,'vpsrld':1,'vpsrlq':1,'vpsrlvd':1,'vpsrlvq':1,
        #'vpbroadcastb':1,'vpbroadcastd':1,'vpbroadcastq':1,'vbroadcastsd':1,'vbroadcastss':1,'vpbroadcastw':1,
        #'vcvtdq2ps':1,'vcvtpd2dq':1,'vcvtpd2ps':1,'vcvtps2dq':1,'vcvtps2pd':1,'vcvtdq2pd':1,'vcvttpd2dq':1,'vcvttps2dq':1,
        #'vpalignr':1,'vpgatherdd':1,'vpgatherdq':1,'vpgatherqd':1,'vpgatherqq':1,
        #'vpavgw':1,'vpavgb':1,
        #'vpmaddwd':1,'vpmaddubsw':1,
        #'vpermq':1,'vpermd':1,'vpermpd':1,'vpermps':1,'vpermilpd':1,'vpermilps':1,
        #'vpacksswb':1,'vpackssdw':1,'vpackuswb':1,'vpackusdw':1,
        #'vpsadbw':1,'vsqrtpd':1,
        #'vpshufd':1,'vpshufb':1,'vshufpd':1,'vshufps':1,'vpshufhw':1,'vpshuflw':1,
        #'vpunpckhwd':1,'vpunpckhdq':1,'vpunpckhqdq':1,'vpunpckhbw':1,
        #'vpunpcklwd':1,'vpunpckldq':1,'vpunpcklqdq':1,'vpunpcklbw':1,
        #'vunpckhpd':1,'vunpckhps':1,'vunpcklpd':1,'vunpcklps':1
        }

BMI_I = {'andn':2,'bextr':1,'blsi':1,'blsmsk':1,'blsr':1,'tzcnt':1}

BMI2_I = {'bzhi':1,'pdep':1,'pext':1,

        'mulx':1,

        'sarx':2,'shlx':2,'shrx':2,'rorx':2
        }

AES_I = {'aesdec':1,'aesdeclast':1,'aesenc':1,'aesenclast':1,'aesimc':1,'aeskeygenassist':1,
        'vaesdec':1,'vaesdeclast':1,'vaesenc':1,'vaesenclast':1,'vaesimc':1,'vaeskeygenassist':1}

SHA_I = {'sha1msg1':1,'sha1msg2':1,'sha1nexte':1,'sha1rnds4':1,'sha256msg1':1,'sha256msg2':1,'sha256rnds2':1}

XOP_I = {'vprotb':1,'vprotw':1,'vprotd':1,'vprotq':1}

O_I = {'pclmulqdq':1,'vpclmulqdq':1,'rdrand':1,'rdseed':1}

#------------------------------------------------------ARM Framework-----------------------------------------------


'''
mips_TI = {'j':1,'b':1,'bc1f':1,'bc1fl':1,'bc1t':1,'bc1tl':1,'bc2f':1,'bc2fl':1,'bc2t':1,'bc2tl':1,
            'beq':1,'beql':1,'bgez':1,'bgezl':1,'bgtz':1,'bgtzl':1,'blez':1,'blezl':1,'bltz':1,'bltzl':1,
            'bne':1,'bnel':1}
mips_CI = {'jal':1, 'jalr':1,'bal':1,'bgezal':1,'bgezall':1,'bltzal':1,'bltzall':1}
mips_AI = {'add':1, 'addu':1, 'addi':1,'addiu':1,'add.s':1,'add.d':1,'madd':1,'maddu':1,
            'sub':1,'subu':1,'sub,s':1,'sub.d':1,'msub':1,'msubu':1,
            'mul':1,'mult':1,'multu':1,'mul.s':1,'mul.d':1,
            'div':1,'divu':1,'div.s':1,'div.d':1,
            'abs.s':1,'abs.d':1,'neg.s':1,'neg.d':1,}
mips_BI = {'and':1, 'andi':1, 'nor':1,'or':1,'ori':1,'xor':1,'xori':1,
            'sll':1,'sllv':1,'sra':1,'srav':1,'srl':1,'srlv':1}
'''