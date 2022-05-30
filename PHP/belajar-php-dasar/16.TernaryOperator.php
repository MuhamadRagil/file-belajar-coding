<?php

$gender = "PRIA";
$hi = null;

if($gender == "PRIA"){
    $hi = "Hallo Bro!";
}else{
    $hi = "Hallo Nona!";
}

echo $hi . PHP_EOL;

$hi = $gender == "PRIA" ? "HI, BRO!" : "HI, NONA!";

echo $hi > PHP_EOL;