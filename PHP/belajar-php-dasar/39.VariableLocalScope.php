<?php

function creatName(){
    $name = "Ragil"; //local scope
}

creatName();
echo $name . PHP_EOL;