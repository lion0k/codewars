<?php
function sqInRect($lng, $wdth) {
  if ($lng === $wdth) {
    return null;
  }

  $res = [];
  while (($lng - $wdth) != 0) {

  #do {
    if ($lng < $wdth) {
      $wdth = abs($lng - $wdth);
      $res[] = $lng;
    } else {
      $lng = abs($lng - $wdth);
      $res[] = $wdth;
    }
  } #while (($lng - $wdth) != 0);
  #$res[] = $lng;
  return $res;
}

print_r(sqInRect(5, 3)); // 3 2 1 1
print_r(sqInRect(20, 14)); // 14, 6, 6, 2, 2, 2
