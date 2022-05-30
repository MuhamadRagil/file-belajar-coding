<?php

require_once "data/person.php";

$Person = new person("Andi","Ragil");
$Person->name = "Andi";
$Person->sayHello(null);

$Person->info();