#include "header.h"

/* 文件属性操作 */
void file_stat(){
  const char * filename="test";
  struct stat * filestat;
  int rstat=stat(filename,filestat);
  printf("file stat return value is %d \n ",rstat);


}

int main(){
  file_stat();

}
