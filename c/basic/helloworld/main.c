#include <stdio.h>

/*
 * @author aming
 * @date 2020 年 03 月 20 日 
 * 输出 Hello,world 到屏幕上
 */

extern int hello();

int main(void){
    printf("Hello, World!\n");
    int size=23;
    int mianji = size * size;
    printf("体积是 %d\n",mianji);
    hello();
    return 0;
}

/* 函数 */
int hello() {
  printf("good\n");
  printf("nice\n");
  return 0;
}
