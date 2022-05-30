<?php

$name = "Ragil";
$name = null;

$age = null;


echo "Nama : ";
echo $name;
echo "\n";

echo "Age : ";
echo $age;
echo "\n";

// mengecek nilai null
echo "name is null ? ";
var_dump(is_null($name));


// menghapus variable
$contoh = "Ragil";
unset($contoh);

echo $contoh;

$contoh = "Ragil";
unset($contoh);

var_dump(isset($contoh));