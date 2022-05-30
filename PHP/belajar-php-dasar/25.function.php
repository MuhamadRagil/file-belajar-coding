<?php

function sayHello()
{
    echo "Hi ini adalah function" . PHP_EOL;
}

sayHello();


// jika menggunakan if statement
$buat = false;

if ($buat){
    function sayHello()
    {
        echo "Hi ini adalah function" . PHP_EOL;
    }   
}

sayHello();