<?php

$name = "Muhamad Ragil";


echo "Name :" . $name . PHP_EOL ;

$valueString = (string)100;
var_dump($valueString);

$valueInteger = (int)"100";
var_dump($valueInteger);

$valueFloat = (float)"1.01";
var_dump($valueFloat);

$name = "Ading";
echo $name[0] . PHP_EOL ;
echo $name[1] . PHP_EOL ;
echo $name[2] . PHP_EOL ;

// variable parsing
echo "Hello $name, Selamat Belajar PHP!" . PHP_EOL;


// curly Brace
$var = "var";
echo "This is {$var}s". PHP_EOL;