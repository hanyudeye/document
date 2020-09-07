#include "header.h"

/* 文件属性操作 */
void file_stat(const char *filename) {
  struct stat file_stat;

  int rstat = lstat(filename, &file_stat);

  if (-1 == rstat)
    printf("file stat return value is %d \n ", rstat);
  else{
    /* printf("ID of containing device:  [%lx,%lx]\n", (long)major(file_stat.st_dev), */
    /*        (long)minor(file_stat.st_dev)); */

    if (S_ISREG(file_stat.st_mode))
      printf("regular file,\t");
    if (S_ISDIR(file_stat.st_mode))
      printf("directory file,\t");
    if (S_ISCHR(file_stat.st_mode))
      printf("char file,\t");
    if (S_ISBLK(file_stat.st_mode))
      printf(" block file,\t");
    if (S_ISFIFO(file_stat.st_mode))
      printf("fifo  file,\t");
    if (S_ISLNK(file_stat.st_mode))
      printf("link file,\t");
    if (S_ISSOCK(file_stat.st_mode))
      printf("socket,\t");
    if (S_TYPEISMQ(&file_stat))
      printf("message queue file,\t");
    if (S_TYPEISSEM(&file_stat))
      printf("semaphore,\t");
    if (S_TYPEISSHM(&file_stat))
      printf("share memory,\t");
    printf("\n");
  }
}

int main() {
  file_stat("test");
  file_stat("/home/");
  file_stat("/dev/loop0");
  file_stat("/dev/mem");
  file_stat("/dev/stdin");
}
