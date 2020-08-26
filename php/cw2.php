<?php

function stray($arr)
{
  if (empty($arr)) {
    return null;
  }  
  
  $countInArr = count($arr);
  if (($countInArr <= 2) || (($countInArr % 2) == 0)) {
    return null;
  }

  if (!sort($arr, SORT_NUMERIC)) {
    return null;
  } 

  if ($arr[0] == $arr[1]) {
    if ($arr[$countInArr - 1] != $arr[$countInArr - 2]) {
      return $arr[$countInArr - 1];
    }
  } else {
    return $arr[0];
  } 
}

print_r(stray([2,2,3]) . PHP_EOL);
print_r(stray([4,3,3,3,3]) . PHP_EOL);
print_r(stray([6,6,6,6,6,1,6,6,6]) . PHP_EOL);
