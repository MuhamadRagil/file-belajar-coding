<?php

require_once "data/person.php";

$Person = new person("Ragil","Depok");
$Person->name = "Ragil";
$Person->addres = "Depok";
$Person->country = "Indonesia";


var_dump($Person);

echo "Name : $Person->name" .PHP_EOL;
echo "Addres : $Person->addres" .PHP_EOL;
echo "Country : $Person->country" .PHP_EOL;