; Test assembly code

section .bss
    ; variable definition section


section .data
    ; constant definition section

    hello: db "Hello World!", 10
    ; string to print

    helloLen: equ $-hello
    ; length of string



section .text
    ; code logic section

    global _start
    ; entry point for linker

    _start:
    ; start of function

    mov     rax, 1          ; system write
    mov     rdi, 1          ; stdout
    mov     rsi, hello      ; message to write
    mov     rdx, helloLen   ; message length
    syscall                 ; call 
    
    ; end of program below
    mov     rax, 60         ; system exit
    mov     rdi, 0          ; error code 0 (succesfully exit)
    syscall




