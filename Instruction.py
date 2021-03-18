#------------------------------------------------------------------------------------------------------------------
#1.transfer 2.arithmetical 3.logical 4.cluster 5.jump 6.call 7.CPU-resolve 8.other 9.return
#------------------------------------------------------MIPS Framework----------------------------------------------
MIPS_I = {'move':1,'movf':1,'movt':1,'movn':1,'movz':1,
        'la':1,'li':1,'lui':1,
        'sb':1,'sh':1,
        'lb':1,'lbu':1,
        'ld':1,'ldl':1,'ldr':1,
        'lw':1,'lwl':1,'lwr':1,
        'sd':1,'sdl':1,'sdr':1,
        'sw':1,'swl':1,'swr':1,
        'lh':1,'lhu':1, 
        'lw':1,'lwu':1,
        'mfhi':1,'mflo':1,'mthi':1,'mtlo':1,

        'add':2, 'addu':2, 'addi':2,'addiu':2,'add.s':2,'add.d':2,
        'sub':2,'subu':2,'sub.s':2,'sub.d':2,
        'mul':2,'mult':2,'multu':2,'mul.s':2,'mul.d':2,
        'div':2,'divu':2,'div.s':2,'div.d':2,
        'madd':2,'maddu':2,'msub':2,'msubu':2,
        'teq':2,'clo':2,'clz':2,
        'slt':2,'slti':2,'sltiu':2,'sltu':2,
        'abs.s':2,'abs.d':2,'neg.s':2,'neg.d':2,
        
        'and':3,'andi':3,'nor':3,'or':3,  'ori':3,'xor':3,'xori':3,
        'sll':3,'sllv':3,'sra':3,'srav':3,'srl':3,'srlv':3,

        'j':5,'b':5,
        'bc0f':5,'bc0fl':5,'bc0t':5,'bc0tl':5,
        'bc1f':5,'bc1fl':5,'bc1t':5,'bc1tl':5,
        'bc2f':5,'bc2fl':5,'bc2t':5,'bc2tl':5,
        'beq':5,'beql':5,'beqz':5,'beqzl':5,
        'bge':5,'bgel':5,'bgez':5,'bgezl':5,'bgeu':5,'bgeul':5,
        'bgt':5,'bgtl':5,'bgtz':5,'bgtzl':5,'bgtu':5,'bgtul':5,
        'ble':5,'blel':5,'blez':5,'blezl':5,'bleu':5,'bleul':5,
        'blt':5,'bltl':5,'bltz':5,'bltzl':5,'bltu':5,'bltul':5,
        'bne':5,'bnel':5,'bnez':5,'bnezl':5,
    
        'jal':6, 'jalr':6,'bal':6,'jr':9,
        'bgezal':6,'bgezall':6,'bltzal':6,'bltzall':6,

        'nop':7,'ssnop':7
}

#------------------------------------------------------x86 Framework-----------------------------------------------
x86_I = {'mov':1,'movsx':1,'movsxd':1,'movzx':1,'movbe':1,
        'xchg':1,'cmpxchg':1,'cmpxchg8b':1,'xlat':1,'xgetbv':1,'bswap':1,
        'push':1,'pusha':1,'pushad':1,'pop':1,'popa':1,'popad':1,
        'lea':1,'lds':1,'les':1,'lfs':1,'lgs':1,'lss':1,
        'pushf':1,'pushfq':1,'pushfd':1,'popf':1, 'popfq':1, 'popfd':1,'lahf':1,'sahf':1,
        'in':1,'ins':1,'insb':1,'insw':1,'insd':1,
        'out':1,'outs':1,'outsb':1,'outsw':1,'outsd':1,
        'cmove':1,'cmovz':1,'cmovne':1,'cmovnz':1,'cmova':1,'cmovnbe':1,'cmovae':1,'cmovnb':1,
        'cmovb':1,'cmovnae':1,'cmovbe':1,'cmovna':1,'cmovg':1,'cmovnle':1,'cmovge':1,'cmovnl':1,
        'cmovl':1,'cmovnge':1,'cmovle':1,'cmovbg':1,'cmovc':1,'cmovnc':1,'cmovo':1,'cmovno':1,
        'cmovs':1,'cmovns':1,'cmovp':1,'cmovpe':1,'cmovnp':1,'cmovpo':1,
            
        'inc':2,'add':2,'adc':2,'xadd':2,'adcx':2,'adox':2,
        'dec':2,'sub':2,'sbb':2,
        'mul':2,'imul':2,
        'div':2,'idiv':2,
        'neg':2,'cmp':2,
        'cbw':2,'cwd':2,'cdq':2,'cqo':2,'cwde':2,'cdqe':2,
        'aaa':2,'daa':2,'aas':2,'das':2,'aam':2,'aad':2,
            
        'and':3,'or':3, 'not':3,'xor':3,'test':3, 
        'sal':3,'shl':3,'rol':3,'rcl':3,'shld':3,
        'shr':3,'sar':3,'ror':3,'rcr':3,'shrd':3,
        'bt':3, 'bts':3,'btr':3,'btc':3,
        'bsf':3,'bsr':3,
            
        'movs':4,'movsb':4,'movsw':4,'movsd':4,'movsq':4,
        'cmps':4,'cmpsb':4,'cmpsw':4,'cmpsd':4,'cmpsq':4,
        'scas':4,'scasb':4,'scasw':4,'scasd':4,'scasq':4,
        'stos':4,'stosb':4,'stosw':4,'stosd':4,'stosq':4,
        'lods':4,'lodsb':4,'lodsw':4,'lodsd':4,'lodsq':4,
        #rep,repe,repne,repz,repnz
            
        'jmp':5,
        'je':5, 'jz':5, 'jne':5,'jnz':5,'jp':5, 'jpe':5, 'jnp':5, 'jpo':5,
        'js':5, 'jns':5,'jo':5, 'jno':5,'jc':5, 'jnc':5, 
        'ja':5, 'jnbe':5, 'jae':5, 'jnb':5, 'jb':5, 'jnae':5, 'jbe':5, 'jna':5,
        'jg':5, 'jnle':5, 'jge':5, 'jnl':5, 'jl':5, 'jnge':5, 'jle':5, 'jng':5,
        'loop':5,'loope':5,'loopz':5,'loopne':5,'loopnz':5,
        'jcxz':5,'jecxz':5,'jrcxz':5,
        
        'call':6,'ret':9,'retn':9,

        'int':7,'into':7,'iret':7,   
        'clc':7,'stc':7,'cmc':7,'cld':7,'std':7,'cli':7,'sti':7,
        'hlt':7,'wait':7,'lock':7,'nop':7,'ud2':7,
            
        'bound':8,'enter':8,'leave':8,
        'lar':8,'lsl':8,'lgdt':8,'sgdt':8,'lidt':8,'sidt':8,'lldt':8,'sldt':8,
        'ltr':8,'str':8,'lmsw':8,'smsw':8,'verr':8,'verw':8,'arpl':8,'clts':8,
        'seto':8,'setno':8,'sets':8,'setns':8,
        'setc':8,'setb':8,'setnae':8,'setnc':8,'setnb':8,'setae':8,
        'setz':8,'sete':8,'setnz':8,'setne':8,
        'setp':8,'setpe':8,'setnp':8,'setpo':8,
        'setbe':8,'setna':8,'setnbe':8,'seta':8,
        'setl':8,'setnge':8,'setnl':8,'setge':8,
        'setle':8,'setng':8,'setnle':8,'setg':8,
        'cpuid':8,'rdtsc':8,'rdmsr':8,'wrmsr':8,'rsm':8,'rdpmc':8,'align':8,
        'sfence':8,'lfence':8,'mfence':8,'pause':8,'clflush':8,'crc32':8,
        }

MMX_I = {'movd':1,'movq':1,
        'packsswb':1,'packssdw':1,'packuswb':1,
        'punpckhbw':1,'punpckhwd':1,'punpckhdq':1,
        'punpcklbw':1,'punpcklwd':1,'punpckldq':1,

        'paddb':2,'paddw':2,'paddd':2,'paddq':2,
        'paddsb':2,'paddsw':2,'paddusb':2,'paddusw':2,
        'psubb':2,'psubw':2,'psubd':2,'psubq':2,
        'psubsb':2,'psubsw':2,'psubusb':2,'psubusw':2,
        'pmullw':2,'pmulhw':2,'pmulluw':2,'pmulhuw':2,
        'pmaddwd':2,
        'pcmpeqb':2,'pcmpeqw':2,'pcmpeqd':2,
        'pcmpgtpb':2,'pcmpgtpw':2,'pcmpgtpd':2,

        'pand':3, 'pandn':3,'por':3,'pxor':3,
        'psllw':3,'pslld':3,'psllq':3,
        'psrlw':3,'psrld':3,'psrlq':3,
        'psraw':3,'psrad':3,

        'emms':7
        }

SSE_I = {'movss':1,
        'movaps':1,'movhps':1,'movlps':1,'movups':1,
        'movhlps':1,'movlhps':1,
        'pmovmskb':1,'movmskps':1,
        'movntq':1,'movntps':1,'maskmovq':1,
        'pmaxsw':1,'maxps':1,'pmaxub':1,'maxss':1,
        'pminsw':1,'minps':1,'pminub':1,'minss':1,
        'cvtpi2ps':1,'cvtps2pi':1,'cvtsi2ss':1,'cvtss2si':1,
        'cvttps2pi':1,'cvttss2si':1,
        'shufps':1,'pshufw':1,'pextrw':1,'pinsrw':1,
        'unpckhps':1,

        'addps':2,'addss':2,
        'subps':2,'subss':2,
        'mulps':2,'mulss':2,
        'divps':2,'divss':2,
        'pavgw':2,'pavgb':2,
        'rcpps':2,'rcpss':2,
        'sqrtps':2,'sqrtss':2,
        'rsqrtps':2,'rsqrtss':2,
        'psadbw':2,

        'andps':3,'andnps':3,
        'orps':3,'xorps':3,
        'cmpps':3,'cmpss':3,
        'comiss':3,'ucomiss':3,

        'prefetchnta':7,'prefetcht0':7,'prefetcht1':7,'prefetcht2':7,
        'stmxcsr':7,'ldmxcsr':7,
        }

SSE2_I = {'movapd':1,'movdqa':1,'movhpd':1,'movlpd':1,'movupd':1,'movdqu':1,
        'movdq2q':1,'movq2dq':1,'movntpd':1,'movntdq':1,'movnti':1,
        'maskmovdqu':1,'movmskpd':1,
        'maxpd':1,'maxsd':1,
        'minpd':1,'minsd':1,
        'cvtdq2pd':1,'cvtdq2ps':1,'cvtps2dq':1,'cvtps2pd':1,
        'cvtpd2dq':1,'cvtpd2pi':1,'cvtpd2ps':1,'cvtpi2pd':1,
        'cvtsd2si':1,'cvtsd2ss':1,'cvtss2sd':1,'cvtsi2sd':1,
        'cvttpd2dq':1,'cvttpd2pi':1,'cvttps2dq':1,'cvttsd2si':1,
        'pshufd':1,'shufpd':1,'pshufhw':1,'pshuflw':1,
        'unpckhpd':1,'unpcklpd':1,

        'addpd':2,'addsd':2,
        'subpd':2,'subsd':2,
        'mulpd':2,'mulsd':2,'pmuludq':2,
        'divpd':2,'divsd':2,
        'sqrtpd':2,'sqrtsd':2,

        'andpd':3,'andnpd':3,
        'orpd':3,'xorpd':3, 
        'pslldq':3,'psrldq':3,
        'cmppd':3,'cmpsd':3,'cmpnltsd':3,
        'pcmpgtw':3,'pcmpgtd':3,'pcmpgtb':3,
        'comisd':3,'ucomisd':3

        #'movsd':2,'movd':2,'movq':2,'pmovmskb':2,
        #'paddw':2,'paddd':2,'paddq':2,'paddb':2,
        #'paddsw':2,'paddsb':2,'paddusw':2,'paddusb':2,
        #'psubw':2,'psubd':2,'psubq':2,'psubb':2,
        #'psubsw':2,'psubsb':2,'psubusw':2,'psubusw':2,
        #'pmulhw':2,'pmulhuw':2,'pmullw':2,
        #'pand':2,'pandn':2,'por':2,'pxor':2,
        #'psllw':2,'pslld':2,'psllq':2,'psllw':2,
        #'psraw':2,'psrad':2,
        #'psrlw':2,'psrld':2,'psrlq':2,
        #'pmaddwd':2,'packssdw':2,'packuswb':2,'punpcklqdq':2,'punpckhqdq':2,
        #'pmaxsw':2,'pmaxub':2,'pminsw':2,'pminub':2,
        #'pcmpeqw':2,'pcmpeqd':2,'pcmpeqb':2,
        #'pavgw':2,'pavgb':2,'pextrw':2,'pinsrw':2,
        #'packsswb':2,'psadbw':2,
        #'punpckhwd':2,'punpckhdq':2,'punpckhqdq':2,'punpckhbw':2,
        #'punpcklwd':2,'punpckldq':2,'punpcklqdq':2,'punpcklbw':2
        }

SSE3_I = {'movddup':1,'movshdup':1,'movsldup':1,
        'lddqu':1,

        'haddpd':2,'haddps':2,
        'hsubpd':2,'hsubps':2,
        'addsubpd':2,'addsubps':2
        }

SSSE3_I = {'palignr':2,'pshufb':2,

        'phaddw':2,'phaddd':2,'phaddsw':2,
        'phsubw':2,'phsubd':2,'phsubsw':2,
        'pabsw':2,'pabsd':2,'pabsb':2,
        'pmulhrsw':2,'pmaddubsw':2,
        'psignb':2,'psignw':2,'psignd':2
        }

SSE41_I = {'blendpd':1,'blendps':1,'blendvpd':1,'blendvps':1,'pblendw':1,'pblendvb':1,
        'pmovsxwd':1,'pmovsxwq':1,'pmovsxdq':1,'pmovsxbw':1,'pmovsxbd':1,'pmovsxbq':1,
        'pmovzxwd':1,'pmovzxwq':1,'pmovzxdq':1,'pmovzxbw':1,'pmovzxbd':1,'pmovzxbq':1,
        'pmaxsd':1,'pmaxsb':1,'pmaxuw':1,'pmaxud':1,
        'pminuw':1,'pminud':1,
        'phminposuw':1,'packusdw':1,'movntdqa':1,
        'pextrb':1,'pextrd':1,'pextrq':1,'extractps':1,
        'pinsrb':1,'pinsrd':1,'pinsrq':1,'insertps':1,
        'roundpd':1,'roundps':1,'roundsd':1,'roundss':1,

        'pmuldq':2,'pmulld':2,
        'pcmpeqq':2,'mpsadbw':2,
        'dppd':2,'dpps':2,

        'ptest':3
        }

SSE42_I = {'pcmpestri':2,'pcmpestrm':2,'pcmpistri':2,'pcmpistrm':2,'pcmpgtq':2}

AVX_I = {'vmovapd':2,'vmovaps':2,'vmovdqa':2,'vmovupd':2,'vmovups':2,'vmovdqu':2,'vmovntpd':2,'vmovntps':2,
        'vmaskmovpd':2,'vmaskmovps':2,'vmovddup':2,'vmovshdup':2,'vmovsldup':2,'vmovmskpd':2,'vmovmskps':2,
        'vmovd':2,'vmovq':2,
            
        'vaddpd':2,'vaddps':2,'vhaddpd':2,'vhaddps':2,
        'vsubpd':2,'vsubps':2,'vhsubpd':2,'vhsubps':2,
        'vaddsubpd':2,'vaddsubpd':2,
        'vmulpd':2,'vmulps':2,
        'vdivpd':2,'vdivps':2,
        'vdpps':2,'vrsqrtps':2,'vsqrtpd':2,

        'vandpd':2,'vandps':2,'vandnpd':2,'vandnps':2,
        'vorpd':2,'vorps':2,'vxorpd':2,'vxorps':2,'vpxor':2,
        'vtestpd':2,'vtestps':2,'vptest':2,
        'vcmppd':2,'vcmpps':2,'vcmpsd':2,'vcmpss':2,

        'vmaxpd':2,'vmaxps':2,'vminpd':2,'vminps':2,
        'vblendpd':2,'vblendps':2,'vblendvpd':2,'vblendvps':2,
        'vbroadcastsd':2,'vbroadcastss':2,'vpbroadcastw':2,'vbroadcastf128':2,
        'vcvtdq2pd':2,'vcvtdq2ps':2,'vcvtpd2dq':2,
        'vcvtpd2ps':2,'vcvtps2dq':2,'vcvtps2pd':2,
        'vcvttpd2dq':2,'vcvttps2dq':2,
        'vextractf128':2,'vinsertf128':2,'vlddqu':2,
        'vpextrd':2,'vpextrq':2,'vpextrqb':2,
        'vpermilpd':2,'vpermilps':2,'vperm2f128':2,
        'vpinsrd':2,'vpinsrq':2,'vpinsrb':2,
        'vroundpd':2,'vroundps':2,'vrcpps':2,
        'vshufpd':2,'vzeroall':2,'vzeroupper':2,
        'vunpckhpd':2,'vunpckhps':2,'vunpcklpd':2,'vunpcklps':2
        }

AVX2_I = {'vpmovsxbw':1,'vpmovsxwd':1,'vpmovsxwq':1,
        'vpmaskmovd':1,'vpmaskmovq':1,'vpmovmskb':1,
        'vpmaxsb':1,'vpmaxsw':1,'vpmaxsd':1,
        'vpmaxub':1,'vpmaxuw':1,'vpmaxud':1,
        'vpminsb':1,'vpminsw':1,'vpminsd':1,
        'vpminub':1,'vpminuw':1,'vpminud':1,
            
        'vpaddb':2,'vpaddw':2,'vpaddd':2,'vpaddq':2,
        'vpaddsb':2,'vpaddsw':2,'vpaddusb':2,'vpaddusw':2,
        'vphaddw':2,'vphaddd':2,'vphaddsw':2,
        'vpsubb':2,'vpsubw':2,'vpsubd':2,'vpsubq':2,
        'vpsubsb':2,'vpsubsw':2,'vpsubusb':2,'vpsubusw':2,
        'vphsubw':2,'vphsubd':2,'vphsubsw':2,
        'vpmuldq':2,'vpmuludq':2,'vpmulhw':2,'vpmulhuw':2,
        'vpmullw':2,'vpmulld':2,'vpmulhrsw':2,
        'vpabsw':2,'vpabsd':2,'vpabsb':2,
        'vpmaddwd':2,'vpmaddubsw':2,
        'vpcmpeqw':2,'vpcmpeqd':2,'vpcmpeqq':2,'vpcmpeqb':2,
        'vpcmpgtw':2,'vpcmpgtd':2,'vpcmpgtq':2,'vpcmpgtb':2,
        'vpsadbw':2,'vmpsadbw':2,

        'vpand':3,'vpandn':3,
        'vpor':3,'vpxor':3,
        'vpsllw':3,'vpslld':3,'vpsllq':3,
        'vpslldq':3,'vpsllvd':3,'vpsllvq':3,
        'vpsraw':3,'vpsrad':3,'vpsravd':3,
        'vpsrlw':3,'vpsrld':3,'vpsrlq':3,
        'vpsrldq':3,'vpsrlvd':3,'vpsrlvq':3,

        'vpalignr':2,'vpavgw':2,'vpavgb':2,
        'vpblendw':2,'vpblendd':2,'vpblendvb':2,
        'vpbroadcastb':2,'vpbroadcastd':2,'vpbroadcastq':2,'vbroadcasti128':2,
        'vextracti128':2,'vinserti128':2,'vperm2i128':2,
        'vpermq':2,'vpermpd':2,'vpermd':2,'vpermps':2,
        'vpshufd':2,'vpshufb':2,'vpshufhw':2,'vpshuflw':2,
        'vpsignw':2,'vpsignd':2,'vpsignb':2,
        'vpgatherdd':2,'vpgatherdq':2,'vpgatherpd':2,'vpgatherps':2,'vpgatherqd':2,'vpgatherqq':2,
        'vpacksswb':2,'vpackssdw':2,'vpackuswb':2,'vpackusdw':2,
        'vpunpckhwd':2,'vpunpckhdq':2,'vpunpckhqdq':2,'vpunpckhbw':2,
        'vpunpcklwd':2,'vpunpckldq':2,'vpunpcklqdq':2,'vpunpcklbw':2,
        'vmovntdqa':2
    }

AVX512_I = {'vp4dpwssd':2,'vp4dpwssds':2,'v4fmaddps':2,'v4fmaddss':2,'v4fnmaddps':2,'v4fnmaddss':2,
        'vpmovwb':2,'vpmovdw':2,'vpmovsxdq':2,'vpmovdb':2,'vpmovqw':2,'vpmovqd':2,'vpmovqb':2,
        'vpmovzxwd':2,'vpmovzxwq':2,'vpmovzxdq':2,'vpmovzxbw':2,'vpmovzxbd':2,'vpmovzxbq':2,
        'vpmovswb':2,'vpmovsdw':2,'vpmovsdb':2,'vpmovsqw':2,'vpmovsqd':2,'vpmovsqb':2,
        'vpmovuswb':2,'vpmovusdw':2,'vpmovusdb':2,'vpmovusqw':2,'vpmovusqd':2,'vpmovusqb':2,'vdbpsadbw':2,
        'vmovdqa32':2,'vmovdqa64':2,'vmovsd':2,'vmovss':2,'vmovdqu8':2,'vmovdqu16':2,'vmovdqu32':2,'vmovdqu64':2,
        'vmovddup':2,'vmovshdup':2,'vmovsldup':2,'vpmovw2m':2,'vpmovd2m':2,'vpmovq2m':2,'vpmovb2m':2,
        'vpmovm2w':2,'vpmovm2d':2,'vpmovm2q':2,'vpmovm2b':2,'vmovntdq':2,
        'kmovw':2,'kmovd':2,'kmovq':2,'kmovb':2,
        'vpmaxsq':2,'vpmaxuq':2,'vmaxsd':2,'vmaxss':2,
        'vpminsq':2,'vpminuq':2,'vminsd':2,'vminss':2,
        'valignd':2,'valignq':2,
        'vpblendmw':2,'vpblendmd':2,'vpblendmq':2,'vpblendmb':2,'vblendmpd':2,'vblendmps':2,
        'vcvtqq2pd':2,'vcvtuqq2pd':2,'vcvtqq2ps':2,'vcvtuqq2ps':2,
        'vcvtsi2ss':2,'vcvtusi2ss':2,'vcvtsi2sd':2,'vcvtusi2sd':2,
        'vcvtpd2qq':2,'vcvtpd2uqq':2,'vcvtsd2si':2,'vcvtsd2usi':2,
        'vcvtps2qq':2,'vcvtss2si':2,'vcvtph2ps':2,
        'vcvtps2ph':2,'vcvtsd2ss':2,'vcvtss2sd':2,
        'vcvtudq2ps':2,'vcvtudq2pd':2,
        'vcvtss2usi':2,'vcvtpd2udq':2,
        'vcvtps2udq':2,'vcvtps2uqq':2,
        'vcvtne2ps2bf16':2,'vcvtneps2bf16':2,
        'vcvttpd2qq':2,'vcvttpd2uqq':2,'vcvttps2qq':2,'vcvttps2uqq':2,
        'vcvttsd2si':2,'vcvttsd2usi':2,'vcvttss2si':2,'vcvttss2usi':2,
        'vcvttps2udq':2,'vcvttpd2udq':2,

        'vaddsd':2,'vaddss':2,
        'kaddb':2,'kaddw':2,'kaddd':2,'kaddq':2,
        'vsubsd':2,'vsubss':2,
        'vmulsd':2,'vmulss':2,'vpmultishiftqb':2,
        'vdivsd':2,'vdivss':2,
        'vpmadd52huq':2,'vpmadd52luq':2,'vpabsq':2,
        'vpcmpb':2,'vpcmpw':2,'vpcmpd':2,'vpcmpq':2,
        'vpcmpub':2,'vpcmpuw':2,'vpcmpud':2,'vpcmpuq':2,
        'vcomisd':2,'vcomiss':2,'vucomiss':2,
        'vfmadd132pd':2,'vfmadd213pd':2,'vfmadd231pd':2,
        'vfmadd132ps':2,'vfmadd213ps':2,'vfmadd231ps':2,
        'vfmadd132sd':2,'vfmadd213sd':2,'vfmadd231sd':2,
        'vfmadd132ss':2,'vfmadd213ss':2,'vfmadd231ss':2,
        'vfmaddsub132pd':2,'vfmaddsub213pd':2,'vfmaddsub231pd':2,
        'vfmaddsub132ps':2,'vfmaddsub213ps':2,'vfmaddsub231ps':2,
        'vfmsub132pd':2,'vfmsub213pd':2,'vfmsub231pd':2,
        'vfmsub132ps':2,'vfmsub213ps':2,'vfmsub231ps':2,
        'vfmsub132sd':2,'vfmsub213sd':2,'vfmsub231sd':2,
        'vfmsub132ss':2,'vfmsub213ss':2,'vfmsub231ss':2,
        'vfmsubadd132pd':2,'vfmsubadd213pd':2,'vfmsubadd231pd':2,
        'vfmsubadd132ps':2,'vfmsubadd213ps':2,'vfmsubadd231ps':2,
        'vfnmadd132pd':2,'vfnmadd213pd':2,'vfnmadd231pd':2,
        'vfnmadd132ps':2,'vfnmadd213ps':2,'vfnmadd231ps':2,
        'vfnmadd132sd':2,'vfnmadd213sd':2,'vfnmadd231sd':2,
        'vfnmadd132ss':2,'vfnmadd213ss':2,'vfnmadd231ss':2,
        'vsqrtps':2,'vsqrtsd':2,'vsqrtss':2,  
        'vrsqrt14pd':2,'vrsqrt14ps':2,'vrsqrt14sd':2,'vrsqrt14ss':2,
        'vrsqrt28pd':2,'vrsqrt28ps':2,'vrsqrt28sd':2,'vrsqrt28ss':2,

        'kandb':2,'kandw':2,'kandd':2,'kandq':2,
        'kandnb':2,'kandnw':2,'kandnd':2,'kandnq':2,
        'vpandq':2,'vpandd':2,'vpandnd':2,'vpandnq':2,
        'knotb':2,'knotw':2,'knotd':2,'knotq':2,
        'korb':2,'korw':2,'kord':2,'korq':2,
        'kxorb':2,'kxorw':2,'kxord':2,'kxorq':2,
        'vpord':2,'vporq':2,'vpxord':2,'vpxorq':2,
        'kxnorb':2,'kxnorw':2,'kxnord':2,'kxnorq':2,
        'ktestb':2,'ktestw':2,'ktestd':2,'ktestq':2,
        'kortestb':2,'kortestw':2,'kortestd':2,'kortestq':2,
        'vptestmb':2,'vptestmw':2,'vptestmd':2,'vptestmq':2,
        'vptestnmb':2,'vptestnmw':2,'vptestnmd':2,'vptestnmq':2,
        'kshiftlb':2,'kshiftlw':2,'kshiftld':2,'kshiftlq':2,
        'kshiftrb':2,'kshiftrw':2,'kshiftrd':2,'kshiftrq':2,
        'vpshldw':2,'vpshldd':2,'vpshldq':2,'vpshldvw':2,'vpshldvd':2,'vpshldvq':2,
        'vpshrdw':2,'vpshrdd':2,'vpshrdq':2,'vpshrdvw':2,'vpshrdvd':2,'vpshrdvq':2,
        'vpsllvw':2,'vpsravw':2,'vpsravq':2,'vpsrlvw':2,
            
            
        'vbroadcastf32x2':2,'vbroadcastf32x4':2,'vbroadcastf32x8':2,
        'vbroadcastf64x2':2,'vbroadcastf64x4':2,
        'vbroadcasti32x2':2,'vbroadcasti32x4':2,'vbroadcasti32x8':2,
        'vbroadcasti64x2':2,'vbroadcasti64x4':2,
        'vpbroadcastmb2q':2,'vpbroadcastmw2d':2,


        'vpshufbitqmb':2,
        'vcompresspd':2,'vcompressps':2,'vcompresspw':2,
        'vpcompressw':2,'vpcompressd':2,'vpcompressq':2,'vpcompressb':2,
        'vpconflictd':2,'vpconflictq':2,
        'vdpbf16ps':2,'vpdpbusd':2,'vpdpbusds':2,'vpdpwssd':2,'vpdpwssds':2,
        'vexp2pd':2,'vexp2ps':2,'vfixupimmpd':2,'vfixupimmps':2,'vfixupimmsd':2,'vfixupimmss':2,
        'vpexpandw':2,'vpexpandd':2,'vpexpandq':2,'vpexpandb':2,'vexpandpd':2,'vexpandps':2,
        'vextractf32x4':2,'vextractf32x8':2,'vextractf64x2':2,'vextractf64x4':2,
        'vextracti32x4':2,'vextracti32x8':2,'vextracti64x2':2,'vextracti64x4':2,
        'vfpclasspd':2,'vfpclassps':2,'vfpclasssd':2,'vfpclassss':2,
        'vgetexppd':2,'vgetexpps':2,'vgetexpsd':2,'vgetexpss':2,
        'vgetmantpd':2,'vgetmantps':2,'vgetmantsd':2,'vgetmantss':2,'vgatherdps':2,'vgatherdpd':2,'vgatherqpd':2,'vgatherqps':2,
        'vpscatterdd':2,'vscatterdps':2,'vpscatterdq':2,'vscatterdpd':2,'vpscatterqd':2,'vpscatterqq':2,'vscatterqpd':2,'vscatterqps':2,
        'vinsertf32x4':2,'vinsertf32x8':2,'vinsertf64x2':2,'vinsertf64x4':2,
        'vinserti32x4':2,'vinserti32x8':2,'vinserti64x2':2,'vinserti64x4':2,
        'kunpckbw':2,'kunpckbq':2,'kunpckbd':2,
        'vplzcntd':2,'vplzcntq':2,
        'vpermt2w':2,'vpermt2d':2,'vpermt2q':2,'vpermt2b':2,'vpermt2pd':2,'vpermt2ps':2,
        'vpermi2w':2,'vpermi2d':2,'vpermi2q':2,'vpermi2b':2,'vpermi2pd':2,'vpermi2ps':2,
        'vpermw':2,'vpermb':2,'vpopcntw':2,'vpopcntd':2,'vpopcntq':2,'vpopcntb':2,
        'vgatherpf0dps':2,'vgatherpf1dps':2,'vgatherpf0dpd':2,'vgatherpf1dpd':2,
        'vgatherpf0qpd':2,'vgatherpf1qpd':2,'vgatherpf0qps':2,'vgatherpf0qps':2,
        'vscatterpf0dps':2,'vscatterpf0dps':2,'vscatterpf0dpd':2,'vscatterpf1dpd':2,
        'vscatterpf0qpd':2,'vscatterpf1qpd':2,'vscatterpf0qps':2,'vscatterpf0qps':2,
        'vrangepd':2,'vrangeps':2,'vrangesd':2,'vrangess':2,
        'vrcp14pd':2,'vrcp14ps':2,'vrcp14sd':2,'vrcp14ss':2,
        'vrcp28pd':2,'vrcp28ps':2,'vrcp28sd':2,'vrcp28ss':2,
        'vreducepd':2,'vreduceps':2,'vreducesd':2,'vreducess':2,
        'vprold':2,'vprolq':2,'vprolvd':2,'vprolvq':2,
        'vprord':2,'vprorq':2,'vprorvd':2,'vprorvq':2,
        'vrndscalepd':2,'vrndscaleps':2,'vrndscalesd':2,'vrndscaless':2,
        'vscalefpd':2,'vscalefps':2,'vscalefsd':2,'vscalefss':2,
        'vshuff32x4':2,'vshuff64x2':2,'vshufi32x4':2,'vshufi64x2':2,
        'vpternlogd':2,'vpternlogq':2,

        #'vpmovsxwd':2,'vpmovsxwq':2,'vpmovsxbw':2,'vpmovsxbd':2,'vpmovsxbq':2,
        #'vmovapd':2,'vmovaps':2,'vmovupd':2,'vmovups':2,'vmovntdqa':2,'vmovntpd':2,'vmovntps':2,
        #'vpaddw':2,'vpaddd':2,'vpaddq':2,'vpaddb':2,'vaddpd':2,'vaddps':2,'vpaddsw':2,'vpaddsb':2,'vpaddusw':2,'vpaddusb':2,
        #'vpsubw':2,'vpsubd':2,'vpsubq':2,'vpsubb':2,'vsubpd':2,'vsubps':2,'vpsubsw':2,'vpsubsb':2,'vpsubusw':2,'vpsubusb':2,
        #'vpabsw':2,'vpabsd':2,
        #'vpmuldq':2,'vpmuludq':2,'vmulpd':2,'vmulps':2,'vpmulhw':2,'vpmulhuw':2,'vpmulhrsw':2,'vpmullw':2,'vpmulld':2,'vpmullq':2,
        #'vdivpd':2,'vdivps':2,
        #'vandpd':2,'vandps':2,'vandnpd':2,'vandnps':2,
        #'vorpd':2,'vorps':2,
        #'vxorpd':2,'vxorps':2,
        #'vcmppd':2,'vcmpps':2,'vcmpsd':2,'vcmpss':2,'vpcmpeqd':2,'vpcmpeqq':2,'vpcmpgtq':2,
        #'vpmaxsw':2,'vpmaxsd':2,'vpmaxsb':2,'vpmaxuw':2,'vpmaxud':2,'vpmaxub':2,
        #'vpminsw':2,'vpminsd':2,'vpminsb':2,'vpminuw':2,'vpminud':2,'vpminub':2,
        #'vpslldq':2,'vpsrldq':2,
        #'vpsllw':2,'vpslld':2,'vpsllq':2,'vpsllvd':2,'vpsllvq':2,
        #'vpsraw':2,'vpsrad':2,'vpsraq':2,'vpsravd':2,
        #'vpsrlw':2,'vpsrld':2,'vpsrlq':2,'vpsrlvd':2,'vpsrlvq':2,
        #'vpbroadcastb':2,'vpbroadcastd':2,'vpbroadcastq':2,'vbroadcastsd':2,'vbroadcastss':2,'vpbroadcastw':2,
        #'vcvtdq2ps':2,'vcvtpd2dq':2,'vcvtpd2ps':2,'vcvtps2dq':2,'vcvtps2pd':2,'vcvtdq2pd':2,'vcvttpd2dq':2,'vcvttps2dq':2,
        #'vpalignr':2,'vpgatherdd':2,'vpgatherdq':2,'vpgatherqd':2,'vpgatherqq':2,
        #'vpavgw':2,'vpavgb':2,
        #'vpmaddwd':2,'vpmaddubsw':2,
        #'vpermq':2,'vpermd':2,'vpermpd':2,'vpermps':2,'vpermilpd':2,'vpermilps':2,
        #'vpacksswb':2,'vpackssdw':2,'vpackuswb':2,'vpackusdw':2,
        #'vpsadbw':2,'vsqrtpd':2,
        #'vpshufd':2,'vpshufb':2,'vshufpd':2,'vshufps':2,'vpshufhw':2,'vpshuflw':2,
        #'vpunpckhwd':2,'vpunpckhdq':2,'vpunpckhqdq':2,'vpunpckhbw':2,
        #'vpunpcklwd':2,'vpunpckldq':2,'vpunpcklqdq':2,'vpunpcklbw':2,
        #'vunpckhpd':2,'vunpckhps':2,'vunpcklpd':2,'vunpcklps':2
        }

BMI_I = {'andn':3,'bextr':2,'blsi':2,'blsmsk':2,'blsr':2,'tzcnt':2}

BMI2_I = {'bzhi':2,'pdep':2,'pext':2,

        'mulx':2,

        'sarx':3,'shlx':3,'shrx':3,'rorx':3
        }

AES_I = {'aesdec':2,'aesdeclast':2,'aesenc':2,'aesenclast':2,'aesimc':2,'aeskeygenassist':2,
        'vaesdec':2,'vaesdeclast':2,'vaesenc':2,'vaesenclast':2,'vaesimc':2,'vaeskeygenassist':2}

SHA_I = {'sha1msg1':2,'sha1msg2':2,'sha1nexte':2,'sha1rnds4':2,'sha256msg1':2,'sha256msg2':2,'sha256rnds2':2}

XOP_I = {'vprotb':2,'vprotw':2,'vprotd':2,'vprotq':2}

O_I = {'pclmulqdq':2,'vpclmulqdq':2,'rdrand':2,'rdseed':2}

#------------------------------------------------------ARM Framework-----------------------------------------------


'''
mips_TI = {'j':2,'b':2,'bc1f':2,'bc1fl':2,'bc1t':2,'bc1tl':2,'bc2f':2,'bc2fl':2,'bc2t':2,'bc2tl':2,
            'beq':2,'beql':2,'bgez':2,'bgezl':2,'bgtz':2,'bgtzl':2,'blez':2,'blezl':2,'bltz':2,'bltzl':2,
            'bne':2,'bnel':2}
mips_CI = {'jal':2, 'jalr':2,'bal':2,'bgezal':2,'bgezall':2,'bltzal':2,'bltzall':2}
mips_AI = {'add':2, 'addu':2, 'addi':2,'addiu':2,'add.s':2,'add.d':2,'madd':2,'maddu':2,
            'sub':2,'subu':2,'sub,s':2,'sub.d':2,'msub':2,'msubu':2,
            'mul':2,'mult':2,'multu':2,'mul.s':2,'mul.d':2,
            'div':2,'divu':2,'div.s':2,'div.d':2,
            'abs.s':2,'abs.d':2,'neg.s':2,'neg.d':2,}
mips_BI = {'and':2, 'andi':2, 'nor':2,'or':2,'ori':2,'xor':2,'xori':2,
            'sll':2,'sllv':2,'sra':2,'srav':2,'srl':2,'srlv':2}
'''