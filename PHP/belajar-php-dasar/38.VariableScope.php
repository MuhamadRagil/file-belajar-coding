<?php

$name = "Ragil"; //global scope

function sayHello()
{
    global $name;
    echo $name .PHP_EOL;
}

sayHello();