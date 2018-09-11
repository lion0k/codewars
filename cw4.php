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
    $cntArr = floor($cnt/2);    
    ($cnt % 2 == 0) ? $isEven = true : $isEven = false;
    for ($i = 0; $i < $cntArr; $i++) {
	    #print_r($res1);
	    #print_r($res2);
      $res1[] = $resFull[$i+1];
      $res2[] = $resFull[$i];
    }
    print_r($res1);
    print_r($res2);
    if (!$isEven) {
      $res2[] = $resFull[$cnt - 1];
      $text = implode(array_merge($res1,$res2));
    }
  }
  return $text;
}
print_r(encrypt('hello', 1));





