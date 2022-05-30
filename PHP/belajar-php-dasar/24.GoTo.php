<?php

goto a;
echo "Hello ini GoTo";


a:
echo "Ini lompatan goto";





$counter = 1;

while (true){
    echo "Ini adalah forlopp ke- $counter" . PHP_EOL;
    $counter++;

    if($counter > 10){
        goto end;
    }
}

end:
echo "End break";