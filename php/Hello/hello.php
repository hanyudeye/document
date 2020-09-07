<?php

class Shizi{
    public  $name="狮子";

    public function print(){
        printf("我是一只狮子！\n");
    }
}

// echo "hello,PHP!\n";

// echo "你好！\n";

// $read=readline("请输入文字");
// echo "输入的文字是\n";

// echo $read;

$s=new Shizi();
$s->print();

printf($s->name);
