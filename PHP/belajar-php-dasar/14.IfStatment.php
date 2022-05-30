<?php

$nilai = 75;
$absen = 90;

if($nilai >= 75 && $absen >= 75){
    echo "Selamat Anda Lulus!". PHP_EOL;
}else{
    echo "Maaf, Anda tidak lulus". PHP_EOL;
}

if($nilai >= 80 && $absen >= 80){
    echo "Nilai Anda A". PHP_EOL;
}else if($nilai >= 70 && $absen >= 70){
    echo "Nilai Anda B". PHP_EOL;
}else if($nilai >= 60 && $absen >= 60){
    echo "Nilai Anda C". PHP_EOL;
}else{
    echo "Nilai Anda D". PHP_EOL;
}


if($nilai >= 80 && $absen >= 80):
    echo "Nilai Anda A". PHP_EOL;
elseif($nilai >= 70 && $absen >= 70):
    echo "Nilai Anda B". PHP_EOL;
elseif($nilai >= 60 && $absen >= 60):
    echo "Nilai Anda C". PHP_EOL;
else:
    echo "Nilai Anda D". PHP_EOL;
endif;