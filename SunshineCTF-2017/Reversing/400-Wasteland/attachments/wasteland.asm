   0x0000000000400ab7 <+0>:	push   rbp
   0x0000000000400ab8 <+1>:	mov    rbp,rsp
   0x0000000000400abb <+4>:	sub    rsp,0x370
   0x0000000000400ac2 <+11>:	mov    rax,QWORD PTR fs:0x28
   0x0000000000400acb <+20>:	mov    QWORD PTR [rbp-0x8],rax
   0x0000000000400acf <+24>:	xor    eax,eax
   0x0000000000400ad1 <+26>:	mov    edi,0x401340
   0x0000000000400ad6 <+31>:	call   0x4006a0 <puts@plt>
   0x0000000000400adb <+36>:	mov    rdx,QWORD PTR [rip+0x2015ae]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400ae2 <+43>:	lea    rax,[rbp-0x200]
   0x0000000000400ae9 <+50>:	mov    esi,0x32
   0x0000000000400aee <+55>:	mov    rdi,rax
   0x0000000000400af1 <+58>:	call   0x400700 <fgets@plt>
   0x0000000000400af6 <+63>:	lea    rax,[rbp-0x200]
   0x0000000000400afd <+70>:	mov    edx,0x3
   0x0000000000400b02 <+75>:	mov    esi,0x40137a
   0x0000000000400b07 <+80>:	mov    rdi,rax
   0x080488ec <+90>: call   0x8048540 <strncmp@plt>
   0x080488f1 <+95>: add    esp,0x10
   0x080488f4 <+98>: test   eax,eax
   0x080488f6 <+100>:   jne    0x804890d <main+123>
   0x080488f8 <+102>:   sub    esp,0xc
   0x080488fb <+105>:   push   0x8049280
   0x08048900 <+110>:   call   0x80484d0 <puts@plt>
   0x08048905 <+115>:   add    esp,0x10
   0x08048908 <+118>:   call   0x80486c6 <end_of_journey>
   0x0804890d <+123>:   sub    esp,0x4
   0x08048910 <+126>:   push   0x5
   0x08048912 <+128>:   push   0x80492a3
   0x08048917 <+133>:   lea    eax,[ebp-0x200]
   0x0804891d <+139>:   push   eax
   0x0000000000400b3b <+132>: call   0x400690 <strncmp@plt>
   0x0000000000400b40 <+137>: test   eax,eax
   0x0000000000400b42 <+139>: jne    0x400d18 <main+609>
   0x0000000000400b48 <+145>: mov    edi,0x4013b0
   0x0000000000400b4d <+150>: call   0x4006a0 <puts@plt>
   0x0000000000400b52 <+155>: mov    rdx,QWORD PTR [rip+0x201537]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400b59 <+162>: lea    rax,[rbp-0x310]
   0x0000000000400b60 <+169>: mov    esi,0x14
   0x0000000000400b65 <+174>: mov    rdi,rax
   0x0000000000400b68 <+177>: call   0x400700 <fgets@plt>
   0x0000000000400b6d <+182>: lea    rax,[rbp-0x2d0]
   0x0000000000400b74 <+189>: movabs rcx,0x6e616c6574736177
   0x0000000000400b7e <+199>: mov    QWORD PTR [rax],rcx
   0x0000000000400b81 <+202>: mov    WORD PTR [rax+0x8],0x64
   0x0000000000400b87 <+208>: lea    rax,[rbp-0x2d0]
   0x0000000000400b8e <+215>: mov    rdi,rax
   0x0000000000400b91 <+218>: call   0x4006a0 <puts@plt>
   0x0000000000400b96 <+223>: mov    rdx,QWORD PTR [rip+0x2014f3]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400b9d <+230>: lea    rax,[rbp-0x2f0]
   0x0000000000400ba4 <+237>: mov    esi,0x14
   0x0000000000400ba9 <+242>: mov    rdi,rax
   0x0000000000400bac <+245>: call   0x400700 <fgets@plt>
   0x0000000000400bb1 <+250>: lea    rdx,[rbp-0x2d0]
   0x0000000000400bb8 <+257>: lea    rax,[rbp-0x310]
   0x0000000000400bbf <+264>: mov    rsi,rdx
   0x0000000000400bc2 <+267>: mov    rdi,rax
   0x0000000000400bc5 <+270>: call   0x400730 <strcat@plt>
   0x0000000000400bca <+275>: lea    rax,[rbp-0x310]
   0x0000000000400bd1 <+282>: mov    rdi,rax
   0x0000000000400bd4 <+285>: call   0x4006c0 <strlen@plt>
   0x0000000000400bd9 <+290>: mov    DWORD PTR [rbp-0x35c],eax
   0x0000000000400bdf <+296>: lea    rax,[rbp-0x2f0]
   0x0000000000400be6 <+303>: mov    rdi,rax
   0x0000000000400be9 <+306>: call   0x4006b0 <atof@plt>
   0x0000000000400bee <+311>: cvttsd2si eax,xmm0
   0x0000000000400bf2 <+315>: mov    DWORD PTR [rbp-0x358],eax
   0x0000000000400bf8 <+321>: mov    eax,DWORD PTR [rbp-0x35c]
   0x0000000000400bfe <+327>: cmp    eax,DWORD PTR [rbp-0x358]
   0x0000000000400c04 <+333>: jne    0x400d18 <main+609>
   0x0000000000400c0a <+339>: mov    rdx,QWORD PTR [rip+0x20147f]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400c11 <+346>: lea    rax,[rbp-0x2b0]
   0x0000000000400c18 <+353>: mov    esi,0x14
   0x0000000000400c1d <+358>: mov    rdi,rax
   0x0000000000400c20 <+361>: call   0x400700 <fgets@plt>
   0x0000000000400c25 <+366>: lea    rax,[rbp-0x2b0]
   0x0000000000400c2c <+373>: mov    rdi,rax
   0x0000000000400c2f <+376>: call   0x4006b0 <atof@plt>
   0x0000000000400c34 <+381>: cvttsd2si eax,xmm0
   0x0000000000400c38 <+385>: mov    DWORD PTR [rbp-0x354],eax
   0x0000000000400c3e <+391>: sar    DWORD PTR [rbp-0x354],0x2
   0x0000000000400c45 <+398>: shl    DWORD PTR [rbp-0x354],0x4
   0x0000000000400c4c <+405>: sar    DWORD PTR [rbp-0x354],1
   0x0000000000400c52 <+411>: shl    DWORD PTR [rbp-0x354],0x4
   0x0000000000400c59 <+418>: sar    DWORD PTR [rbp-0x354],0x4
   0x0000000000400c60 <+425>: shl    DWORD PTR [rbp-0x354],0x9
   0x0000000000400c67 <+432>: sar    DWORD PTR [rbp-0x354],0x5
   0x0000000000400c6e <+439>: shl    DWORD PTR [rbp-0x354],0x4
   0x0000000000400c75 <+446>: sar    DWORD PTR [rbp-0x354],0x3
   0x0000000000400c7c <+453>: shl    DWORD PTR [rbp-0x354],0x2
   0x0000000000400c83 <+460>: mov    rdx,QWORD PTR [rip+0x201406]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400c8a <+467>: lea    rax,[rbp-0x270]
   0x0000000000400c91 <+474>: mov    esi,0x14
   0x0000000000400c96 <+479>: mov    rdi,rax
   0x0000000000400c99 <+482>: call   0x400700 <fgets@plt>
   0x0000000000400c9e <+487>: lea    rax,[rbp-0x270]
   0x0000000000400ca5 <+494>: mov    rdi,rax
   0x0000000000400ca8 <+497>: call   0x4006b0 <atof@plt>
   0x0000000000400cad <+502>: cvttsd2si eax,xmm0
   0x0000000000400cb1 <+506>: mov    DWORD PTR [rbp-0x350],eax
   0x0000000000400cb7 <+512>: mov    eax,DWORD PTR [rbp-0x354]
   0x0000000000400cbd <+518>: cmp    eax,DWORD PTR [rbp-0x350]
   0x0000000000400cc3 <+524>: jne    0x400cea <main+563>
   0x0000000000400cc5 <+526>: mov    esi,0x401228
   0x0000000000400cca <+531>: mov    edi,0x4013af
   0x0000000000400ccf <+536>: call   0x400720 <fopen@plt>
   0x0000000000400cd4 <+541>: mov    QWORD PTR [rbp-0x328],rax
   0x0000000000400cdb <+548>: mov    rax,QWORD PTR [rbp-0x328]
   0x0000000000400ce2 <+555>: mov    rdi,rax
   0x0000000000400ce5 <+558>: call   0x400986 <pathfinding>
   0x0000000000400cea <+563>: lea    rax,[rbp-0x200]
   0x0000000000400cf1 <+570>: mov    edx,0x4
   0x0000000000400cf6 <+575>: mov    esi,0x4013b1
   0x0000000000400cfb <+580>: mov    rdi,rax
   0x08048b52 <+704>:   call   0x8048540 <strncmp@plt>
   0x08048b57 <+709>:   add    esp,0x10
   0x08048b5a <+712>:   test   eax,eax
   0x08048b5c <+714>:   jne    0x8048d6d <main+1243>
   0x08048b62 <+720>:   sub    esp,0xc
   0x08048b65 <+723>:   push   0x80492b4
   0x08048b6a <+728>:   call   0x80484d0 <puts@plt>
   0x08048b6f <+733>:   add    esp,0x10
   0x08048b72 <+736>:   mov    eax,ds:0x804b060
   0x08048b77 <+741>:   sub    esp,0x4
   0x08048b7a <+744>:   push   eax
   0x08048b7b <+745>:   push   0x14
   0x08048b7d <+747>:   lea    eax,[ebp-0x2be]
   0x08048b83 <+753>:   push   eax
   0x08048b84 <+754>:   call   0x80484a0 <fgets@plt>
   0x08048b89 <+759>:   add    esp,0x10
   0x08048b8c <+762>:   mov    eax,ds:0x804b060
   0x08048b91 <+767>:   sub    esp,0x4
   0x08048b94 <+770>:   push   eax
   0x08048b95 <+771>:   push   0x14
   0x08048b97 <+773>:   lea    eax,[ebp-0x2aa]
   0x08048b9d <+779>:   push   eax
   0x08048b9e <+780>:   call   0x80484a0 <fgets@plt>
   0x08048ba3 <+785>:   add    esp,0x10
   0x08048ba6 <+788>:   mov    eax,ds:0x804b060
   0x08048bab <+793>:   sub    esp,0x4
   0x08048bae <+796>:   push   eax
   0x08048baf <+797>:   push   0x14
   0x08048bb1 <+799>:   lea    eax,[ebp-0x296]
   0x08048bb7 <+805>:   push   eax
   0x08048bb8 <+806>:   call   0x80484a0 <fgets@plt>
   0x08048bbd <+811>:   add    esp,0x10
   0x08048bc0 <+814>:   sub    esp,0xc
   0x08048bc3 <+817>:   lea    eax,[ebp-0x296]
   0x08048bc9 <+823>:   push   eax
   0x08048bca <+824>:   call   0x8048530 <atof@plt>
   0x08048bcf <+829>:   add    esp,0x10
   0x08048bd2 <+832>:   fnstcw WORD PTR [ebp-0x32e]
   0x08048bd8 <+838>:   movzx  eax,WORD PTR [ebp-0x32e]
   0x08048bdf <+845>:   mov    ah,0xc
   0x08048be1 <+847>:   mov    WORD PTR [ebp-0x330],ax
   0x08048be8 <+854>:   fldcw  WORD PTR [ebp-0x330]
   0x08048bee <+860>:   fistp  DWORD PTR [ebp-0x300]
   0x08048bf4 <+866>:   fldcw  WORD PTR [ebp-0x32e]
   0x08048bfa <+872>:   mov    DWORD PTR [ebp-0x2fc],0xdead
   0x08048c04 <+882>:   mov    eax,DWORD PTR [ebp-0x300]
   0x08048c0a <+888>:   xor    eax,DWORD PTR [ebp-0x2fc]
   0x08048c10 <+894>:   mov    DWORD PTR [ebp-0x2f8],eax
   0x08048c16 <+900>:   cmp    DWORD PTR [ebp-0x2f8],0x32
   0x08048c1d <+907>:   jne    0x8048d6d <main+1243>
   0x08048c23 <+913>:   mov    DWORD PTR [ebp-0x2f4],0x0
   0x08048c2d <+923>:   mov    DWORD PTR [ebp-0x2f0],0xffffffff
   0x08048c37 <+933>:   mov    eax,DWORD PTR [ebp-0x2fc]
   0x08048c3d <+939>:   or     eax,DWORD PTR [ebp-0x300]
   0x08048c43 <+945>:   mov    DWORD PTR [ebp-0x2f0],eax
   0x08048c49 <+951>:   mov    eax,DWORD PTR [ebp-0x2f4]
   0x08048c4f <+957>:   or     DWORD PTR [ebp-0x300],eax
   0x08048c55 <+963>:   mov    eax,DWORD PTR [ebp-0x2f0]
   0x08048c5b <+969>:   or     eax,DWORD PTR [ebp-0x2fc]
   0x08048c61 <+975>:   mov    DWORD PTR [ebp-0x2ec],eax
   0x08048c67 <+981>:   mov    eax,DWORD PTR [ebp-0x2ec]
   0x08048c6d <+987>:   or     eax,DWORD PTR [ebp-0x300]
   0x08048c73 <+993>:   mov    DWORD PTR [ebp-0x2f4],eax
   0x08048c79 <+999>:   mov    eax,DWORD PTR [ebp-0x2f0]
   0x08048c7f <+1005>:  or     eax,DWORD PTR [ebp-0x2f4]
   0x08048c85 <+1011>:  mov    DWORD PTR [ebp-0x2fc],eax
   0x08048c8b <+1017>:  mov    eax,DWORD PTR [ebp-0x2f0]
   0x08048c91 <+1023>:  and    eax,DWORD PTR [ebp-0x2f4]
   0x08048c97 <+1029>:  mov    DWORD PTR [ebp-0x300],eax
   0x08048c9d <+1035>:  mov    eax,DWORD PTR [ebp-0x300]
   0x08048ca3 <+1041>:  and    eax,DWORD PTR [ebp-0x2ec]
   0x08048ca9 <+1047>:  mov    DWORD PTR [ebp-0x2fc],eax
   0x08048caf <+1053>:  mov    eax,DWORD PTR [ebp-0x2fc]
   0x08048cb5 <+1059>:  xor    eax,DWORD PTR [ebp-0x2f0]
   0x08048cbb <+1065>:  mov    DWORD PTR [ebp-0x2f4],eax
   0x08048cc1 <+1071>:  mov    eax,DWORD PTR [ebp-0x300]
   0x08048cc7 <+1077>:  xor    eax,DWORD PTR [ebp-0x2f4]
   0x08048ccd <+1083>:  mov    DWORD PTR [ebp-0x2f0],eax
   0x08048cd3 <+1089>:  mov    eax,DWORD PTR [ebp-0x2f4]
   0x08048cd9 <+1095>:  xor    DWORD PTR [ebp-0x2ec],eax
   0x08048cdf <+1101>:  mov    eax,ds:0x804b060
   0x08048ce4 <+1106>:  sub    esp,0x4
   0x08048ce7 <+1109>:  push   eax
   0x08048ce8 <+1110>:  push   0x14
   0x08048cea <+1112>:  lea    eax,[ebp-0x264]
   0x08048cf0 <+1118>:  push   eax
   0x08048cf1 <+1119>:  call   0x80484a0 <fgets@plt>
   0x08048cf6 <+1124>:  add    esp,0x10
   0x08048cf9 <+1127>:  sub    esp,0xc
   0x08048cfc <+1130>:  lea    eax,[ebp-0x264]
   0x08048d02 <+1136>:  push   eax
   0x08048d03 <+1137>:  call   0x8048530 <atof@plt>
   0x08048d08 <+1142>:  add    esp,0x10
   0x08048d0b <+1145>:  fnstcw WORD PTR [ebp-0x32e]
   0x08048d11 <+1151>:  movzx  eax,WORD PTR [ebp-0x32e]
   0x08048d18 <+1158>:  mov    ah,0xc
   0x08048d1a <+1160>:  mov    WORD PTR [ebp-0x330],ax
   0x08048d21 <+1167>:  fldcw  WORD PTR [ebp-0x330]
   0x08048d27 <+1173>:  fistp  DWORD PTR [ebp-0x2e8]
   0x08048d2d <+1179>:  fldcw  WORD PTR [ebp-0x32e]
   0x08048d33 <+1185>:  mov    eax,DWORD PTR [ebp-0x2ec]
   0x08048d39 <+1191>:  cmp    eax,DWORD PTR [ebp-0x2e8]
   0x08048d3f <+1197>:  jne    0x8048d6d <main+1243>
   0x08048d41 <+1199>:  sub    esp,0x8
   0x08048d44 <+1202>:  push   0x8049130
   0x08048d49 <+1207>:  push   0x80492da
   0x08048d4e <+1212>:  call   0x8048520 <fopen@plt>
   0x08048d53 <+1217>:  add    esp,0x10
   0x08048d56 <+1220>:  mov    DWORD PTR [ebp-0x304],eax
   0x08048d5c <+1226>:  sub    esp,0xc
   0x08048d5f <+1229>:  push   DWORD PTR [ebp-0x304]
   0x08048d65 <+1235>:  call   0x8048787 <pathfinding>
   0x08048d6a <+1240>:  add    esp,0x10
   0x08048d6d <+1243>:  sub    esp,0x4
   0x08048d70 <+1246>:  push   0x4
   0x08048d72 <+1248>:  push   0x80492dc
   0x08048d77 <+1253>:  lea    eax,[ebp-0x200]
   0x08048d7d <+1259>:  push   eax
  0x0000000000400edf <+1064>: call   0x400690 <strncmp@plt>
   0x0000000000400ee4 <+1069>:   test   eax,eax
   0x0000000000400ee6 <+1071>:   jne    0x401045 <main+1422>
   0x0000000000400eec <+1077>:   mov    edi,0x4013e8
   0x0000000000400ef1 <+1082>:   call   0x4006a0 <puts@plt>
   0x0000000000400ef6 <+1087>:   mov    DWORD PTR [rbp-0x368],0x1
   0x0000000000400f00 <+1097>:   jmp    0x400f12 <main+1115>
   0x0000000000400f02 <+1099>:   shl    DWORD PTR [rbp-0x368],1
   0x0000000000400f08 <+1105>:   mov    edi,0x401410
   0x0000000000400f0d <+1110>:   call   0x4006a0 <puts@plt>
   0x0000000000400f12 <+1115>:   cmp    DWORD PTR [rbp-0x368],0x31
   0x0000000000400f19 <+1122>:   jle    0x400f02 <main+1099>
   0x0000000000400f1b <+1124>:   mov    DWORD PTR [rbp-0x330],0x0
   0x0000000000400f25 <+1134>:   mov    rdx,QWORD PTR [rip+0x201164]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000400f2c <+1141>:   lea    rax,[rbp-0x270]
   0x0000000000400f33 <+1148>:   mov    esi,0x64
   0x0000000000400f38 <+1153>:   mov    rdi,rax
   0x0000000000400f3b <+1156>:   call   0x400700 <fgets@plt>
   0x0000000000400f40 <+1161>:   lea    rax,[rbp-0x270]
   0x0000000000400f47 <+1168>:   mov    rdi,rax
   0x0000000000400f4a <+1171>:   call   0x4006b0 <atof@plt>
   0x0000000000400f4f <+1176>:   cvttsd2si eax,xmm0
   0x0000000000400f53 <+1180>:   mov    DWORD PTR [rbp-0x330],eax
   0x0000000000400f59 <+1186>:   mov    eax,DWORD PTR [rbp-0x330]
   0x0000000000400f5f <+1192>:   cmp    eax,DWORD PTR [rbp-0x368]
   0x0000000000400f65 <+1198>:   jne    0x401045 <main+1422>
   0x08048e39 <+1447>:  mov    DWORD PTR [ebp-0x31c],0x2
   0x08048e43 <+1457>:  mov    DWORD PTR [ebp-0x320],0x0
   0x08048e4d <+1467>:  jmp    0x8048ea3 <main+1553>
   0x08048e4f <+1469>:  shl    DWORD PTR [ebp-0x31c],1
   0x08048e55 <+1475>:  add    DWORD PTR [ebp-0x31c],0xf5
   0x08048e5f <+1485>:  mov    eax,DWORD PTR [ebp-0x31c]
   0x08048e65 <+1491>:  imul   eax,eax,0x6f9
   0x08048e6b <+1497>:  mov    DWORD PTR [ebp-0x31c],eax
   0x08048e71 <+1503>:  mov    ecx,DWORD PTR [ebp-0x31c]
   0x08048e77 <+1509>:  mov    edx,0x1bd71c0f
   0x08048e7c <+1514>:  mov    eax,ecx
   0x08048e7e <+1516>:  imul   edx
   0x08048e80 <+1518>:  sar    edx,0x8
   0x08048e83 <+1521>:  mov    eax,ecx
   0x08048e85 <+1523>:  sar    eax,0x1f
   0x08048e88 <+1526>:  sub    edx,eax
   0x08048e8a <+1528>:  mov    eax,edx
   0x08048e8c <+1530>:  imul   eax,eax,0x932
   0x08048e92 <+1536>:  sub    ecx,eax
   0x08048e94 <+1538>:  mov    eax,ecx
   0x08048e96 <+1540>:  mov    DWORD PTR [ebp-0x318],eax
   0x08048e9c <+1546>:  add    DWORD PTR [ebp-0x320],0x1
   0x08048ea3 <+1553>:  cmp    DWORD PTR [ebp-0x320],0x13
   0x08048eaa <+1560>:  jle    0x8048e4f <main+1469>
   0x08048eac <+1562>:  mov    eax,ds:0x804b060
   0x08048eb1 <+1567>:  sub    esp,0x4
   0x08048eb4 <+1570>:  push   eax
   0x08048eb5 <+1571>:  push   0x32
   0x08048eb7 <+1573>:  lea    eax,[ebp-0x296]
   0x08048ebd <+1579>:  push   eax
   0x08048ebe <+1580>:  call   0x80484a0 <fgets@plt>
   0x08048ec3 <+1585>:  add    esp,0x10
   0x08048ec6 <+1588>:  sub    esp,0xc
   0x08048ec9 <+1591>:  lea    eax,[ebp-0x296]
   0x08048ecf <+1597>:  push   eax
   0x08048ed0 <+1598>:  call   0x8048530 <atof@plt>
   0x08048ed5 <+1603>:  add    esp,0x10
   0x08048ed8 <+1606>:  fnstcw WORD PTR [ebp-0x32e]
   0x08048ede <+1612>:  movzx  eax,WORD PTR [ebp-0x32e]
   0x08048ee5 <+1619>:  mov    ah,0xc
   0x08048ee7 <+1621>:  mov    WORD PTR [ebp-0x330],ax
   0x08048eee <+1628>:  fldcw  WORD PTR [ebp-0x330]
   0x08048ef4 <+1634>:  fistp  DWORD PTR [ebp-0x31c]
   0x08048efa <+1640>:  fldcw  WORD PTR [ebp-0x32e]
   0x08048f00 <+1646>:  mov    eax,DWORD PTR [ebp-0x31c]
   0x08048f06 <+1652>:  cmp    eax,DWORD PTR [ebp-0x318]
   0x08048f0c <+1658>:  jne    0x8048f3a <main+1704>
   0x08048f0e <+1660>:  sub    esp,0x8
   0x08048f11 <+1663>:  push   0x8049130
   0x08048f16 <+1668>:  push   0x8049334
   0x08048f1b <+1673>:  call   0x8048520 <fopen@plt>
   0x08048f20 <+1678>:  add    esp,0x10
   0x08048f23 <+1681>:  mov    DWORD PTR [ebp-0x304],eax
   0x08048f29 <+1687>:  sub    esp,0xc
   0x08048f2c <+1690>:  push   DWORD PTR [ebp-0x304]
   0x08048f32 <+1696>:  call   0x8048787 <pathfinding>
   0x08048f37 <+1701>:  add    esp,0x10
   0x08048f3a <+1704>:  sub    esp,0x4
   0x08048f3d <+1707>:  push   0x5
   0x08048f3f <+1709>:  push   0x8049336
   0x08048f44 <+1714>:  lea    eax,[ebp-0x200]
   0x08048f4a <+1720>:  push   eax
   0x0000000000401059 <+1442>:   call   0x400690 <strncmp@plt>
   0x000000000040105e <+1447>:   test   eax,eax
   0x0000000000401060 <+1449>:   jne    0x401181 <main+1738>
   0x0000000000401066 <+1455>:   mov    edi,0x401440
   0x000000000040106b <+1460>:   call   0x4006a0 <puts@plt>
   0x0000000000401070 <+1465>:   mov    rdx,QWORD PTR [rip+0x201019]        # 0x602090 <stdin@@GLIBC_2.2.5>
   0x0000000000401077 <+1472>:   lea    rax,[rbp-0x2b0]
   0x000000000040107e <+1479>:   mov    esi,0x5
   0x0000000000401083 <+1484>:   mov    rdi,rax
   0x0000000000401086 <+1487>:   call   0x400700 <fgets@plt>
   0x000000000040108b <+1492>:   lea    rax,[rbp-0x2b0]
   0x0000000000401092 <+1499>:   mov    rdi,rax
   0x0000000000401095 <+1502>:   call   0x4006b0 <atof@plt>
   0x000000000040109a <+1507>:   cvtsd2ss xmm2,xmm0
   0x000000000040109e <+1511>:   movss  DWORD PTR [rbp-0x32c],xmm2
   0x00000000004010a6 <+1519>:   cvtss2sd xmm0,DWORD PTR [rbp-0x32c]
   0x00000000004010ae <+1527>:   movsd  xmm1,QWORD PTR [rip+0x422]        # 0x4014d8
   0x00000000004010b6 <+1535>:   ucomisd xmm1,xmm0
   0x00000000004010ba <+1539>:   jbe    0x4010d0 <main+1561>
   0x00000000004010bc <+1541>:   mov    edi,0x401468
   0x00000000004010c1 <+1546>:   call   0x4006a0 <puts@plt>
   0x00000000004010c6 <+1551>:   mov    edi,0x0
   0x00000000004010cb <+1556>:   call   0x400740 <exit@plt>
   0x00000000004010d0 <+1561>:   cvtss2sd xmm0,DWORD PTR [rbp-0x32c]
   0x00000000004010d8 <+1569>:   ucomisd xmm0,QWORD PTR [rip+0x3f8]        # 0x4014d8
   0x00000000004010e0 <+1577>:   jbe    0x4010f6 <main+1599>
   0x00000000004010e2 <+1579>:   mov    edi,0x401471
   0x00000000004010e7 <+1584>:   call   0x4006a0 <puts@plt>
   0x00000000004010ec <+1589>:   mov    edi,0x0
   0x00000000004010f1 <+1594>:   call   0x400740 <exit@plt>
   0x00000000004010f6 <+1599>:   mov    edi,0x401480
   0x08048ffa <+1896>:  push   0x8049378
   0x08048fff <+1901>:  call   0x80484d0 <puts@plt>
   0x08049004 <+1906>:  add    esp,0x10
   0x08049007 <+1909>:  call   0x80487f2 <djb2hash>
   0x0804900c <+1914>:  mov    DWORD PTR [ebp-0x2dc],eax
   0x08049012 <+1920>:  mov    eax,ds:0x804b060
   0x08049017 <+1925>:  sub    esp,0x4
   0x0804901a <+1928>:  push   eax
   0x0804901b <+1929>:  push   0xa
   0x0804901d <+1931>:  lea    eax,[ebp-0x264]
   0x08049023 <+1937>:  push   eax
   0x08049024 <+1938>:  call   0x80484a0 <fgets@plt>
   0x08049029 <+1943>:  add    esp,0x10
   0x0804902c <+1946>:  sub    esp,0xc
   0x0804902f <+1949>:  lea    eax,[ebp-0x264]
   0x08049035 <+1955>:  push   eax
   0x08049036 <+1956>:  call   0x8048510 <atol@plt>
   0x0804903b <+1961>:  add    esp,0x10
   0x0804903e <+1964>:  mov    DWORD PTR [ebp-0x2d8],eax
   0x08049044 <+1970>:  mov    eax,DWORD PTR [ebp-0x2dc]
   0x0804904a <+1976>:  cmp    eax,DWORD PTR [ebp-0x2d8]
   0x08049050 <+1982>:  jne    0x804908e <main+2044>
   0x08049052 <+1984>:  sub    esp,0xc
   0x08049055 <+1987>:  push   0x80493c3
   0x0804905a <+1992>:  call   0x80484d0 <puts@plt>
   0x0804905f <+1997>:  add    esp,0x10
   0x08049062 <+2000>:  sub    esp,0x8
   0x08049065 <+2003>:  push   0x8049130
   0x0804906a <+2008>:  push   0x80493ce
   0x0804906f <+2013>:  call   0x8048520 <fopen@plt>
   0x08049074 <+2018>:  add    esp,0x10
   0x08049077 <+2021>:  mov    DWORD PTR [ebp-0x304],eax
   0x0804907d <+2027>:  sub    esp,0xc
   0x08049080 <+2030>:  push   DWORD PTR [ebp-0x304]
   0x08049086 <+2036>:  call   0x8048787 <pathfinding>
   0x0804908b <+2041>:  add    esp,0x10
   0x0804908e <+2044>:  mov    eax,0x0
   0x08049093 <+2049>:  mov    ecx,DWORD PTR [ebp-0xc]
   0x08049096 <+2052>:  xor    ecx,DWORD PTR gs:0x14
   0x0804909d <+2059>:  je     0x80490a4 <main+2066>
   0x0804909f <+2061>:  call   0x80484b0 <__stack_chk_fail@plt>
   0x080490a4 <+2066>:  mov    ecx,DWORD PTR [ebp-0x4]
   0x080490a7 <+2069>:  leave  
   0x080490a8 <+2070>:  lea    esp,[ecx-0x4]
   0x080490ab <+2073>:  ret   










  
