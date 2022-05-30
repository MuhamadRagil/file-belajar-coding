<?php

$total = 0;

$fruit = "10000";
$chicken = "5000";
$orangeJuice = "15000";

// jika pake cara biasa
// $total = $total + $fruit;

$total += $fruit;
$total += $chicken;
$total += $orangeJuice;

var_dump($total);
