#include <omp.h>
#include <stdio.h>

int int main(int argc, char *argv[])
{
  pragmaomp parallel{
    printf("I am a parallel region\n");
  }
  return 0;
}

