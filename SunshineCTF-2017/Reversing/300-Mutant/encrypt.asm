; make the check function visible to the linker
global encrypt

section .data
k dd 0x6c05,0x6f05,0x6c05,0x2d05,0x6905,0x7405,0x7305,0x2d05,0x6105,0x2d05,0x6b05,0x6505,0x7905
l dd 13

section .text

extern mprotect
; prototype: int __cdecl check(int a, int B)/>
; desc: checks two integers and returns the result
_get:
mov rax,[rsp]
ret ;

encrypt:
	push rbp ;
	mov rbp, rsp;
	sub rsp,24
	call _get;
	mov [rbp-8], rdi ; load rdi into local veriable
	mov [rbp-16], rax
	mov QWORD[rbp-24], 0 ; we need an index to keep track of where we are in the k
	mov eax, [rbp-16] ; mptotect all of the code from here down to be writeable
	cdq ; doing modulous to become page aligned
	shr edx,20
	add eax,edx
	and eax, 4095
	sub eax, edx ; result of modulous is stored in eax
	mov edi, DWORD[rbp-16]
	sub edi, eax ; we are now page aligned
	mov rsi,4096 ; page size
	mov rdx, 7 ; read write execute 
	call mprotect
	.L1:
		mov rax,[rbp-8]; moving character pointer into rax
		movzx eax,BYTE[rax];
		cmp eax, 0 ; checking if the char is null
		je .R1 ; if it is null, we have reached the end of the string
		add eax,0xff ; adding one to the current character
		mov edx,eax ; copying the new character into edx
		mov rax, [rbp-8] ; putiting the current character into rax
		mov [rax] ,dl ; updtating the character
		; here we are going to get the current position of the k
		mov rbx,k; int ptr to key is going in rbx
		mov rcx,[rbp-24] ; current position of k goes in rcx
		imul ecx,4 ;j
		add rbx,rcx
		mov ebx,DWORD[rbx]
		; this is where we are modifying our code
		mov rax,[rbp-16]
		add rax, 64
		mov DWORD[rax],ebx
		add QWORD[rbp-8], 1; moving to the next character
		;; i = (i+1)%21
		mov eax,[rbp-24] ; 
		add eax, 1 ; 
		xor edx,edx
		mov ecx,[l]
		idiv ecx
		mov DWORD[rbp-24], edx
		jmp .L1

	.R1:
		sub rsp, 24
		leave
		ret ; return
