<?php
function find_even_index($arr){
  if (empty($arr)) {
    return 0;
  }

  $sumArr = array_sum($arr);
  if ($sumArr == 0) {
    return $sumArr;
  }

  $cnt = count($arr);
  if ($cnt == 1) {
    return -1;
  }

  $halfArr = 0;
  $halfSum = 0;
  for ($i = 0; $i < $cnt-1; $i++) {
    $halfSum += $arr[$i];
    if ($halfArr == ($sumArr - $halfSum)) {
      return $i;
    } else {
      $halfArr += $arr[$i];
    }    
  }
  return -1;
}

print_r(find_even_index([1,2,3,4,3,2,1]) .' = 3' . PHP_EOL);
print_r(find_even_index([1,100,50,-51,1,1]) . ' = 1' . PHP_EOL);
print_r(find_even_index([20,10,-80,10,10,15,35]) . ' = empty' . PHP_EOL);
print_r(find_even_index(range(1,100)) .' = -1' . PHP_EOL);
print_r(find_even_index(range(-100,-1)) .' = -1' . PHP_EOL);


