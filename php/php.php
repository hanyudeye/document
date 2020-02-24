<?php

// header('Location: http://www.baidu.com/');

ini_set("display_errors", "On");
error_reporting(E_ALL); 

// echo timezone_version_get();

try {
    // afsdj afsd;
    $ex=   new Exception();
    // throwException($ex);
    ec();
}
catch(Exception $e){
    echo "hello";
    echo $e->__toString();
}catch(Error $x){

    echo "error";
    echo $x->__toString();
}
