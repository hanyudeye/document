#include <stdio.h>

void printarr(int* arr,int n){
  int i;
  for(i=0;i<n;i++){
    printf("%d",arr[i]);
  }
  printf("\n");
}

int main()
{
  int shuzis[4]={1,3,4,6};
  int num=4;

  printarr(shuzis,num);
  return 0;
}
