<?php
function encrypt($text, int $n) {
  if (empty($text) || $n <= 0) {
    return $text;
  }

  for ($y = 0; $y < $n; $y++) {
    $res1 = [];
    $res2 = [];

    $resFull = str_split($text);
    $cnt = count($resFull);
    ($cnt % 2 == 0) ? $isEven = true : $isEven = false;
    for ($i = 1; $i < $cnt; $i+=2) {
	    #print_r($res1);
	    #print_r($res2);
      $res1[] = $resFull[$i];
      $res2[] = $resFull[$i-1];
    }
    if (!$isEven) {
      $res2[] = $resFull[$cnt - 1];
    }
    $text = implode(array_merge($res1,$res2));
  }
  return $text . PHP_EOL;
}

function decrypt($text, int $n) {
    if (empty($text) || $n <= 0) {
	return $text;		      
    }	 
   for ($y = 0; $y < $n; $y++) {   
    $res = [];
    $resFull = str_split($text);
    $cnt = count($resFull);
    $dev = floor($cnt/2);
    ($cnt % 2 == 0) ? $isEven = true : $isEven = false;
    for ($i = 0; $i < $dev; $i++) {
	    $res[] =  $resFull[$dev + $i];
     $res[] = $resFull[$i];
    }
     if (!$isEven) {
	     $res[] =  $resFull[$cnt - 1];
     }
    $text = implode($res);
   }
   return $text . PHP_EOL; 
}

print_r(decrypt('elhlo', 1));
print_r(decrypt('hSi  etTi sats!', 1));
