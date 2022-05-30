<?php

$counter = 1;

for ( ; $counter <= 10 ; ){
    echo "Ini adalah forlopp ke- $counter" . PHP_EOL;
    $counter++;
}

// perulangan init statement
for ($counter = 1; $counter <= 10 ; ){
    echo "Ini adalah forlopp ke- $counter" . PHP_EOL;
    $counter++;
}

// perulangan post statement
for ( $counter = 1; $counter <= 10 ; $counter++ ){
    echo "Ini adalah forlopp ke- $counter" . PHP_EOL;
}

// alternatif
for ( $counter = 1; $counter <= 10 ; $counter++ ):
    echo "Ini adalah forlopp ke- $counter" . PHP_EOL;
endfor;