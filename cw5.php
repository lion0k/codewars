<?php
function revRot($s, $sz) {
  if ($sz <= 0 || empty($s)) {
    return '';
  }
  $cnt = strlen($s);
  if ($sz > $cnt) {
    return '';
  }
  
  $res = [];  
  $numChunk = floor($cnt / $sz);
  $tempArr = array_chunk(str_split($s), $sz);
  for ($i = 0; $i < $numChunk; $i++) {
    if (isSumDigitsDiv2($tempArr[$i])) {
      $res[] = array_reverse($tempArr[$i]);
    } else {
	    $firstVal = (array) array_shift($tempArr[$i]);
	    $res[] = array_merge($tempArr[$i], $firstVal);
    }
  }
  $strFin = '';
  foreach($res as $val) {
  	$strFin .= implode($val);
  }
  return $strFin;
}

function isSumDigitsDiv2(array $arr):bool {
  return (array_sum($arr) % 2 == 0) ? true : false;
}

print_r(revRot('123456987654', 6) . PHP_EOL);//234561876549
print_r(revRot('123456987653', 6) . PHP_EOL);//234561356789
print_r(revRot('', 6) . PHP_EOL);//234561356789
print_r(revRot('123456987653', 0) . PHP_EOL);//234561356789
