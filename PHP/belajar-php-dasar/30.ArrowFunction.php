<?php

$firstName = "Ragil";
$lastName = "Agnal";

$arrowFunction = fn() => "Hello $firstName $lastName" . PHP_EOL;

echo $arrowFunction();