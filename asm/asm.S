.section .data
output:
.ascii "The processor Vendor ID is 'XXXXXXXXXXXX'\n"

.section .text
.global _start
.code16

_start:
    jmp entry
    /*定义fat12文件格式*/
    .byte 0x00
    .ascii "helloOSX"
    .word  512
    .byte  1
    .word  1
    .byte  2
    .word  224
    .word  2880
    .byte  0xf0
    .word  9
    .word  18
    .word  2
    .long  0
    .long  2880
    .byte  0,0,0x29
    .long  0xffffffff
    .ascii  "myosudisk  "
    .ascii  "fat12   "
    .fill 18


entry:
    mov $0,%ax
    mov %ax,%ds
    mov %ax,%es
    mov %ax,%ss
    mov $0x7c00,%sp


puts:
  ;# 输出字符 'A'
  movb $0x0e,%ah
  movb $0x41,%al
  movw $0x0e,%bx
  int $0x10


  ;# 输出字符 'a'
  movb $0x0e,%ah
  movb $0x61,%al
  movw $0x0e,%bx
  int $0x10
 
  jmp .

msg:
	.asciz "\r\nmy bootloader is running"
my: .asciz "\r\nwelcome to our course "

.org 510
.word 0xaa55


















# linux中断函数

  ## movl	$0,	%eax		# The CPUID output option(the Vendor ID string)
  ## cpuid #cpuid 指令根据不同的 eax,输出不同的值
  ## movl	$output,%edi
  ## movl	%ebx, 	28(%edi)
  ## movl	%edx,	32(%edi)
  ## movl	%ecx,	36(%edi)

  ## movl	$42,	%edx	# 显示的字符数
  ## movl	$output,%ecx	# 缓冲区指针
  ## movl	$1,	%ebx	# 文件描述符
  ## movl	$4,	%eax	# 系统调用号，_write
  ## int	$0x80		# 系统调用

  ## movl	$0,	%ebx	# 传给_exit 的参数
  ## movl	$1,	%eax	# 系统调用号，_exit
  ## int	$0x80		# 系统调用

