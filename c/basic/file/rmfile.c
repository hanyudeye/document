#include <stdio.h>
int main() {
  char filename[80];
  printf("The file to delete:");
  gets(filename);
  
  if (remove(filename) == 0)
    printf("Removed %s.", filename);
  else
    perror("remove");
}
