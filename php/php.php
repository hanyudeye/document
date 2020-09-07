<?php

// header('Location: http://www.baidu.com/');

ini_set("display_errors", "On");
error_reporting(E_ALL); 

// echo timezone_version_get();

setcookie("usern","aming", time()+60,"/","localhost",0);
// setcookie("user", "aming", time()+60,'/',".localhost",0);

// echo( '你好，世界' );

// loads the wordpress environment and template.
// 加载环境和模板

if(! isset($wp_did_header)){
    $wp_did_header = true;

// load the wordpress library
    require_once(dirname(__FILE__).'/wp-load.php');
    // set up the wordpress query
    wp();

    // load the theme template
    require_once(ABSPATH.WPINC.'/template-loader.php');
}

// bootstrap file for setting the ABSPATH constant
// and loading the wp-config.php file. The wp-config.php
// file will then load the wp-settings.php file,which
// will then set up the wordpress environment.

// if the wp-config.php file is not fonund then an error
// will be displayed asking the visitor to set up the wp-config.php file.

// will also search for wp-config.php in wordpress' parent
// directory to allow the wordpress directory to remain untouched.

// ;; @package wordpress

// define abspath as  this file's directory
if(!defined('ABSPATH')){
    define('ABSPATH',dirname(__FILE__).'/');
}

error_reporting(E_CORE_ERROR | E_CORE_WARNING | E_COMPILE_ERROR | E_ERROR | E_WARNING | E_PARSE | E_USER_ERROR | E_USER_WARNING | E_RECOVERABLE_ERROR);

/**
 * If wp-config.php Exists in the wordPress root , or if it exists in the root and wp-settings.php
 * doesn't ,load wp-config.php. The secondary check for wp-settings.php has the 
 * added benefit of avoiding cases where the current directory is a nested installation,e.g. / is wordPress(a ) and /blog/ is wordpress (b).
 * If neither set of conditions is true, initiate loading the setup process.
*/

if(file_exists(ABSPATH.'wp-config.php')){
    /** The config file resides in ABSPATH */
    require_once(ABSPATH.'wp-config.php');
}elseif (@file_exists(dirname(ABSPATH).'wp-config.php') && !@file_exists(dirname(ABSPATH).'/wp-settings.php')){
    /** the config file resides one level above ABSPATH but is not part of another installation*/ 
    require_once(dirname(ABSPATH).'/wp-config.php');
}else{
    //A config file doesn't exist
    define('WPINC','wp-includes');
    require_once(ABSPATH.WPINC.'/load.php');

    //Standardize $_SERVER variables across setups.
}
