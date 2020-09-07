#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void Test(void){
  char *str;
  str = (char *)malloc(10);

  strcpy(str,"testing");
  printf("%s\n",str);
}

int main(){
  Test();

  return 0;
}
