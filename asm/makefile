file=asm
src=$(file).S
obj=$(file).o

elf=boot.elf
boot=boot.out
asm=boot.asm

# c程序
cfile=c
csrc=c.c

# 链接程序
$(boot):$(src)
	gcc -c $(src) -m32 -o $(obj)
	ld -m elf_i386 $(obj) -e _start -Ttext 0x7c00 -o $(elf)
	objcopy -S -O binary -j .text $(elf)  $(boot)
	objdump -S $(elf) > $(asm)

# 制作软盘
fat12:
	@dd if=/dev/zero of=$(boot) seek=1 count=2879 >> /dev/zero
	@ls -al $(boot)

# 执行模拟器
run:$(asm)
	qemu-system-x86_64 -fda $(boot)

# 清除中间文件
clean:
	-rm -f $(obj) $(elf) $(boot) $(asm)

c:$(cfile).c
	gcc $< -o $@
