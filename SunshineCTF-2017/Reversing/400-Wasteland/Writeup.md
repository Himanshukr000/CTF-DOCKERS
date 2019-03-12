So for this challenge, we are given a assembly file. Here i'm going to go through and reverse the important bits back to the C code. Then once you have the C code, you should be able to get all of the answers either by working them out by hand, or having a C program do it for you.

```
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
```

```c
	if (strncmp(input, "End", 3) == 0)
	{
		printf("So you think you've found the end?\n");
		end_of_journey();
	}
```
```
   0x0000000000400b59 <+162>: lea    rax,[rbp-0x310]
   0x0000000000400b60 <+169>: mov    esi,0x14
   0x0000000000400b65 <+174>: mov    rdi,rax
   0x0000000000400b68 <+177>: call   0x400700 <fgets@plt>
```

```c
	fgets(string, sizeof(string), stdin);
```

```
   0x0000000000400b6d <+182>: lea    rax,[rbp-0x2d0]
   0x0000000000400b74 <+189>: movabs rcx,0x6e616c6574736177
   0x0000000000400b7e <+199>: mov    QWORD PTR [rax],rcx
   0x0000000000400b81 <+202>: mov    WORD PTR [rax+0x8],0x64
```

```c
	strcpy(given, "wasteland");
```

```
   0x0000000000400b87 <+208>: lea    rax,[rbp-0x2d0]
   0x0000000000400b8e <+215>: mov    rdi,rax
   0x0000000000400b91 <+218>: call   0x4006a0 <puts@plt>
```

```c
	printf("%s\n", given);
```

```
   0x0000000000400b9d <+230>: lea    rax,[rbp-0x2f0]
   0x0000000000400ba4 <+237>: mov    esi,0x14
   0x0000000000400ba9 <+242>: mov    rdi,rax
   0x0000000000400bac <+245>: call   0x400700 <fgets@plt>
```

```c
	fgets(answer, sizeof(answer), stdin);
```

```
   0x0000000000400bb1 <+250>: lea    rdx,[rbp-0x2d0]
   0x0000000000400bb8 <+257>: lea    rax,[rbp-0x310]
   0x0000000000400bbf <+264>: mov    rsi,rdx
   0x0000000000400bc2 <+267>: mov    rdi,rax
   0x0000000000400bc5 <+270>: call   0x400730 <strcat@plt>
```

```c
	strcat(string, given);
```

```
   0x0000000000400bca <+275>: lea    rax,[rbp-0x310]
   0x0000000000400bd1 <+282>: mov    rdi,rax
   0x0000000000400bd4 <+285>: call   0x4006c0 <strlen@plt>
   0x0000000000400bd9 <+290>: mov    DWORD PTR [rbp-0x35c],eax
```

```c
	int str_len = strlen(string);
```

```
   0x0000000000400bdf <+296>: lea    rax,[rbp-0x2f0]
   0x0000000000400be6 <+303>: mov    rdi,rax
   0x0000000000400be9 <+306>: call   0x4006b0 <atof@plt>
   0x0000000000400bee <+311>: cvttsd2si eax,xmm0
   0x0000000000400bf2 <+315>: mov    DWORD PTR [rbp-0x358],eax
```

```c
	int user_size = atof(answer);
```

```
   0x0000000000400bf8 <+321>: mov    eax,DWORD PTR [rbp-0x35c]
   0x0000000000400bfe <+327>: cmp    eax,DWORD PTR [rbp-0x358]
   0x0000000000400c04 <+333>: jne    0x400d18 <main+609>
```

```c
if (str_len == user_size)
```

```
   0x0000000000400c11 <+346>: lea    rax,[rbp-0x2b0]
   0x0000000000400c18 <+353>: mov    esi,0x14
   0x0000000000400c1d <+358>: mov    rdi,rax
   0x0000000000400c20 <+361>: call   0x400700 <fgets@plt>
```

```c
	char string[20];
	fgets(string, sizeof(string), stdin);
```

```
   0x0000000000400c25 <+366>: lea    rax,[rbp-0x2b0]
   0x0000000000400c2c <+373>: mov    rdi,rax
   0x0000000000400c2f <+376>: call   0x4006b0 <atof@plt>
   0x0000000000400c34 <+381>: cvttsd2si eax,xmm0
   0x0000000000400c38 <+385>: mov    DWORD PTR [rbp-0x354],eax
```

```c
	int final_int;
	final_int = atof(final_prompt);
```

```
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
```

```c
	final_int = final_int >> 2;
	final_int = final_int << 4;
	final_int = final_int >> 1;
	final_int = final_int << 4;
	final_int = final_int >> 4;
	final_int = final_int << 9;
	final_int = final_int >> 5;
	final_int = final_int << 4;
	final_int = final_int >> 3;
	final_int = final_int << 2;
```

```
   0x0000000000400c8a <+467>: lea    rax,[rbp-0x270]
   0x0000000000400c91 <+474>: mov    esi,0x14
   0x0000000000400c96 <+479>: mov    rdi,rax
   0x0000000000400c99 <+482>: call   0x400700 <fgets@plt>
   0x0000000000400c9e <+487>: lea    rax,[rbp-0x270]
   0x0000000000400ca5 <+494>: mov    rdi,rax
   0x0000000000400ca8 <+497>: call   0x4006b0 <atof@plt>
   0x0000000000400cad <+502>: cvttsd2si eax,xmm0
   0x0000000000400cb1 <+506>: mov    DWORD PTR [rbp-0x350],eax
```

```c
	fgets(final_answer, sizeof(final_answer), stdin);
	int last_piece = atof(final_answer);
```

```
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
```

```c
	if (final_int == last_piece)
			{
				piece = fopen("1", "r");
				pathfinding(piece);
			}
```

   0x0000000000400cea <+563>: lea    rax,[rbp-0x200]
   0x0000000000400cf1 <+570>: mov    edx,0x4
   0x0000000000400cf6 <+575>: mov    esi,0x4013b1
   0x0000000000400cfb <+580>: mov    rdi,rax
   0x08048b52 <+704>:   call   0x8048540 <strncmp@plt>
   0x08048b57 <+709>:   add    esp,0x10
   0x08048b5a <+712>:   test   eax,eax
   0x08048b5c <+714>:   jne    0x8048d6d <main+1243>```
```

```c
	if (strncmp(input, "North", 5) == 0)
	{
		printf("You head North, towards the mammoth mountains.\n");
		char string[20];
		char answer[20];
		char given[20];
		fgets(string, sizeof(string), stdin);
		strcpy(given, "wasteland");
		printf("%s\n", given);
		fgets(answer, sizeof(answer), stdin);
		strcat(string, given);
		int str_len = strlen(string);
		int user_size = atof(answer);
		if (str_len == user_size)
		{
			char final_prompt[20];
			int final_int;
			char final_answer[20];
			fgets(final_prompt, sizeof(final_prompt), stdin);
			final_int = atof(final_prompt);
			final_int = final_int >> 2;
			final_int = final_int << 4;
			final_int = final_int >> 1;
			final_int = final_int << 4;
			final_int = final_int >> 4;
			final_int = final_int << 9;
			final_int = final_int >> 5;
			final_int = final_int << 4;
			final_int = final_int >> 3;
			final_int = final_int << 2;
			fgets(final_answer, sizeof(final_answer), stdin);
			int last_piece = atof(final_answer);
			if (final_int == last_piece)
			{
				piece = fopen("1", "r");
				pathfinding(piece);
			}
			
		}	
	}
```

```c
	if (strncmp(input, "East", 4) == 0) {
```

```
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
```

```c
		fgets(xbuf0, sizeof(xbuf0), stdin);
		fgets(xbuf1, sizeof(xbuf1), stdin);
		fgets(xbuf2, sizeof(xbuf2), stdin);
		int xint0 = atof(xbuf2);
```

```
   0x08048be8 <+854>:   fldcw  WORD PTR [ebp-0x330]
   0x08048bee <+860>:   fistp  DWORD PTR [ebp-0x300]
   0x08048bf4 <+866>:   fldcw  WORD PTR [ebp-0x32e]
   0x08048bfa <+872>:   mov    DWORD PTR [ebp-0x2fc],0xdead
   0x08048c04 <+882>:   mov    eax,DWORD PTR [ebp-0x300]
   0x08048c0a <+888>:   xor    eax,DWORD PTR [ebp-0x2fc]
```

```c
	int xint1 = 0xdead;
	int product;
	product = xint0 ^ xint1;
```

```
   0x08048c10 <+894>:   mov    DWORD PTR [ebp-0x2f8],eax
   0x08048c16 <+900>:   cmp    DWORD PTR [ebp-0x2f8],0x32
   0x08048c1d <+907>:   jne    0x8048d6d <main+1243>
```

```c
	if (product == 50) {
```

```
   0x08048c23 <+913>:   mov    DWORD PTR [ebp-0x2f4],0x0
   0x08048c2d <+923>:   mov    DWORD PTR [ebp-0x2f0],0xffffffff
```

```c
	int xint2 = 0x0;
	int xint3 = 0xffffffff;
```

```
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
```

```c
	xint3 = xint1 | xint0;
	xint0 = xint2 | xint0;
	xint4 = xint3 | xint1;
	xint2 = xint4 | xint0;
	xint1 = xint3 | xint2;
	xint0 = xint3 & xint2;
	xint1 = xint0 & xint4;
	xint2 = xint1 ^ xint3;
	xint3 = xint0 ^ xint2;
	xint4 = xint4 ^ xint2; 
```

```
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
```

```c
	fgets(xbuf4, sizeof(xbuf4), stdin);
	final_x = atof(xbuf4);
```

```
   0x08048d1a <+1160>:  mov    WORD PTR [ebp-0x330],ax
   0x08048d21 <+1167>:  fldcw  WORD PTR [ebp-0x330]
   0x08048d27 <+1173>:  fistp  DWORD PTR [ebp-0x2e8]
   0x08048d2d <+1179>:  fldcw  WORD PTR [ebp-0x32e]
   0x08048d33 <+1185>:  mov    eax,DWORD PTR [ebp-0x2ec]
   0x08048d39 <+1191>:  cmp    eax,DWORD PTR [ebp-0x2e8]
   0x08048d3f <+1197>:  jne    0x8048d6d <main+1243>
```

```c
	if (xint4 == final_x) {
```

```
  0x08048d44 <+1202>:  push   0x8049130
   0x08048d49 <+1207>:  push   0x80492da
   0x08048d4e <+1212>:  call   0x8048520 <fopen@plt>
   0x08048d53 <+1217>:  add    esp,0x10
   0x08048d56 <+1220>:  mov    DWORD PTR [ebp-0x304],eax
   0x08048d5c <+1226>:  sub    esp,0xc
   0x08048d5f <+1229>:  push   DWORD PTR [ebp-0x304]
   0x08048d65 <+1235>:  call   0x8048787 <pathfinding>
```

```c
	if (strncmp(input, "East", 4) == 0)
	{
		printf("You head East, to the Great Warlands.\n");
		char xbuf0[20];
		char xbuf1[20];
		char xbuf2[20];
		char xbuf4[20];
		fgets(xbuf0, sizeof(xbuf0), stdin);
		fgets(xbuf1, sizeof(xbuf1), stdin);
		fgets(xbuf2, sizeof(xbuf2), stdin);
		int xint0 = atof(xbuf2);
		int xint1 = 0xdead;
		int product;
		product = xint0 ^ xint1;
		if (product == 50)
		{
			int final_x;
			int xint2 = 0x0;
			int xint3 = 0xffffffff;
			int xint4;
			xint3 = xint1 | xint0;
			xint0 = xint2 | xint0;
			xint4 = xint3 | xint1;
			xint2 = xint4 | xint0;
			xint1 = xint3 | xint2;
			xint0 = xint3 & xint2;
			xint1 = xint0 & xint4;
			xint2 = xint1 ^ xint3;
			xint3 = xint0 ^ xint2;
			xint4 = xint4 ^ xint2; 
			fgets(xbuf4, sizeof(xbuf4), stdin);
			final_x = atof(xbuf4);
			if (xint4 == final_x)
			{
				piece = fopen("2", "r");
				pathfinding(piece);
			}
		}
	}
```

```
   0x0000000000400edf <+1064>: call   0x400690 <strncmp@plt>
   0x0000000000400ee4 <+1069>:   test   eax,eax
   0x0000000000400ee6 <+1071>:   jne    0x401045 <main+1422>
```

```c
if (strncmp(input, "West", 4) == 0) {
```

```
   0x0000000000400ef6 <+1087>:   mov    DWORD PTR [rbp-0x368],0x1
   0x0000000000400f00 <+1097>:   jmp    0x400f12 <main+1115>
   0x0000000000400f02 <+1099>:   shl    DWORD PTR [rbp-0x368],1
   0x0000000000400f08 <+1105>:   mov    edi,0x401410
   0x0000000000400f0d <+1110>:   call   0x4006a0 <puts@plt>
   0x0000000000400f12 <+1115>:   cmp    DWORD PTR [rbp-0x368],0x31
   0x0000000000400f19 <+1122>:   jle    0x400f02 <main+1099>
```

```c
	int i = 1;
	while (i<50)
	{
		i = i*2;
		printf("The more you wander, the more you find.\n");
	}
```

```
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
```

```c
	char buf0[100];
	int check = 0;
	fgets(buf0, sizeof(buf0), stdin);
	check = atof(buf0);
```

```
   0x0000000000400f59 <+1186>:   mov    eax,DWORD PTR [rbp-0x330]
   0x0000000000400f5f <+1192>:   cmp    eax,DWORD PTR [rbp-0x368]
   0x0000000000400f65 <+1198>:   jne    0x401045 <main+1422>
```

```c
	if (check == i) {
```

```
   0x08048e39 <+1447>:  mov    DWORD PTR [ebp-0x31c],0x2
   0x08048e43 <+1457>:  mov    DWORD PTR [ebp-0x320],0x0
```

```c
		int i2 = 2;
		int i3;
```

```
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
```

```c
	for (i = 0; i < 20; i++)
	{
		i2 = i2 *2;
		i2 = i2 + 245;
			i2 = i2 * 1785;
			i3 = i2 % 2354;
	}
```

```
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
```

```c
	fgets(buf1, sizeof(buf1), stdin);
	i2 = atof(buf1);
```

```
   0x08048ef4 <+1634>:  fistp  DWORD PTR [ebp-0x31c]
   0x08048efa <+1640>:  fldcw  WORD PTR [ebp-0x32e]
   0x08048f00 <+1646>:  mov    eax,DWORD PTR [ebp-0x31c]
   0x08048f06 <+1652>:  cmp    eax,DWORD PTR [ebp-0x318]
   0x08048f0c <+1658>:  jne    0x8048f3a <main+1704>
```

```c
	if (i2 == i3) {
```

```
   0x08048f11 <+1663>:  push   0x8049130
   0x08048f16 <+1668>:  push   0x8049334
   0x08048f1b <+1673>:  call   0x8048520 <fopen@plt>
   0x08048f20 <+1678>:  add    esp,0x10
   0x08048f23 <+1681>:  mov    DWORD PTR [ebp-0x304],eax
   0x08048f29 <+1687>:  sub    esp,0xc
   0x08048f2c <+1690>:  push   DWORD PTR [ebp-0x304]
   0x08048f32 <+1696>:  call   0x8048787 <pathfinding>
```

```c
	piece = fopen("3", "r");
	pathfinding(piece);
```

```c
	if (strncmp(input, "West", 4) == 0)
	{
		printf("You head West, towards the green sea.\n");
		int i = 1;
		while (i<50)
		{
			i = i*2;
			printf("The more you wander, the more you find.\n");
		}

		char buf0[100];
		int check = 0;
		fgets(buf0, sizeof(buf0), stdin);
		check = atof(buf0);
		if (check == i)
		{
			int i2 = 2;
			int i3;
			for (i = 0; i < 20; i++)
			{
				i2 = i2 *2;
				i2 = i2 + 245;
				i2 = i2 * 1785;
				i3 = i2 % 2354;
			}
			char buf1[50];
			fgets(buf1, sizeof(buf1), stdin);
			i2 = atof(buf1);
			if (i2 == i3)
			{
				piece = fopen("3", "r");
				pathfinding(piece);
			} 
		}
	
	}
```

```
   0x08048f44 <+1714>:  lea    eax,[ebp-0x200]
   0x08048f4a <+1720>:  push   eax
   0x0000000000401059 <+1442>:   call   0x400690 <strncmp@plt>
   0x000000000040105e <+1447>:   test   eax,eax
   0x0000000000401060 <+1449>:   jne    0x401181 <main+1738>
```

```c
	if (strncmp(input, "South", 5) == 0) {
```

```
   0x0000000000401077 <+1472>:   lea    rax,[rbp-0x2b0]
   0x000000000040107e <+1479>:   mov    esi,0x5
   0x0000000000401083 <+1484>:   mov    rdi,rax
   0x0000000000401086 <+1487>:   call   0x400700 <fgets@plt>
```

```c
	char buf0[5];
	fgets(buf0, sizeof(buf0), stdin);
```

```
   0x000000000040108b <+1492>:   lea    rax,[rbp-0x2b0]
   0x0000000000401092 <+1499>:   mov    rdi,rax
   0x0000000000401095 <+1502>:   call   0x4006b0 <atof@plt>
   0x000000000040109a <+1507>:   cvtsd2ss xmm2,xmm0
   0x000000000040109e <+1511>:   movss  DWORD PTR [rbp-0x32c],xmm2
```

```c
	float f;
	f = atof(buf0);
```

```
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
```

```c
	if (f < 12.684125)
	{
		puts("Too much");
		exit(0);
	}

	if (f > 12.684125)
	{
		puts("Too little");
		exit(0);
	}
```

```
   0x08048ffa <+1896>:  push   0x8049378
   0x08048fff <+1901>:  call   0x80484d0 <puts@plt>
```

```c
	printf("Please enter 5 characters to get hashed (btw this is really an x86 binary)\n")
```

```
   0x08049007 <+1909>:  call   0x80487f2 <djb2hash>
   0x0804900c <+1914>:  mov    DWORD PTR [ebp-0x2dc],eax
```

# Is there something missing here?

```
   0x0804901b <+1929>:  push   0xa
   0x0804901d <+1931>:  lea    eax,[ebp-0x264]
   0x08049023 <+1937>:  push   eax
   0x08049024 <+1938>:  call   0x80484a0 <fgets@plt>
```

```c
	fgets(hash_prompt, sizeof(hash_prompt), stdin);
```

```
   0x0804902f <+1949>:  lea    eax,[ebp-0x264]
   0x08049035 <+1955>:  push   eax
   0x08049036 <+1956>:  call   0x8048510 <atol@plt>
   0x0804903b <+1961>:  add    esp,0x10
   0x0804903e <+1964>:  mov    DWORD PTR [ebp-0x2d8],eax
```

```c
	unsigned long hash_user = atol(hash_prompt);
```

```
   0x08049044 <+1970>:  mov    eax,DWORD PTR [ebp-0x2dc]
   0x0804904a <+1976>:  cmp    eax,DWORD PTR [ebp-0x2d8]
   0x08049050 <+1982>:  jne    0x804908e <main+2044>
```

```c
	if (hash == hash_user) {
```

```
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
```

```c
	printf("They match\n");
	piece = fopen("4", "r");
	pathfinding(piece);
```

```c
if (strncmp(input, "South", 5) == 0)
	{
		printf("You head South, to the endless marshes.\n");
		float f;
		char buf0[5];
		fgets(buf0, sizeof(buf0), stdin);
		f = atof(buf0);

		if (f < 12.684125)
		{
			puts("Too much");
			exit(0);
		}

		if (f > 12.684125)
		{
			puts("Too little");
			exit(0);
		}
		
		else
		{
			int hi;
			printf("Please enter 5 characters to get hashed (btw this is really an x86 binary)\n");
			long hash = djb2hash();
			char hash_prompt[10];
			
			fgets(hash_prompt, sizeof(hash_prompt), stdin);
			unsigned long hash_user = atol(hash_prompt);
			if (hash == hash_user)
			{
				printf("They match\n");
				piece = fopen("4", "r");
				pathfinding(piece);
			}
			
		}
		
	}
```

One thing, for the djb2hash function, you are supposed to google it to find the code for it. Using that you generate a hash for a specific phrase, then input the phrase and the hash for it. Here is the code I used.

```c
#include <stdio.h>
#include <stdlib.h>

int main()
{
    char *str = "Chalk";
    unsigned long hash = 5381;
    printf("%s\n", str);
    int c;
    
    while (c = *str++)
        hash = ((hash << 5) + hash) + c; /* hash * 33 + c */
    
    printf("%lu\n", hash);
    return 0;
}
```

So after you reversed all of it, you should get the answers for everything.

```
North answers: "" + "10" & "38" + "9216"

East answers: "" + "" + "56991" & "57023"

West answers: "64" & "-1153"

South answers: "nan" & "Chalk" + output of hash (for chalk it's 217455688)

End String: 1dt6SE89dNEOnAdBzxtNllxgfH3VJCyJRWm9tDnanQJMkzSF2CKSKSTSkZDvTSkZDvheYsdA9ueFUJPeOzcTwoSPq5OpuLrhAzD35myz3XV38K2aQlqv1vZIfJNcM1HyiaLk88CO4MdeXbQIJdThWqicmv1pKjo3V5gGON0jcRQJGpcedJNEQPc2rY

flag: sun{w@5t4land_i5 @_dang3r0u5_p1@c3}
```
