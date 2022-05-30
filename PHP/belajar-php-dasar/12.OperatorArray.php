<?php

// Union
$first = [
    "first_name" => "Muhamad Ragil"
];

$last = [
    "last_name" => "Agnal Azkiya"
];

$full = $first + $last;
var_dump($full);

// Equality
$a = [
    "first_name" => "Muhammad Ragil",
    "last_name" => "Agnal Azkiya"
];

$b = [
    "last_name" => "Agnal Azkiya",
    "first_name" => "Muhammad Ragil"
];

var_dump($a == $b);
var_dump($a === $b);