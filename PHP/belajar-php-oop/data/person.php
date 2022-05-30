<?php

class Person
{

    // const in class
    const AUTHOR = "Try Code Me";

    // properties
    //type declaration
    var string $name;
    // nullable properties
    var ?string $addres = null;
    // default value
    var string $country = "Indonesia";

    //constructor function
    function __construct(string $name, ?string $addres){
        $this->name = $name;
        $this->addres = $addres;
    }

    function sayHello(?string $name)
    {
        if(is_null($name)){
            echo "Hi my name is $this->name" .PHP_EOL;    
        }else{
            echo "Hi $name, my name is $this->name" .PHP_EOL;
        }
        
    }

    // function untuk const
    function info() //self used for const acces in the same class
    {
        echo "Author :" . self::AUTHOR .PHP_EOL; 
    }

    // function destruct
    function __destruct()
    {
        echo "Object person $this->name is destroyed" . PHP_EOL;
    }
}