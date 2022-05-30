<?php

$data = [];

if(isset($data["action"])){
    $action = $data["action"];
}else{
    $action = "Nothing";
};

echo $action;

//alternatif
$data = [];
$action = $data["action"] ?? "Nothing";

echo $action;