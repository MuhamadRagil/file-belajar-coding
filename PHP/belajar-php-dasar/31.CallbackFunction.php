<?php

function sayHello (string $name , callable $filter)
{
    $finalName = call_user_func($filter,$name);
    echo"Hello $finalName" . PHP_EOL;
}

sayHello("Ragil", "strtoupper");
sayHello("Ragil","strtolower");
sayHello("Ragil", function(string $name): string 
{
    return strtoupper($name);
});
sayHello("Ragil", fn($name) => strtoupper($name));