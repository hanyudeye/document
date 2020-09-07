#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
/* 不带缓冲的 IO */

void file_io_test() {

  /* 打开文件 */

  /* 对于存在的文件，返回文件描述符，如果文件不存在，返回 -1 */
  printf("%d\n", open("./test", O_RDWR));
  printf("%d\n", open("./test", O_RDWR | O_CREAT, S_IRUSR | S_IWUSR));
  /* 文件打开一般用于如下用途。 */
  /*   - `O_RDONLY`常量：文件只读打开 */
  /*   - `O_WRONLY`常量：文件只写打开 */
  /*   - `O_RDWR`常量：文件读、写打开 */
  /*   - `O_EXEC`常量：只执行打开 */

  /* 读文件 */
  char read_buff[100];
  char write_buff[100];

  int fd = open("./test", O_RDWR | O_APPEND);
  if (fd != -1) {
    printf("here\n");

    int r = read(fd, read_buff, 30);
    printf("文件内容是%s\n", read_buff);
    printf("返回值%d\n", r);

    /* 定位文件到结尾，其实不做也可以，默认追加的  */
    off_t rl = lseek(fd, 0, SEEK_END);
    if (-1 == rl)
      printf("lseek 发生错误,错误为 %s\n", strerror(errno));
    else
      printf("lseek SEEK_END的返回值是 %ld\n", rl);

    /* 追加文字 hello world*/
    char writestr[] = "hello,world\n" ;
    strcpy(write_buff, writestr);
    write(fd,write_buff,sizeof(writestr));

    /* 再看下文件内容 */
    /* 自己打开文件 test看 */

  } else {
    printf("文件打不开\n");
  }
}

int main(int argc, char *argv[])
{

  /* 文件操作 */
  file_io_test();
  return 0;
}


