#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define LEN 20
  int main(int argc, char *argv[])
  {

    char buf[LEN];

    int s= creat("helloworld",S_IRWXU | S_IRWXG);
    if(s != -1){
      printf("create sucess \n");
    }else{
      printf("create fail \n");
    }

    return 0;
  }
