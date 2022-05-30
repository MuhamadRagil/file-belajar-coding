<?php

$sayHello = function(string $name){
    echo "Hello $name" . PHP_EOL;
};

$sayHello("Ragil");



function sayGoodBye(string $name, $filter){
    $finalName = $filter($name);
    echo "GoodBye $finalName" .PHP_EOL;
}

sayGoodBye("Ragil", function(string $name): string{
    return strtoupper($name);
});

$filterFunction = function(string $name): string{
    return strtoupper($name);
};

sayGoodBye("Ragil", $filterFunction);

//mengakses function diuar variable
$firstName = "Ragil";
$lastName = "Agnal";

$sayHelloRagil = function() use($firstName, $lastName){
    return "Hello $firstName $lastName" .PHP_EOL;
};

echo $sayHelloRagil();