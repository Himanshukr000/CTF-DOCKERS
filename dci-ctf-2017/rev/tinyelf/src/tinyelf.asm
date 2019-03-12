            db      0x7F    ; * id  0                   ; START OF ELF HEADER
            db      0x45    ; * id  1 (E)
            db      0x4C    ; * id  2 (L)
            db      0x46    ; * id  3 (F)
            db      0x58    ; file class            ; pop eax
            db      0x3c    ; data encoding         ; cmp al, 2 (1)
            db      0x02    ; File version          ; cmp al, 2 (2)
jz bridge  ;db      0x74    ; OS/ABI                ; jz short +11 (1)
           ;db      0x0b    ; padding 1             ; jz short +11 (2)
end:        db      0xb3    ; padding 2             ; mov bl, 1 (1)
            db      0x01    ; padding 3             ; mov bl, 1 (2)
            db      0x31    ; padding 4             ; xor eax, eax (1)
            db      0xc0    ; padding 5             ; xor eax, eax (2)
            db      0x40    ; padding 6             ; inc eax
            db      0xcd    ; padding 7             ; int 0x80 (1)
            db      0x80    ; padding 8             ; int 0x80 (2)
            db      0x02    ; * e_type_1
            db      0x00    ; * e_type_2
            db      0x03    ; * e_architecture_1
            db      0x00    ; * e_architecture_2
bridge:     db      0xb4    ; e_version_1           ; mov ah, 32 (1)
            db      0x20    ; e_version_2           ; mov ah, 32 (2)
jmp solve  ;db      0xeb    ; e_version_3           ; jmp short +22 (1)
           ;db      0x16    ; e_version_4           ; jmp short +22 (1)
            db      0x04    ; + e_entry_1
            db      0x20    ; + e_entry_2
            db      0x00    ; + e_entry_3
            db      0x01    ; + e_entry_4
            db      0x21    ; + e_progHeaderoff_1
            db      0x00    ; + e_progHeaderoff_2
            db      0x00    ; + e_progHeaderoff_3
            db      0x00    ; + e_progHeaderoff_4
            db      0xff    ; e_sectionHeaderOff_1  ; free byte
            db      0x01    ; e_sectionHeaderOff_2      ; START OF PROGRAM HEADER   ; * p_type_1
            db      0x00    ; e_sectionHeaderOff_3                                  ; * p_type_2
            db      0x00    ; e_sectionHeaderOff_4                                  ; * p_type_3
            db      0x00    ; e_flags_1                                             ; * p_type_4
            db      0x00    ; e_flags_2                                             ; * p_offset_1
            db      0x00    ; e_flags_3                                             ; * p_offset_2
            db      0x00    ; e_flags_4                                             ; * p_offset_3
            db      0x00    ; + e_ehsize_1                                          ; * p_offset_4
            db      0x00    ; + e_ehsize_2                                          ; + p_vaddr_1
            db      0x20    ; + e_phentsize_1                                       ; + p_vaddr_2
            db      0x00    ; + e_phentsize_2                                       ; + p_vaddr_3
            db      0x01    ; * e_phnum_1                                           ; + p_vaddr_4
            db      0x00    ; * e_phnum_2                                           ; p_paddr_1
solve:      db      0x31    ; e_shentsize_1         ; xor ecx, ecx (1)              ; p_paddr_2
            db      0xc9    ; e_shentsize_2         ; xor ecx, ecx (2)              ; p_paddr_3
            db      0xbb    ; e_shnum_1             ; mov ebx, 0x01002000 (1)       ; p_paddr_4
            db      0x00    ; e_shnum_2   c0        ; mov ebx, 0x01002000 (2)       ; * p_filesz_1
            db      0x20    ; e_shstrndx_1          ; mov ebx, 0x01002000 (3)       ; + p_filesz_2
            db      0x00    ; e_shstrndx_2          ; m ; END OF ELF HEADER         ; p_filesz_3
            db      0x01                            ; mov ebx, 0x01002000 (5)       ; p_filesz_4
            db      0x5e                            ; pop esi                       ; p_memsz_1
            db      0x5e                            ; pop esi                       ; p_memsz_2
jmp skippf ;db      0xeb                            ; jmp short +1 (1)              ; p_memsz_3
           ;db      0x01                            ; jmp short +1 (2)              ; p_memsz_4
            db      0x07                                                            ; * p_flags_1
skippf:     db      0x20                            ; and [ebx+0x0a], cl (1)        ; p_flags_2
            db      0x4b                            ; and [ebx+0x0a], cl (2)        ; p_flags_3
            db      0x0a                            ; and [ebx+0x0a], cl (3)        ; p_flags_4
loop1:      db      0x56                            ; > push esi                    ; p_align_1
            db      0x53                            ; > push ebx                    ; p_align_2
            db      0x01                            ; > add esi, ecx (1)            ; p_align_3
            db      0xce                            ; > ; END OF PROGRAM HEADER     ; p_align_4
            db      0x01                            ; > add ebx, ecx (1)
            db      0xcb                            ; > add ebx, ecx (2)
            db      0x31                            ; > xor edx, edx (1)
            db      0xd2                            ; > xor edx, edx (2)
            db      0x30                            ; > xor al, al (1)
            db      0xc0                            ; > xor al, al (2)
loop2:      db      0x02                            ; >> add al, [ebx] (1)
            db      0x03                            ; >> add al, [ebx] (2)
            db      0x00                            ; >> add bl, ah (1)
            db      0xe3                            ; >> add bl, ah (2)
            db      0x42                            ; >> inc edx
            db      0x83                            ; >> cmp edx, 4 (1)
            db      0xfa                            ; >> cmp edx, 4 (2)
            db      0x04                            ; >> cmp edx, 4 (3)
jnz loop2  ;db      0x75                            ; >> jnz short -10 (1)
           ;db      0xf6                            ; >> jnz short -10 (2)
            db      0x5b                            ; > pop ebx
            db      0x32                            ; > xor al, [esi]
            db      0x06                            ; > xor al, [esi]
            db      0x08                            ; > or [ebx+0x0a], al
            db      0x43                            ; > or [ebx+0x0a], al
            db      0x0a                            ; > or [ebx+0x0a], al
            db      0x5e                            ; > pop esi
            db      0x41                            ; > inc ecx
            db      0x38                            ; > cmp cl, ah
            db      0xe1                            ; > cmp cl, ah
jnz loop1  ;db      0x75                            ; > jnz short
           ;db      0x20                            ; > jnz short
jmp end    ;db      0xeb                            ; jmp short -86
           ;db      0xaa                            ; jmp short -86
            db      0x00                            ; free byte
            db      0xf8                            ; flag byte
            db      0xfc                            ; flag byte
            db      0x32                            ; flag byte
            db      0x04                            ; flag byte
            db      0x2a                            ; flag byte
            db      0x03                            ; flag byte
            db      0x6e                            ; flag byte
            db      0xf9                            ; flag byte
            db      0x3f                            ; flag byte
            db      0x81                            ; flag byte
            db      0x6b                            ; flag byte
            db      0x06                            ; flag byte
            db      0xec                            ; flag byte
            db      0x36                            ; flag byte
            db      0x72                            ; flag byte
            db      0x73                            ; flag byte
            db      0xba                            ; flag byte
            db      0x0e                            ; flag byte
            db      0x25                            ; flag byte
            db      0x2e                            ; flag byte
            db      0xb7                            ; flag byte
            db      0x70                            ; flag byte
            db      0x1c                            ; flag byte
            db      0x0f                            ; flag byte
            db      0x2d                            ; flag byte
            db      0xec                            ; flag byte
            db      0x68                            ; flag byte
            db      0x70                            ; flag byte
            db      0x61                            ; flag byte
            db      0x32                            ; flag byte
            db      0x58                            ; flag byte
            db      0x7c                            ; flag byte
; nasm -f bin tinyelf.asm -o tinyelf
; chmod +x tinyelf
