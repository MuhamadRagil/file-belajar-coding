<?php

$values = array(1, 2, 3, 4);
var_dump($values);

$name = ["Muhamad", "Ragil", "Agnal", "Azkiya"];
var_dump($name);


// operasi array
var_dump($name[0]);

$name[0]= "Muhammad";
var_dump($name);

unset($name[2]);
var_dump($name);

$name[] = "Agnal";
var_dump($name);

// membuat map dalam bahsa pemrograman php
$Ragil = array(
    "id" => "Ragil",
    "name" => "Agnal",
    "age" => 17 
);
var_dump($Ragil);


// array dalam array
$Ragil = array(
    "id" => "Ragil",
    "name" => "Agnal",
    "age" => 17,
    "address" => [
        "city" => "DEPOK",
        "country" => "INDONESIA"
    ]
);

var_dump($Ragil);
var_dump($Ragil["address"]["country"]);