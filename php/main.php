<?php

include 'change_directory.php';

//
// Test 1
//
echo "\nTest1 - should display '/a/b/c/x'\n";
$path = new Path('/a/b/c/d');
$path->cd('../x');
echo  "$path->currentPath\n";


//
// Test 2
//
echo "\nTest2 - should display 'a' \n";
$path = new Path('/a/b/c/d');
echo  "$path->currentPath\n";
$path->cd('../../../b2/../');
echo  "$path->currentPath\n";




//
// Test 3 (not moving)
//
echo "\nTest3 - not moving\n";
$path = new Path('/a/b/c/d');
echo  "$path->currentPath\n";
$path->cd('./././');
echo  "$path->currentPath\n";


//
// Test 4 - parent of root
//
echo "\nTest4 - error\n";
$path = new Path('/');
echo  "$path->currentPath\n";
try {
    $path->cd('..');
    echo  "$path->currentPath\n";
} catch(\Error $e){
    error_log("Yup, error: " . $e->getMessage());
}

//
// Test 5
//
echo "\nTest3 - new absolute path\n";
$path = new Path('/a/b/c/d');
echo  "$path->currentPath\n";
$path->cd('/x/y/z');
echo  "$path->currentPath\n";

