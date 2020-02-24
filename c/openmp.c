#include <omp.h>
#include <stdio.h>

int int main(int argc, char *argv[])
{
#pragma omp parallel{
  printf("I am a parallel region\n");
}
  return 0;
}
